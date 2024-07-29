# detect_noisy_MEG_sensors
MNE-python based MEG bad sensors/channels detection

Download dataset from [here](https://osf.io/mvug7).

Run `compareLOFvsMaxwell.py`


| # | Maxwell   | Local Outlier Factor (LOF)    |
|--------|-------------|-------------|
| Filter     | Applies low pass at 40 Hz  | Requires band-pass filter  |
| Hyperparameter      | None  | a) Number of neighbors, b) LOF threshold  |
| Execution Time      | TBD | TBD  |


