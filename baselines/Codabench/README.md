# STORM-AI Starter Toolkit (Codabench)
## Persistence baseline
This baseline provides a boilerplate of how a submission should be made to the Codabench platform. This notebook acts as a quick start guide and establishes a low-performance baseline for the challenge. It consists in the replication of the initial values of the NRLMSIS model through all the output size.

As the objective is to get the orbital mean density, it utilizes the [devkit provided propagator](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/tree/main/orbit_propagator) to propagate from the initial state the orbit the object specified. 

> **Note:** For your own models you should create your own conda or micromamba enviroments using the commands `conda create <env>` and `conda activate <env>`, and there install all your dependencies.

The structure of this baseline is:
```
persistence
├── submission                  
|    ├── propagator.py  # An adaptation of the propagator provided
|    ├── orekit-data.zip # Used by the Orekit library
|    ├── persistence_model.pkl # Trained model
|    ├── submission.py # Execution entrypoint and controller
|    ├── atm.py  # Atmospheric model extrated from the notebook.
|    └── environment.yml # Depency list
└── dev
    └── persistence-baseline.ipynb # Model creation and explanation

```
Once you run the notebook and the model is trained, you can follow the following steps to build and test your submission:

- Create you micromamba enviroment from the `environment.yml` you created from your enviroment:

```bash
yes | micromamba env create --name sub_env --file /app/ingested_program/environment.yml
```
- Test submission docker on a toy test dataset:

```bash
micromamba run --name sub_env python submission.py
```

Once everything is working you should compress this files as a `.zip` file and submit it to Codabench, following the [tutorial](https://2025-ai-challenge.readthedocs.io/en/latest/submission.html).
