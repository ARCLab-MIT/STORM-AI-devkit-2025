# Challenge Results

The 2025 MIT ARCLab Prize for AI Innovation in Space (STORM-AI) has concluded. This page summarizes the final outcome of the competition. The complete design, methodology, and analysis &mdash; including per-storm error breakdowns and case studies &mdash; are presented in our *Space Weather* article (see the [Citation](https://2025-ai-challenge.readthedocs.io/en/latest/cite.html) page).

## Participation

The challenge drew **139 teams from 21 countries**, with most participants coming from the USA and India, followed at a lower incidence by Germany, Turkey, the UK, France, Spain, Canada, and Australia. Participants were split between academia (about 58%) and industry (about 33%), spanning AI, Aeronautics & Astronautics, data science, and Space Situational Awareness, and roughly 60% reported that this was their first AI challenge. Twenty-eight teams remained active through the end of the competition phase, together producing over 900 successful submissions on Codabench.

## Final Standings

Teams were ranked by a composite score that blends model performance with the quality of their technical report:

> **CS = 0.8 · M<sub>norm</sub> + 0.2 · Q**

where **M<sub>norm</sub>** is the normalized model-performance score (from the OD-RMSE / SSAOD-RMSE leaderboard metrics across the public and private evaluation sets) and **Q** is the technical-report score (judged on Clarity, Novelty, Technical Depth, Reproducibility, and Insights). The final top-ten standings were:

| Rank | Team | Phase 1 (M<sub>norm</sub>) | Phase 2 (Q) | Total (CS) |
|-----:|------|---------------------------:|------------:|-----------:|
| 1 | **Bimasakti**      | 1.000 | 0.624 | **0.925** |
| 2 | **Millennial-IUP** | 0.938 | 0.640 | **0.879** |
| 3 | **Cteceliker**     | 0.803 | 0.720 | **0.786** |
| 4 | SAADAT             | 0.709 | 0.807 | 0.729 |
| 5 | Mattmotoki         | 0.758 | 0.407 | 0.688 |
| 6 | Digantara          | 0.543 | 0.744 | 0.583 |
| 7 | Is_Fr              | 0.301 | 0.547 | 0.350 |
| 8 | JMU-ARIES          | 0.209 | 0.512 | 0.270 |

*Team Jaikamal reached a model score of M<sub>norm</sub> = 0.636 but did not submit a technical report, so no composite score was assigned. The strongest individual reports came from SAADAT, Digantara, and Cteceliker.*

## Winners

* 🥇 **1st &mdash; Team Bimasakti.** Their model, *BiMA*, is a bias-corrected ensemble of LightGBM regressors built on top of the empirical NRLMSIS 2.1 model. By learning the ratio and log-ratio between observed and empirical density with a direct, multi-horizon formulation (rather than a recursive one), it corrects the baseline's systematic bias while avoiding compounding error growth, achieving roughly a 44% error reduction and the most robust behavior under the storm-weighted private metric.
* 🥈 **2nd &mdash; Team Millennial-IUP.** A physics-guided CNN-LSTM-GRU hybrid over a 30-day look-back window. A lightweight propagator reconstructs the satellite's recent environment, and a dense sequence-to-sequence output predicts the full 72-hour horizon at once. This model was the most stable across regimes and the best performer during the most extreme storms.
* 🥉 **3rd &mdash; Team Cteceliker.** A compact, reproducible residual-based approach with strong local performance during the most extreme (G5) storm conditions.

A notable special case is **Team Digantara** (6th overall), whose XGBoost + TSLANet model with FFT-based frequency features and physics-guided altitude/F10.7 binning led the public leaderboard for the entire competition phase, but produced flat predictions on out-of-distribution private cases (extreme F10.7 values outside its bins), which lowered its final ranking.

## Key Takeaways

* **AI beats the empirical baselines.** Across the evaluation, data-driven models consistently outperformed both MSIS and JB2008. The top approach achieved about a **50.8% RMSE reduction versus JB2008** and a **67.7% reduction versus MSIS** overall.
* **The hardest periods are where AI helps most.** The advantage over empirical models is largest precisely where those models are weakest. Even though skill drops during extreme events &mdash; during the May 2024 "Gannon" storm the top model's improvement fell to 6.1% over JB2008 and 34.7% over MSIS &mdash; the leading models still kept a positive forecasting skill, reaching a minimum private-set score around 0.44 (an improvement of roughly 4× over MSIS even when storm periods dominated the score).
* **No single recipe wins.** The leading entries converged on distinct paradigms (an empirical-model bias correction, a recurrent environment reconstruction, and a frequency-domain model with physics-guided binning), revealing a clear trade-off between responsiveness and stability. Grounding a model in physical structure &mdash; an empirical prior, physically motivated features, or explicit storm-time handling &mdash; helped most where data were scarce.
* **Watch out for overfitting.** A marked drop in performance on the private set for part of the leaderboard pointed to overfitting on the public data. The deliberately overlapping Phase 1.1 set acted as a low-barrier warm-up and a check on memorization, while the disjoint Phase 1.2 and private sets (with SWARM-B never seen in training) confirmed that the gains were genuine generalization.

## Read More

* The complete results, figures, and per-storm analysis are in the **STORM-AI article** &mdash; see the [Citation](https://2025-ai-challenge.readthedocs.io/en/latest/cite.html) page.
* The full dataset (training, public-evaluation, and private-evaluation splits) is permanently archived on the [Harvard Dataverse](https://dataverse.harvard.edu/dataverse/stormai).
* The development kit, baseline solutions, and evaluation script remain available in the [GitHub repository](https://github.com/ARCLab-MIT/STORM-AI-devkit-2025).
