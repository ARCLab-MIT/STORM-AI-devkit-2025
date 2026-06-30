# STORM-AI Starter Toolkit (EvalAI — legacy)

> **⚠️ Legacy path.** The 2025 STORM-AI challenge was hosted on **Codabench**, not EvalAI. This directory is kept for reference only. For the current workflow, use the [Codabench persistence baseline](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/tree/main/baselines/Codabench) and follow the [submission tutorial](https://2025-ai-challenge.readthedocs.io/en/latest/submission.html).

## Persistence baseline
This baseline provides a boilerplate of how a submission was made to the EvalAI platform. The notebook acts as a quick-start guide and establishes a low-performance baseline for the challenge. It replicates the initial values of the NRLMSIS model across the full output horizon.

As the objective is to get the orbital mean density, it utilizes the [devkit provided propagator](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/tree/main/orbit_propagator) to propagate from the initial state the orbit the object specified. 

> **Note:** The `Dockerfile` provides an image of the environment needed to run the propagator. However, it is recommended to install it locally in a `conda` environment so you can experiment freely.

The structure is more or less the following
```
baselines
├── persistence                  
|    ├── propagator.py  # An adaptation of the propagator provided
|    ├── persistence-baseline.ipynb # Model creation and explanation
|    ├── orekit-data.zip # Used by the Orekit library
|    ├── atm.py  # Atmospheric model extracted from the notebook.
|    ├── Dockerfile # Used to build the image with the dependencies
|    └── requirements.txt # Dependency list
└── evaluation.py # Script that calculates the challenge metrics
```
Once you run the notebook and the model is trained, you can follow the following steps to build and test your Docker submission:

- Build docker image for submission: 

```bash
docker build -t storm-ai-submission .
```
- Test submission docker on a toy test dataset:

```bash
docker run -v [[TOY_TEST_DATASET_DIR]]:/dataset -v $(pwd)/submission:/submission storm-ai-submission
```
