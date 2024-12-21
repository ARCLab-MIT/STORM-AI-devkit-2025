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
            data = json.load(f)
        return data

    def _validate_data(self):
        """Validate that the ground truth and participant data have the same timestamps."""
        for key in self.ground_truth.keys():
            if key not in self.participant:
                return False
            if self.ground_truth[key]['Timestamp'] != self.participant[key]['Timestamp']:
                return False
        return True

    def _compute_weight(self, timestamps, epsilon=1e-5):
        """
        Compute exponential decay weights based on the time difference.
        
        Args:
        - timestamps (list): List of ISO 8601 timestamps.
        - epsilon (float): Minimum weight value at the end of the forecast period.
        
        Returns:
        - np.array: Array of weights.
        """
        t_seconds = np.array(pd.to_datetime(timestamps) - pd.to_datetime(timestamps[0]), dtype='timedelta64[s]').astype(int)
        duration = t_seconds[-1]
        gamma = -np.log(epsilon) / duration
        weights = np.exp(-gamma * t_seconds)
        return weights

    def _rmse(self, true_values, predicted_values):
        """Compute RMSE between two arrays."""
        return np.sqrt(np.mean((np.array(true_values) - np.array(predicted_values)) ** 2))

    def score(self):
        """
        Calculate the Propagation Score (PS) across all datasets.
        
        Returns:
        - float: Propagation Score (PS).
        """
        total_score = 0
        total_weight = 0

        for key in self.ground_truth.keys():
            timestamps = self.ground_truth[key]['Timestamp']
            true_density = self.ground_truth[key]['Orbit Mean Density (kg/m^3)']
            msis_density = self.ground_truth[key]['MSIS Orbit Mean Density (kg/m^3)']
            test_density = self.participant[key]['Orbit Mean Density (kg/m^3)']

            # Compute weights
            weights = self._compute_weight(timestamps)

            # Compute RMSE for MSIS and test densities
            rmse_test = self._rmse(true_density, test_density)
            rmse_msis = self._rmse(true_density, msis_density)
            
            # Avoid division by zero
            rmse_msis = max(rmse_msis, 1e-10)

            # Compute skill score
            skill_score = 1 - (rmse_test / rmse_msis)

            # Aggregate weighted scores
            total_score += skill_score * np.sum(weights)
            total_weight += np.sum(weights)

        # Final Propagation Score
        propagation_score = total_score / total_weight
        return propagation_score


def run_evaluator(ground_truth_path=None, participant_path=None):
    """
    Runs the evaluation of the participant's model by calculating the Propagation Score (PS).
    
    Args:
    - ground_truth_path (str): Path to the ground truth JSON file.
    - participant_path (str): Path to the participant JSON file.
    """
    if participant_path is None:
        participant_df = '../toy_data/participant_toy.csv'
    
    if ground_truth_path is None:
        ground_truth_path = '../toy/grountruth_toy.csv'

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
