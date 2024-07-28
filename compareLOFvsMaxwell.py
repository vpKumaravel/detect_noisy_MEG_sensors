import matplotlib.pyplot as plt
import mne
from mne.preprocessing import find_bad_channels_maxwell, find_bad_channels_lof
import numpy as np

# Path to the MEG data file
file_path = 'data/subX_MEG_RAW_run1.fif'

# Load the raw MEG data
raw = mne.io.read_raw_fif(file_path, preload=True)
raw_copy = raw.copy()

# Maxwell bad channel detection
bad_channels, flat_channels, scores = find_bad_channels_maxwell(raw, return_scores=True)
print("Maxwell - Bad channels identified automatically:", bad_channels)
print("Maxwell - Flat channels identified automatically:", flat_channels)

# Pick MEG gradiometers
raw_copy = raw_copy.load_data().filter(l_freq=1, h_freq=40)
picks = mne.pick_types(raw_copy.info, meg='grad', eeg=False, eog=False)
lof_threshold = 1.4 # Hyperparameter 1
num_channels = len(picks)
n_neighbors = int(np.sqrt(num_channels)) # Hyperparameter 2
print(n_neighbors)
# Call find_bad_channels_lof to get bad channels and scores
bad_channels_lof, scores = find_bad_channels_lof(raw_copy, n_neighbors=n_neighbors, metric='euclidean',
                                                 threshold=lof_threshold, return_scores=True, picks=picks)

# Print and mark bad channels identified by LOF
raw_copy.info['bads'] = []
for pick_idx, score in enumerate(scores):
    if np.abs(score) >= lof_threshold:
        ch_name = raw_copy.info['chs'][picks[pick_idx]]['ch_name']
        print(f'LOF: Marking channel {ch_name} as bad with a LOF score of {score}')
        raw_copy.info['bads'].append(ch_name)

