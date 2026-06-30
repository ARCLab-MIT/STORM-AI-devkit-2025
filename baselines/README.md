
# Baseline submissions
Participants submit their trained algorithm together with the code/workflow that generates predictions to the competition platform, in the programming language they prefer. Here we provide a Docker container and an example submission in Python, but participants are allowed to submit with other custom containers too. 

## Evaluation script
The `evaluation.py` script provides participants a simple way to assess the performance of the models they submit for the challenge. It reproduces locally the **public** challenge metric, so you can estimate your leaderboard score before submitting.

The toy datasets `ground_truth_toy.json` and `participant_toy.json` serve as simplified, 
example datasets for the challenge. These datasets are intended for initial 
testing and understanding of the simplified evaluation script and the baseline model.

### Example Usage
The `run_evaluator` function is the main entry point of the script and accepts the following arguments:

- `participant`: Path to the participant's prediction JSON file.
- `ground_truth`: Path to the ground truth JSON file (which also carries the MSIS baseline densities).

You can also run the script directly from the command line. For example:
```bash
python evaluation.py --participant=participant.json --ground_truth=ground_truth.json
```
Both files use the same JSON schema as the submission `prediction.json` (a `File ID` mapping to `Timestamp` and `Orbit Mean Density (kg/m^3)` arrays).

### Returns
The `score` function returns the challenge's public metric: the **Orbit-Density RMSE skill score (OD-RMSE)**, implemented in the code as the *Propagation Score (PS)*. It measures the percentage improvement of a submission's density forecast over the MSIS baseline, weighting early lead times more heavily because small early errors compound into large trajectory deviations. A score of `1` is a perfect forecast, `0` is parity with the MSIS baseline, and negative values are worse than the baseline. The private leaderboard additionally used a storm-aware variant (SSAOD-RMSE) that up-weights periods of high geomagnetic activity; see the [paper](https://2025-ai-challenge.readthedocs.io/en/latest/cite.html) for the full definitions. 
