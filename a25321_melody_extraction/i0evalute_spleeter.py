import librosa
import mir_eval

import numpy as np


# Load the original audio file
audio_file = 'audio_example.mp3'
y_orig, sr_orig = librosa.load(audio_file)

# Load the separated audio files
vocal_file = 'output/audio_example/vocals.wav'
y_vocal, sr_vocal = librosa.load(vocal_file)
accompaniment_file = 'output/audio_example/accompaniment.wav'
y_accompaniment, sr_accompaniment = librosa.load(accompaniment_file)

# Resample the audio files if necessary
if sr_vocal != sr_orig:
    y_vocal = librosa.resample(y_vocal, sr_vocal, sr_orig)
if sr_accompaniment != sr_orig:
    y_accompaniment = librosa.resample(y_accompaniment, sr_accompaniment, sr_orig)

# Transpose the estimated sources and combine them
estimated_sources = np.vstack((y_vocal, y_accompaniment))

# Combine the reference sources
reference_sources = np.array([y_orig, y_orig])

# Evaluate the performance using metrics such as SNR, SIR, and SAR
snr = mir_eval.separation.bss_eval_sources(reference_sources, estimated_sources)[0]
sir = mir_eval.separation.bss_eval_sources(reference_sources, estimated_sources)[1]
sar = np.mean(librosa.feature.spectral_contrast(y_vocal)[:, np.newaxis]) / np.mean(librosa.feature.spectral_contrast(y_accompaniment)[:, np.newaxis])

print('We choose use metrics such as signal-to-noise ratio (SNR), \
source-to-interference ratio (SIR), \
and source-to-artifact ratio (SAR) to evaluate the performance of the model.')
x = snr
x= list(map(lambda x :str(x) + '%',x.round(2)))
print('SNR: ')
print(f'{x}')
# print(f"SNR: {snr:.2f} dB")

x = sir
x= list(map(lambda x :str(x) + '%',x.round(2)))
print('SIR:')
print(f'{x}')
# print(f"SIR: {sir:.2f} dB")

# print(sar, type(sar), '#'*20)
# x = sar
# x= list(map(lambda x :str(x) + '%',x.round(2)))
# print(f'{x}')
print(f"SAR: {sar:.2f}")