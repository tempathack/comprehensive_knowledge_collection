# sktime Algorithms - Overview

sktime provides a unified, sklearn-style API for time-series tasks. It organizes algorithms by scitype (what an estimator does) and by data type (series/panel/hierarchical).

## Data scitypes
- **Series**: one time series (univariate or multivariate), optionally with exogenous inputs.
- **Panel**: a collection of series (aligned or unequal length).
- **Hierarchical**: multiple aggregation levels (store -> region -> country).

## Estimator scitypes
- **Forecaster**, **Classifier**, **Regressor**, **Clusterer**
- **AnomalyDetector / SeriesAnnotator**
- **Transformer** for feature extraction, denoising, scaling, and imputation

## Algorithm families (examples)
- Classical statistical: Naive, ARIMA/SARIMA, ETS, Theta
- Feature-based: ROCKET, TSFresh, catch22
- Distance-based: kNN + DTW/EDR
- Interval-based: Time Series Forest (TSF)
- Dictionary-based: BOSS, WEASEL
- Shapelet-based, Deep learning, Probabilistic/ensemble

## Classification family deep dives
- Distance-based: `data_science/time_series/sktime_algorithms/classification/distance_based/00_overview`
- Interval-based: `data_science/time_series/sktime_algorithms/classification/interval_based/00_overview`
- Dictionary-based: `data_science/time_series/sktime_algorithms/classification/dictionary_based/00_overview`
- Shapelet-based: `data_science/time_series/sktime_algorithms/classification/shapelet_based/00_overview`

## Full catalog
See `data_science/time_series/sktime_algorithms/registry/00_overview` for a dynamic list of all estimators from your local sktime install.
