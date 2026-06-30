# Dataset Information

<!-- Announcement Quote Block -->
<div style="display: flex; flex-direction: column; background-color: #e7f3fe; border-left: 6px solid #2196f3; border-radius: 4px; padding: 15px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); font-family: Arial, sans-serif; color: #333;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff; background-color: #1565c0; display: inline-block; padding: 5px 10px; border-radius: 3px; margin-bottom: 10px;">📢 Dataset release</div>
    <p style="font-size: 14px; margin: 0; line-height: 1.5;">
        The competition has concluded and the <strong>complete STORM-AI dataset</strong> &mdash; training, public-evaluation, and private-evaluation splits &mdash; is now permanently archived and openly available on the <a href="https://dataverse.harvard.edu/dataverse/stormai">Harvard Dataverse</a>. The Dropbox links below were used during the live competition and may be retired; the Dataverse archive is the canonical source.
    </p>
</div>

## Overview

The Satellite Tracking and Orbit Resilience Modeling with AI (STORM-AI) dataset combines multi-phenomenology observations &mdash; solar, geomagnetic, and orbital &mdash; into a single basis for data-driven thermospheric density forecasting. All of it is derived from publicly available products distributed by organizations not affiliated with the challenge, including ESA, NASA Goddard Space Flight Center, NOAA, and the Space-Track catalog. The dataset spans roughly 25 years and seven satellites across six missions (SWARM A/B/C, CHAMP, GRACE, and GRACE-FO), deliberately covering both quiet and highly active geomagnetic periods (for example the 2003 Halloween storms, the 2015 St. Patrick's Day storm, the 2018&ndash;2020 deep solar minimum between cycles 24 and 25, and the very active year 2024).

The data is organized into three splits:

* **Training set (8,118 samples)** &mdash; used to develop models. It includes five of the six missions (SWARM A and C, CHAMP, GRACE, and GRACE-FO); **SWARM-B is held out entirely and never appears in training**, providing a fully independent evaluation source.
* **Public evaluation set** &mdash; not shared directly with participants; it was accessed only through the scoring server to drive the live leaderboard while limiting overfitting.
* **Private evaluation set (4,557 evaluation samples in total)** &mdash; focused on periods of strong solar and geomagnetic activity and used for the final ranking.

### What is a "sample"?

Throughout the dataset, a **sample** is a single forecasting instance for one satellite, identified by a unique `File ID`. Each sample bundles three elements:

1. **Initial state** &mdash; the satellite's orbital elements and geodetic position at the reference epoch `t0`.
2. **60 days of context** &mdash; the OMNI2 and GOES space-weather history immediately preceding `t0`.
3. **Target** &mdash; the orbit-averaged thermospheric density over the following 3 days (72 h) at a 10-minute cadence (432 values), together with the corresponding MSIS baseline forecast.

All sample counts reported here (such as the 8,118 training samples) refer to forecasting instances defined in this way.

## STORM-AI Data Formats

### Public Training Dataset

The public training dataset is the portion participants used to train and develop their models. It is permanently archived on the <a href="https://dataverse.harvard.edu/dataverse/stormai">Harvard Dataverse</a> (the competition-era Dropbox mirror is <a href="https://www.dropbox.com/scl/fo/ilxkfy9yla0z2ea97tfqv/AB9lngJ2yHvf9t5h2oQXaDc?rlkey=iju8q5b1kxol78kbt0b9tcfz3&st=j7f0mcc3&dl=0">still available here</a>) and includes the following files and folders:
* <b>Initial state files</b>: contain samples of a satellite's initial orbital elements, geodetic (ITRF) positional coordinates, and a 5-digit file ID for each I/O pair in the provided training data. Each file name has the format `[first file ID]_to_[last file ID]-initial_states.csv`.
* <b>OMNI2 data folder</b>: Space weather information collected by NASA Space Flight Goddard Center and provided in 60-day segments (one 60-day OMNI2 history file per initial state). Each file name has the format `omni2-[file ID]-[first day]_to_[last day].csv`, where the dates are displayed as `YYYYmmDD`.
* <b>GOES data folder</b>: X-Ray flux information collected by NOAA'S GOES satellites and provided in 60-day segments (one 60-day GOES history file per initial state). Each file name has the format `goes-[file ID]-[first day]_to_[last day].csv`, where the dates are displayed as `YYYYmmDD`. To maximize availability, measurements from multiple GOES satellites were merged, with higher-numbered satellites taking precedence in cases of overlap, so a single file may contain rows from different GOES spacecraft.
* <b>Thermospheric density data folder</b>: Time series orbit average density values collected by ESA satellites and provided in 3-day segments (one 3-day "forecasted" density file per initial state). Each file name has the format `[spacecraft]-[file ID]-[first day]_to_[last day].csv`, where the spacecraft is indicated by a 6-character designation and dates are displayed as `YYYYmmDD`.

Your objective is to design a model that, given a spacecraft's initial state and 60 days of space weather information directly preceding that state, can predict the next 3 days of atmospheric density values the spacecraft will observe.

That is, your model should take in these inputs: 
* A satellite's initial location, provided in both geodetic coordinates and orbital elements
* Space weather information for the 60 day period preceding the timestamp of the initial satellite location
* X-Ray flux information for the 60 day period preceding the timestamp of the initial satellite location

Your model should then predict the sequence of orbit-averaged atmospheric density values that the spacecraft will observe in the future. This prediction must span a period of 3 days directly following the timestamp of the initial satellite location.  

Some recommendations: 
* We recommend reviewing the data column header descriptions in the [Definitions](https://2025-ai-challenge.readthedocs.io/en/latest/dataset.html#definitions) section for more details on the contents of the challenge dataset. This includes exploring the column headers and data type descriptions. 
* Be mindful of dataset units and representations!
* You may access additional GOES, OMNI2, CHAMP, GRACE, and SWARM data through NOAA, NASA, and ESA online if you wish to supplement the provided warm-up data while training your algorithms.

### Instructions for Dataset Download

Dropbox may not support direct downloading of the entire Phase 1 dataset at once. Instead, open the Phase 1 dataset folder, where you’ll find several subfolders—such as omni2, goes, and density—available for individual download. Note that the goes folder is larger and contains multiple subfolders, each of which can also be downloaded separately.


### Warmup Dataset 

The <a href="https://www.dropbox.com/scl/fo/nz1j92xpr6eet3fa5mx5i/ADMYs2zfr3dvxJ-FFd5dmM8?rlkey=tem27v1d2raf2nnlcq6cd49ev&st=sty6ggo3&dl=0)">warm-up dataset</a> was released to participants on November 15, 2024. 

Participants should use this subset of the STORM-AI data to become familiar with the phenomenology and formats they will be asked to use during Phase 1 of the competition. The warmup dataset consists of the following files and folders: 
* <b>wu001_to_wu715-initial_states.csv</b>: 715 sets of orbital elements and geodetic position coordinates for ESA's SWARM A satellite
* <b>OMNI2</b>: Space weather information collected by NASA Space Flight Goddard Center and provided in 60-day segments (one 60-day OMNI2 history file per initial SWARM A state)
* <b>GOES</b>: X-Ray flux information collected by NOAA'S GOES-13 satellite and provided in 60-day segments (one 60-day GOES history file per initial SWARM A state)
* <b>Sat_Density</b>: Time series orbit average density values collected by ESA'S SWARM A satellite and provided in 3-day segments (one 3-day "forecasted" density file per initial SWARM A state)

### Evaluation Dataset Composition

The evaluation data was served only through the scoring server and split into a public part (driving the live leaderboard) and a private part (used for the final ranking, weighted toward strong solar/geomagnetic activity). The public part was further divided into Phase 1.1 (a low-barrier warm-up that overlaps in time with the training period but uses shifted initial states) and Phase 1.2 (built entirely from samples never seen in training). The table below shows how the 4,557 evaluation samples are distributed across missions and phases; note that **SWARM-B appears only in evaluation**, never in training.

| Satellite  | Phase 1.1 | Phase 1.2 | Private Eval. | Total |
|------------|----------:|----------:|--------------:|------:|
| CHAMP      | 1129 | 0   | 10  | 1139 |
| GRACE-1    | 29   | 0   | 0   | 29   |
| GRACE-2    | 949  | 0   | 10  | 959  |
| SWARM-A    | 0    | 0   | 102 | 102  |
| SWARM-B    | 0    | 844 | 122 | 966  |
| SWARM-C    | 0    | 483 | 109 | 592  |
| GRACE-FO 1 | 640  | 0   | 130 | 770  |
| **Totals** | **2747** | **1327** | **483** | **4557** |

### Definitions

#### Spacecraft Initial State Data
| Column Header  | Description | 
| ------------- | ------------- | 
| File ID  | 5 character designator assigned to the OMNI2, GOES, & Sat_Density files associated with the initial satellite state |
| Timestamp  | Start of the study period  |
| Semi-major Axis (km) | Satellite semi-major axis. Defines the size of the orbit. Represented in km | 
| Eccentricity | Satellite eccentricity. Describes the shape of the orbit and how stretched it is. Ranges from 0 (perfectly circular) to 1 (parabolic); values greater than 1 indicate a hyperbolic orbit. | 
| Inclination (deg) | Satellite inclination. The tilt of the orbit relative to the equatorial plane of the central body; the angle between the orbital plane and the equatorial plane. An inclination of 0° indicates an orbit in the equatorial plane, while 90° represents a polar orbit (crossing over the poles). Units in degrees. |
| RAAN (deg) | Satellite right ascension of the ascending node. Defines horizontal orientation of the orbit; tilt of the orbit relative to the equatorial plane. Units in degrees. |
| Argument of Perigee (deg) | Satellite argument of periapsis. Specifies the orientation of the orbit within its plane; defines where the orbit’s closest approach occurs within the plane of the orbit. Units in degrees. |
| True Anomaly (deg) | Satellite true anomaly. Position of the body along the orbit at a specific time. Units in degrees. |
| Latitude (deg) | Satellite geodetic latitude at the start of the study period. Units in degrees.   | 
| Longitude (deg) | Satellite geodetic longitude at the start of the study period. Units in degrees. |
| Altitude (km) | Satellite altitude at the start of the study period. Units in km for this dataset.  | 

#### OMNI2 Space Weather Data
| Column Header              | Description                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| Timestamp                  | Datetime-like timestamp of observation.                                                               |
| YEAR                       | Year of observation.                                                                                 |
| DOY                        | Day of Year (Julian day) of observation. Ranges 01 to 365.                                           |
| Hour                       | Hour of observation, typically in UTC. Ranges 00 to 23.                                              |
| Bartels_rotation_number    | Number of 27-day solar rotations that have occurred since February 8, 1832.                        |
| ID_for_IMF_spacecraft      | Identifier for spacecraft measuring IMF (Interplanetary Magnetic Field).                  |
| ID_for_SW_Plasma_spacecraft| Identifier for spacecraft measuring Solar Wind Plasma.                                   |
| num_points_IMF_averages    | Number of data points used to calculate IMF averages.                                   |
| num_points_Plasma_averages | Number of data points used to calculate Plasma averages.                               |
| Scalar_B_nT                | Scalar (magnitude) of the magnetic field. Units in nT.                                               |
| Vector_B_Magnitude_nT      | Vector magnitude of the magnetic field. Units in nT.                                                 |
| Lat_Angle_of_B_GSE         | Latitude angle of magnetic field in GSE coordinates. Units in Degrees.                               |
| Long_Angle_of_B_GSE        | Longitude angle of magnetic field in GSE coordinates. Units in Degrees.                              |
| BX_nT_GSE_GSM              | X-component of magnetic field in GSE and GSM coordinates. Units in nT.                               |
| BY_nT_GSE                  | Y-component of magnetic field in GSE coordinates. Units in nT.                                       |
| BZ_nT_GSE                  | Z-component of magnetic field in GSE coordinates. Units in nT.                                       |
| BY_nT_GSM                  | Y-component of magnetic field in GSM coordinates. Units in nT.                                       |
| BZ_nT_GSM                  | Z-component of magnetic field in GSM coordinates. Units in nT.                                       |
| RMS_magnitude_nT           | RMS of magnetic field magnitude. Units in nT.                                                        |
| RMS_field_vector_nT        | RMS of the magnetic field vector. Units in nT.                                                       |
| RMS_BX_GSE_nT              | RMS of BX component in GSE. Units in nT.                                                             |
| RMS_BY_GSE_nT              | RMS of BY component in GSE. Units in nT.                                                             |
| RMS_BZ_GSE_nT              | RMS of BZ component in GSE. Units in nT.                                                             |
| SW_Plasma_Temperature_K    | Solar wind plasma temperature. Units in K.                                                           |
| SW_Proton_Density_N_cm3    | Solar wind proton density. Units in particles/cm³.                                                   |
| SW_Plasma_Speed_km_s       | Solar wind plasma speed. Units in km/s.                                                              |
| SW_Plasma_flow_long_angle  | Longitude angle of solar wind plasma flow. Units in Degrees.                                         |
| SW_Plasma_flow_lat_angle   | Latitude angle of solar wind plasma flow. Units in Degrees.                                          |
| Alpha_Prot_ratio           | Ratio of alpha particles to protons in the solar wind. Units in -.                                   |
| sigma_T_K                  | Standard deviation of solar wind temperature. Units in K.                                            |
| sigma_n_N_cm3              | Standard deviation of proton density. Units in particles/cm³.                                        |
| sigma_V_km_s               | Standard deviation of solar wind speed. Units in km/s.                                               |
| sigma_phi_V_degrees        | Standard deviation of plasma flow longitude angle. Units in Degrees.                                 |
| sigma_theta_V_degrees      | Standard deviation of plasma flow latitude angle. Units in Degrees.                                  |
| sigma_ratio                | Standard deviation ratio. Units in -.                                                                |
| Flow_pressure              | Solar wind flow pressure. Units in nPa.                                                              |
| E_electric_field           | Electric field strength. Units in mV/m.                                                              |
| Plasma_Beta                | Ratio of plasma pressure to magnetic pressure. Units in -.                                           |
| Alfen_mach_number          | Alfvén Mach Number, indicating ratio of solar wind speed to Alfvén speed. Units in -.                |
| Magnetosonic_Mach_number   | Magnetosonic Mach Number, indicating ratio of solar wind speed to magnetosonic speed. Units in -.    |
| Quasy_Invariant            | Quasi-invariant parameter in plasma physics. Units in -.                                             |
| Kp_index                   | Planetary K-index, measuring geomagnetic activity. Units in -.                                       |
| R_Sunspot_No               | Sunspot number, indicating solar activity level. Units in -.                                         |
| Dst_index_nT               | Disturbance Storm Time index. Units in nT.                                                           |
| ap_index_nT                | Ap index, daily averaged planetary geomagnetic index. Units in nT.                                   |
| f10.7_index                | F10.7 Solar radio flux. Units in 10⁻²² W/m²/Hz.                                                      |
| AE_index_nT                | Auroral Electrojet Index, measuring auroral activity strength. Units in nT.                          |
| AL_index_nT                | Auroral Lower Index, measuring lower limit of auroral activity. Units in nT.                         |
| AU_index_nT                | Auroral Upper Index, measuring upper limit of auroral activity. Units in nT.                         |
| pc_index                   | Polar Cap Index, measuring geomagnetic activity in polar regions. Units in -.                        |
| Lyman_alpha                | Lyman-alpha solar flux. Units in W/m².                                                               |
| Proton_flux_>1_Mev         | Proton flux for energies >1 MeV. Units in particles/cm²/s/sr.                                        |
| Proton_flux_>2_Mev         | Proton flux for energies >2 MeV. Units in particles/cm²/s/sr.                                        |
| Proton_flux_>4_Mev         | Proton flux for energies >4 MeV. Units in particles/cm²/s/sr.                                        |
| Proton_flux_>10_Mev        | Proton flux for energies >10 MeV. Units in particles/cm²/s/sr.                                       |
| Proton_flux_>30_Mev        | Proton flux for energies >30 MeV. Units in particles/cm²/s/sr.                                       |
| Proton_flux_>60_Mev        | Proton flux for energies >60 MeV. Units in particles/cm²/s/sr.                                       |
| Flux_FLAG                  | Flag indicating quality of proton flux measurements. Units in -.                                     |
| Date                       | Date of observation. Units in YYYY-MM-DD.                                                            |

#### GOES-EAST (GOES-8, 12, 13, 16) X-Ray Flux Data
For additional information on the GOES datasets, we recommend checking out <a href="https://www.dropbox.com/scl/fo/ilxkfy9yla0z2ea97tfqv/AB9lngJ2yHvf9t5h2oQXaDc?rlkey=iju8q5b1kxol78kbt0b9tcfz3&st=j7f0mcc3&dl=0">the NOAA Satellite Information System</a>.

There is a specific bit arrangement for <b>xrsa_flag</b> and <b>xrsb_flag</b> values-- you can find more info on <a href="https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/discussions/6">this discussion forum post</a>. Overall, it would be most helpful for you to just think of any data entries with 0.0 flag values as ‘good’ data. Any other value in the flag columns can be considered ‘bad’ or ‘compromised’ data.


| Column Header              | Description                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| time                       | Timestamp of the measurement.                                                                     |
| quad_diode                 | Measurement from the quad diode sensor.                                                          |
| xrsa_flux                  | Flux measured in the XRS-A sensor, represents solar soft X-ray emissions.                        |
| xrsa_flux_observed         | Observed flux in the XRS-A sensor, including all raw measurement data without corrections.        |
| xrsa_flux_electrons        | Estimated contribution of electron flux in the XRS-A sensor measurements.                        |
| xrsb_flux                  | Flux measured in the XRS-B sensor, represents solar hard X-ray emissions.                        |
| xrsb_flux_observed         | Observed flux in the XRS-B sensor, including all raw measurement data without corrections.        |
| xrsb_flux_electrons        | Estimated contribution of electron flux in the XRS-B sensor measurements.                        |
| xrsa_flag                  | Quality flag for XRS-A data.                                                                      |
| xrsb_flag                  | Quality flag for XRS-B data.                                                                      |
| xrsa_num                   | Number of valid data points in the XRS-A dataset during the study period.                         |
| xrsb_num                   | Number of valid data points in the XRS-B dataset during the study period.                         |
| xrsa_flag_excluded         | Indicates whether specific XRS-A data points are excluded based on quality checks. Binary flag.   |
| xrsb_flag_excluded         | Indicates whether specific XRS-B data points are excluded based on quality checks. Binary flag.   |
| au_factor                  | Calibration factor for converting flux values into physical units.                                |
| corrected_current_xrsb2    | Corrected current values for the XRS-B2 sensor.                                                   |
| roll_angle                 | Roll angle of the spacecraft during the measurement.                                              |
| xrsa1_flux                 | Flux measured in XRS-A1 sensor, represents solar soft X-ray emissions.                           |
| xrsa1_flux_observed        | Observed flux in XRS-A1 sensor, including all raw measurement data without corrections.           |
| xrsa1_flux_electrons       | Estimated contribution of electron flux in the XRS-A1 sensor measurements.                       |
| xrsa2_flux                 | Flux measured in XRS-A2 sensor, represents solar soft X-ray emissions.                           |
| xrsa2_flux_observed        | Observed flux in XRS-A2 sensor, including all raw measurement data without corrections.           |
| xrsa2_flux_electrons       | Estimated contribution of electron flux in the XRS-A2 sensor measurements.                       |
| xrsb1_flux                 | Flux measured in XRS-B1 sensor, represents solar hard X-ray emissions.                           |
| xrsb1_flux_observed        | Observed flux in XRS-B1 sensor, including all raw measurement data without corrections.           |
| xrsb1_flux_electrons       | Estimated contribution of electron flux in the XRS-B1 sensor measurements.                       |
| xrsb2_flux                 | Flux measured in XRS-B2 sensor, represents solar hard X-ray emissions.                           |
| xrsb2_flux_observed        | Observed flux in XRS-B2 sensor, including all raw measurement data without corrections.           |
| xrsb2_flux_electrons       | Estimated contribution of electron flux in the XRS-B2 sensor measurements.                       |
| xrs_primary_chan           | Primary X-ray sensor channel used for the measurement.                                           |
| xrsa1_flag                 | Quality flag for XRS-A1 data.                                                                     |
| xrsa2_flag                 | Quality flag for XRS-A2 data.                                                                     |
| xrsb1_flag                 | Quality flag for XRS-B1 data.                                                                     |
| xrsb2_flag                 | Quality flag for XRS-B2 data.                                                                     |
| xrsa1_num                  | Number of valid data points in the XRS-A1 dataset during the study period.                        |
| xrsa2_num                  | Number of valid data points in the XRS-A2 dataset during the study period.                        |
| xrsb1_num                  | Number of valid data points in the XRS-B1 dataset during the study period.                        |
| xrsb2_num                  | Number of valid data points in the XRS-B2 dataset during the study period.                        |
| xrsa1_flag_excluded        | Indicates whether specific XRS-A1 data points are excluded based on quality checks. Binary flag.  |
| xrsa2_flag_excluded        | Indicates whether specific XRS-A2 data points are excluded based on quality checks. Binary flag.  |
| xrsb1_flag_excluded        | Indicates whether specific XRS-B1 data points are excluded based on quality checks. Binary flag.  |
| xrsb2_flag_excluded        | Indicates whether specific XRS-B2 data points are excluded based on quality checks. Binary flag.  |
| yaw_flip_flag              | Indicates whether a yaw flip occurred during the measurement.                                     |


<!-- | Column Header            | Description                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------|
| Timestamp                 | Timestamp of the measurement.    
| xrsa_flux                | Flux measured in the XRS-A sensor, represents solar soft X-ray emissions. |
| xrsa_flux_observed       | Observed flux in the XRS-A sensor, including all raw measurement data without corrections.         |
| xrsa_flux_electrons      | Estimated contribution of electron flux in the XRS-A sensor measurements.       |
| xrsb_flux                | Flux measured in the XRS-B sensor, represents solar hard X-ray emissions. |
| xrsb_flux_observed       | Observed flux in the XRS-B sensor, including all raw measurement data without corrections.         |
| xrsb_flux_electrons      | Estimated contribution of electron flux in the XRS-B sensor measurements.      |
| xrsa_flag                | Quality flag for XRS-A data.                                                                       |
| xrsb_flag                | Quality flag for XRS-B data.                                                                       |
| xrsa_num                 | Number of valid data points in the XRS-A dataset during the study period.                          |
| xrsb_num                 | Number of valid data points in the XRS-B dataset during the study period.                          |
| xrsa_flag_excluded       | Indicates whether specific XRS-A data points are excluded based on quality checks. Binary flag.    |
| xrsb_flag_excluded       | Indicates whether specific XRS-B data points are excluded based on quality checks. Binary flag.    | -->

#### Spacecraft Atmospheric Density Data
| Column Header  | Description | 
| ------------- | ------------- | 
| Timestamp  | Datetime-like timestamp of observation. |
| Orbit Mean Density (kg/m^3) | Orbit-average of density derived from GPS accelerations. Helps assess long-term drag effects; used to decide if drift control maneuvers are needed due to accumulated orbital decay. Units in kg/m^3. | 

### Release History

| Version  | Release Date    | Description                                                                                           |
|--------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| V1.0     | 2024-11-15      | OMNI2 and SWARM A data shared in 3 files (OMNI2, SWARM A POD, SWARM A DNS) for 2014-2019              |
| V1.1     | 2024-11-20      | Added GOES East inputs for 2014-2019                                                                  |
| V2.0     | 2024-12-11      | Reorganized OMNI2, GOES & SWARM data into multiple files (1 of each type per initial satellite state) |
| V3.0     | 2024-12-17      | Added samples 0-5570 to Phase 1 dataset without GOES inputs                                           |
| V3.1     | 2024-12-20      | Added samples 5571-8118 and remaining GOES inputs to Phase 1 dataset                                  |
| V3.2     | 2025-01-22      | Added initial state time codes for samples 6672-8118 and fixed OEs in warmup dataset                  |
| V3.3     | 2025-03-04      | Added missing GOES data from 2007-2013                                                                |
| V3.4     | 2025-04-07      | Increased GOES data density for the 2007-2013 files updated in V3.3. See more details <a href="https://github.com/ARCLab-MIT/STORM-AI-devkit-2025/discussions/25#discussioncomment-12780485">here<a/>.           |
| Full release | 2026        | Complete dataset (training, public-evaluation, and private-evaluation splits, all missions) permanently archived on the <a href="https://dataverse.harvard.edu/dataverse/stormai">Harvard Dataverse</a> alongside the *Space Weather* article.           |

## Guidelines

Participants should note that algorithm inputs must be limited to the phenomenology and data formats present in the public training dataset, but utilizing additional phenomenology or data sources for model validation and development is allowed and encouraged. 

Also note that since these datasets are collected from real spacecraft, there may be short gaps in the data due to blackout periods and instrument error. Participants should take this into account when designing their algorithms to ensure successful submissions.

