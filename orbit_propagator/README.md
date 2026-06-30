
# STORM-AI-Propagator

We have provided a high-fidelity orbit propagator that participants can choose to use. The orbit propagator will propagate a satellite through a participants’ atmospheric model, and considers these additional perturbations: Earth’s non-spherical gravity field, solar radiation pressure, lunisolar third body accelerations, and Earth solid tides. The output of the propagator are the states of the satellite and the instantaneous density of the model at every iteration. The propagator is implemented using the [Orekit Python Wrapper](https://gitlab.orekit.org/orekit-labs/python-wrapper), and the tutorial is a Jupyter Notebook in Python.

The tutorial is a tool to help participants, but it may not be necessary for all participants. To access it, the propagator is located in the github devkit (STORM-AI-devkit-2025 → orbit_propagator → propagator_tutorial.ipynb). Open propagator_tutorial.ipynb and follow the instructions to download and set-up Orekit. The tutorial also includes instructions on how to add your own atmospheric model and toggle the propagation settings.

## Instructions to create a Miniconda virtual environment with the Orekit Python wrapper

Installation Instructions for Miniconda can be found here: https://docs.anaconda.com/miniconda/install/

1. **Create a virtual environment**:

   ```bash
   conda create -n orekit_venv_v12 python=3.8.20 anaconda
   ```

2. **Activate the virtual environment**:

   ```bash
   conda activate orekit_venv_v12
   ```

3. **Install required packages using conda**:

   - Install **Orekit** (version 12.1.2):
     ```bash
     conda install -c conda-forge orekit=12.1.2
     ```

   - Install **Pandas**:
     ```bash
     conda install -c conda-forge pandas
     ```

   - Install **NumPy**:
     ```bash
     conda install -c anaconda numpy
     ```

   - Install **Python-dateutil**:
     ```bash
     conda install -c anaconda python-dateutil
     ```

   - Install **Matplotlib**:
     ```bash
     conda install -c conda-forge matplotlib
     ```

4. **Check package version**:

   To verify the version of Orekit installed, use the following command:

   ```bash
   pip show orekit
   ```


