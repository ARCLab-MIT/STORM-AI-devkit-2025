import numpy as np
import pandas as pd
import argparse
import json
import os

class DensityModelEvaluator:
    def __init__(self, ground_truth_file, participant_file):
        """
        Initialize the evaluator with ground truth and participant data.
        
        Args:
        - ground_truth_file (str): Path to the ground truth JSON file.
        - participant_file (str): Path to the participant JSON file.
        """
        self.ground_truth = self._load_json(ground_truth_file)
        self.participant = self._load_json(participant_file)

        # Validate structure
        if not self._validate_data():
            raise ValueError("Mismatch between ground truth and participant data structure.")
        
    def _load_json(self, file_path):
        """Load and parse the JSON file."""
        with open(file_path, 'r') as f:
            return json.load(f)

    def _validate_data(self):
        """
        Validates that both ground truth and participant data contain the same keys.

        Returns:
            bool: True if data keys match, False otherwise.
        """
        ground_truth_keys = set(self.ground_truth.keys())
        participant_keys = set(self.participant.keys())
        return ground_truth_keys == participant_keys

     def _pad_or_truncate(self, array, target_length):
            """
            Adjusts the length of an array by padding with NaNs or truncating.
    
            Args:
                array (np.ndarray): Input array.
                target_length (int): Desired length of the array.
    
            Returns:
                np.ndarray: Adjusted array with length equal to target_length.
            """
            current_length = len(array)
            if current_length == target_length:
                return array
            elif current_length < target_length:
                padding = np.full(target_length - current_length, np.nan)
                return np.concatenate([array, padding])
            else:
                return array[:target_length]

    def _prepare_dataframe(self):
        """
        Combines ground truth, MSIS, and participant data into a single DataFrame.

        Returns:
            pd.DataFrame: Combined DataFrame containing all relevant data.
        """
        combined_data = []

        for file_id in self.ground_truth.keys():
            # Convert timestamps to datetime objects
            timestamps = pd.to_datetime(self.ground_truth[file_id]['Timestamp'], errors='coerce')
            num_timestamps = len(timestamps)

            # Extract density arrays
            truth_density = np.array(self.ground_truth[file_id]['Orbit Mean Density (kg/m^3)'])
            msis_density = np.array(self.ground_truth[file_id]['MSIS Orbit Mean Density (kg/m^3)'])
            pred_density = np.array(self.participant[file_id]['Orbit Mean Density (kg/m^3)'])

            # Align array lengths
            truth_density = self._pad_or_truncate(truth_density, num_timestamps)
            msis_density = self._pad_or_truncate(msis_density, num_timestamps)
            pred_density = self._pad_or_truncate(pred_density, num_timestamps)

            # Create DataFrame for the current file_id
            file_df = pd.DataFrame({
                'FileID': [file_id] * num_timestamps,
                'Timestamp': timestamps,
                'TruthDensity': truth_density,
                'MSISDensity': msis_density,
                'PredictDensity': pred_density
            })

            # Calculate DeltaTime in seconds from the first timestamp
            file_df['DeltaTime'] = (file_df['Timestamp'] - file_df['Timestamp'].iloc[0]).dt.total_seconds()

            combined_data.append(file_df)

        # Concatenate all individual DataFrames
        combined_df = pd.concat(combined_data, ignore_index=True)

        # Replace invalid density values with NaN
        combined_df.replace(9.99e32, np.nan, inplace=True)

        # Remove rows with any NaN in key density columns
        combined_df.dropna(subset=['TruthDensity', 'MSISDensity', 'PredictDensity'], inplace=True)

        return combined_df

    def score(self, epsilon=1e-5):
        """
        Computes the Propagation Score (PS) based on the provided data.

        Args:
            epsilon (float, optional): Minimum weight value at the end of the forecast period. Defaults to 1e-5.

        Returns:
            float: Calculated Propagation Score (PS). Returns np.nan if no valid data is available.
        """
        # Prepare the combined DataFrame
        combined_df = self._prepare_dataframe()

        if combined_df.empty:
            return np.nan

        # Calculate squared errors for MSIS and participant predictions
        combined_df['MSIS_ErrorSq'] = (combined_df['MSISDensity'] - combined_df['TruthDensity']) ** 2
        combined_df['Pred_ErrorSq'] = (combined_df['PredictDensity'] - combined_df['TruthDensity']) ** 2

        # Compute mean squared errors grouped by DeltaTime
        mse_grouped = combined_df.groupby('DeltaTime')[['MSIS_ErrorSq', 'Pred_ErrorSq']].mean()

        # Calculate RMSE by taking square roots of MSE
        rmse_df = mse_grouped.apply(np.sqrt)
        rmse_df.columns = ['MSIS_RMSE', 'Pred_RMSE']

        # Calculate exponential weights based on DeltaTime
        delta_times = rmse_df.index.values
        if len(delta_times) < 2:
            weights = np.ones_like(delta_times, dtype=float)
        else:
            total_duration = max(delta_times[-1] - delta_times[0], 1e-12)
            decay_rate = -np.log(epsilon) / total_duration
            weights = np.exp(-decay_rate * (delta_times - delta_times[0]))

        # Avoid division by zero by replacing zero RMSE with a small value
        rmse_df['MSIS_RMSE'].replace(0, 1e-32, inplace=True)

        # Compute the skill score for each DeltaTime
        rmse_df['Skill'] = 1 - (rmse_df['Pred_RMSE'] / rmse_df['MSIS_RMSE'])

        skill_scores = rmse_df['Skill'].values

        if np.all(np.isnan(skill_scores)):
            return np.nan

        # Calculate the weighted average of skill scores
        propagation_score = np.average(skill_scores, weights=weights)
        return propagation_score

def run_evaluator(ground_truth_path=None, participant_path=None):
    """
    Runs the evaluation of the participant's model by calculating the Propagation Score (PS).
    
    Args:
    - ground_truth_path (str): Path to the ground truth JSON file.
    - participant_path (str): Path to the participant JSON file.
    """
    evaluator = DensityModelEvaluator(ground_truth_path, participant_path)
    ps = evaluator.score()
    print(f'Propagation Score (PS): {ps:.6f}')
    return ps


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ground_truth', type=str, required=True, help='Path to the ground truth JSON file.')
    parser.add_argument('--participant', type=str, required=True, help='Path to the participant JSON file.')
    args = parser.parse_args()
    run_evaluator(args.ground_truth, args.participant)
