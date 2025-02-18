import torch
from pathlib import Path
import dill
import time
import os
import pandas as pd
from datetime import datetime
from orekit.pyhelpers import setup_orekit_curdir
from org.orekit.time import AbsoluteDate, TimeScalesFactory
from org.orekit.frames import FramesFactory
from org.orekit.orbits import KeplerianOrbit
from org.orekit.utils import Constants
import json
from propagator import prop_orbit
from atm import * 

TRAINED_MODEL_PATH = Path('persistence_model.pkl')
TEST_DATA_DIR = os.path.join('/app','data', 'dataset', 'test')
TEST_PREDS_FP = Path('/app/output/prediction.json')

# Paths
initial_states_file = os.path.join(TEST_DATA_DIR, "initial_states.csv")
omni2_path = os.path.join(TEST_DATA_DIR, "omni2")

initial_states = pd.read_csv(initial_states_file)

# Load initial states
initial_states = pd.read_csv(initial_states_file, usecols=['File ID', 'Timestamp', 'Semi-major Axis (km)', 'Eccentricity', 'Inclination (deg)','RAAN (deg)', 'Argument of Perigee (deg)', 'True Anomaly (deg)'])
print(initial_states.columns)
initial_states['Timestamp'] = pd.to_datetime(initial_states['Timestamp'])

# Process each row of the initial states
model = torch.load(os.path.join(TRAINED_MODEL_PATH), pickle_module=dill)

predictions = {}

for _, row in initial_states.iterrows():
    file_id = row['File ID']
    # Load corresponding OMNI2 data
    omni2_file = os.path.join(omni2_path, f"omni2-{file_id}.csv")
    
    if not os.path.exists(omni2_file):
        print(f"OMNI2 file {omni2_file} not found! Skipping...")
        continue
    
    omni2_data = pd.read_csv(omni2_file, usecols=['Timestamp', 'f10.7_index', 'ap_index_nT'])
    omni2_data['Timestamp'] = pd.to_datetime(omni2_data['Timestamp'])
    omni2_data = omni2_data.ffill()  

    initial_state = row.drop("File ID")

    result = model(omni2_data, initial_state.to_dict())

    predictions[file_id] = {
        "Timestamp": list(map(lambda ts: ts.isoformat(), result["Timestamp"])),
        "Orbit Mean Density (kg/m^3)": result["Density (kg/m3)"].tolist()
    }
    print(f"Model execution for {file_id} Finished")



with open(TEST_PREDS_FP, "w") as outfile: 
    json.dump(predictions, outfile)

print("Saved predictions to: {}".format(TEST_PREDS_FP))
# time.sleep(360) # EVALAI BUG FIX
