# Baseline Solutions

## NRLMSIS-Persistence Baseline 

This baseline is a very naive approach to the problem. Its main purpose is to guide participants through the different steps of preparing and testing a model, helping them understand the workflow required to make their own submissions.

In time series problems, the **persistence baseline** is often used to assess model performance. This approach simply takes the last observed value of the input and propagates it through the output, replicating the initial value as predictions for all future steps. It can be described as follows:


 ![](_img/PersistenceForm.png)

<br>

For example, for yt = 5:

 ![](_img/PersistenceExample.png)

<br>
Although this approach may seem overly simplistic, it is surprisingly effective in certain cases, to the point that beating it can be challenging. This is because, in time series prediction tasks, the closer the future time steps are to the present, the more similar their values tend to be due to local temporal dependencies. As a result, when there are no significant outliers, this method can deliver reasonably good performance.

In this particular case, as we need to propagate and do not know the values to propagate from the beginning, we will combine it with the NRLMSIS model to obtain predictions for the initial date along the propagated orbit at each time step. To achieve this, we will use the [`pymsis`](https://swxtrec.github.io/pymsis/) library. We will then propagate our results using the [custom propagator](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/tree/main/orbit_propagator), which is provided as part of the development tools and makes use of the [`Orekit`](https://www.orekit.org/) library. 

<!-- Baseline Solutions Section -->
<div align="center" style="margin-bottom: 20px;">
    <!-- Centered Button with Emoji -->
    <div style="display: inline-flex; align-items: center; background-color: #4d4d4d; color: #ffffff; border-radius: 5px; padding: 5px 15px; font-family: Arial, sans-serif; font-size: 14px; text-align: center; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);">
        <span style="margin-right: 8px; font-size: 18px;">👩🏾‍💻</span>
        <a href="https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/tree/main/baselines/persistence" target="_blank" style="color: #ffffff; text-decoration: none;">
            Go to baseline
        </a>
    </div>
</div>

<!-- Quote Block -->
<div style="display: flex; flex-direction: column; background-color: #f9f9f9; border-left: 6px solid #4aa8ec; border-radius: 4px; padding: 15px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); font-family: Arial, sans-serif;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff; background-color: #4aa8ec; display: inline-block; padding: 5px 10px; border-radius: 3px; margin-bottom: 10px;">ℹ️ Note</div>
    <p style="font-size: 14px; margin: 0; color: #555;">This persistence baseline is provided as a minimal reference solution to illustrate the full submission workflow. The approaches that ultimately performed best in the competition are described on the <a href="https://2025-ai-challenge.readthedocs.io/en/latest/results.html">Results</a> page and in the article.</p>
</div>

## Baseline Model Orbit Propagator

Since many participants do not have a background in space or astrodynamics, we have provided a high-fidelity orbit propagator that participants may use if they decide to take an approach that relies on propagating a spacecraft’s initial orbit. This tool can propagate a satellite through a custom atmospheric model, and considers these additional perturbations: Earth’s non-spherical gravity field, solar radiation pressure, lunisolar third body accelerations, and Earth solid tides. The propagator’s outputs are composed of the satellite’s orbital state vector and the instantaneous density of the model at every iteration. The propagator is implemented using the Orekit Python Wrapper, and the tutorial is a Jupyter Notebook in Python.

You can access the propagator and its accompanying tutorial in our GitHub devkit [here](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/tree/main/orbit_propagator). To use it, simply open `propagator_tutorial.ipynb` and follow the instructions to download and set-up Orekit. The tutorial also includes instructions on how to add your own atmospheric model and toggle the propagation settings. These resources are intended to help any participants who are not experienced with orbit propagation and would like to incorporate a propagator into their model. Competitors are more than welcome to use alternative propagation tools or to submit models that do not rely on orbit propagation at all. 

