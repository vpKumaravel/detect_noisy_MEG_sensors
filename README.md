# detect_noisy_MEG_sensors
MNE-python based MEG bad sensors/channels detection

## Prerequisites

- Python 3.x
- MNE-Python 1.7
- NumPy 1.x

## Dataset
Download dataset from [here](https://osf.io/mvug7).

For the run1, the following is the ground truth (manually annotated by authors). For other runs, please refer to the excel file inside the `data` folder.

<img width="86" alt="image" src="https://github.com/user-attachments/assets/2cbc81fc-7696-43ff-b1b5-b8fca3df6c25">


## Code
Run `compareLOFvsMaxwell.py`

## Source Code

**MNE-Python:** The LOF Python file can be found [here](https://mne.tools/stable/generated/mne.preprocessing.find_bad_channels_lof.html#mne.preprocessing.find_bad_channels_lof).  
**Python-MEEGKIT:** LOF can be used in this Python package for M/EEG processing. Source code: [here](https://github.com/nbara/python-meegkit/blob/master/meegkit/lof.py).  
**EEGLAB:** The EEGLAB plugin can be found [here](https://github.com/vpKumaravel/detectbadchannelLOF).

## Background

The LOF algorithm is originally designed to detect bad sensors in Neonatal EEG data as a part of NEAR pipeline ([paper](https://www.sciencedirect.com/science/article/pii/S1878929322000123)). Later, I tried evaluating the algorithm on a public adult EEG dataset. A comparative evaluation revealed a better bad channel detection using LOF (paper can be found [here](https://www.mdpi.com/1424-8220/22/19/7314)).

For MEG datasets, there is no systematic validation conducted. I hope this repository using a sample open source dataset demonstrates the feasibility.

## Console Output

**Maxwell Method**
```
Static bad channels:  ['MEG2241']
Static flat channels: []
[done]
Elapsed time: 162.29768228530884 seconds
Maxwell - Bad channels identified automatically: ['MEG2241']
Maxwell - Flat channels identified automatically: []
```

**Local Outlier Factor (LOF) Method**
```
LOF: Detected bad channel(s): ['MEG0223', 'MEG2432', 'MEG2443', 'MEG2513']
Elapsed time: 7.4986419677734375 seconds
LOF: Marking channel MEG0223 as bad with a LOF score of -1.4420097344785427
LOF: Marking channel MEG2432 as bad with a LOF score of -1.4533940514459451
LOF: Marking channel MEG2443 as bad with a LOF score of -1.5501051894957765
```

## Maxwell vs LOF

| #   | Maxwell                                | Local Outlier Factor (LOF)                               |
|-----|----------------------------------------|-----------------------------------------------------------|
| **Filter**                              | Applies a low pass filter at 40 Hz                        | Requires band-pass filter (commonly between 1-40 Hz)    |
| **Hyperparameters**                     | None                                                   | a) Number of neighbors<br>b) LOF threshold                |
| **Execution Time**                      | 162.29768228530884 s                                                  | 7.4986419677734375 s                       |
| **Methodology**                         | Utilizes predefined signal processing techniques and statistical modeling to identify noisy sensors. | Anomaly detection based on local density deviation. Requires parameter tuning and preprocessing. |
| **Sensitivity to Noise**                | Designed to handle typical noise and artifacts in MEG data. | Designed to identify sensors that consistently captured motion or jump artifacts. |
| **Flexibility**                         | Less flexible, reliant on specific filter settings.       | More flexible, allowing for adjustments based on data characteristics (by legitimately tuning the hyperparameters) |
| **Interpretability**                    | Results are typically straightforward based on filtering and statistical analysis. | Channels that are free of contamination typically have an LOF score close to 1.0. Scores above 1.2 suggest increasing likelihood of contamination, with the probability of contamination rising as the LOF score increases.  |

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## References

```
@Article{LOF2022,
AUTHOR = {Kumaravel, Velu Prabhakar and Buiatti, Marco and Parise, Eugenio and Farella, Elisabetta},
TITLE = {Adaptable and Robust EEG Bad Channel Detection Using Local Outlier Factor (LOF)},
JOURNAL = {Sensors},
VOLUME = {22},
YEAR = {2022},
NUMBER = {19},
ARTICLE-NUMBER = {7314},
URL = {https://www.mdpi.com/1424-8220/22/19/7314},
DOI = {10.3390/s22197314}
}

@article{NEAR2022,
  title={NEAR: An artifact removal pipeline for human newborn EEG data},
  author={V.P. Kumaravel, E.Farella, E.Parise, and M.Buiatti},
  journal={Developmental Cognitive Neuroscience (Special Issue: EEG Methods for Developmental Cognitive Neuroscientists: A Tutorial Approach)},
  doi={https://doi.org/10.1016/j.dcn.2022.101068},
  year={2022}
}
```
## Contact

For questions or comments, please contact via [email](mailto:vpr.kumaravel@gmail.com).

