import wave
import librosa
import mir_eval
import numpy as np
import librosa
import mido

from scipy.io import wavfile
import pretty_midi
import timeit
from matplotlib import pyplot as plt

print(mir_eval.__version__)

# Open the WAV file for reading
with wave.open("vocals.wav", "rb") as wav_file:
 # Get the parameters of the WAV file
 num_channels = wav_file.getnchannels()
 sample_width = wav_file.getsampwidth()
 frame_rate = wav_file.getframerate()
 num_frames = wav_file.getnframes()
 # Read the data from the WAV file
 wav_data = wav_file.readframes(num_frames)
# Create a new WAV file for writing
with wave.open("i2polyphonic.wav", "wb") as new_wav_file:
 # Set the parameters for the new WAV file
 new_wav_file.setnchannels(num_channels)
 new_wav_file.setsampwidth(sample_width)
 new_wav_file.setframerate(frame_rate)
 # Modify the data to create polyphonic style
 new_wav_data = b""
 for i in range(0, len(wav_data), num_channels * sample_width):
     new_wav_data += wav_data[i : i + sample_width] * num_channels
 # Write the modified data to the new WAV file
 new_wav_file.writeframes(new_wav_data)
# 如果需要变成midi格式，打开下面的librosa代码
# 默认关闭了，为了效率
print('part II')
starttime = timeit.default_timer()
# Load audio file
filename = 'i2polyphonic.wav'
y, sr = librosa.load(filename)
# Get chroma features
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
# Normalize chroma features
chroma_norm = librosa.util.normalize(chroma)
# Create MIDI file
midi = mido.MidiFile()
track = mido.MidiTrack()
midi.tracks.append(track)
# Set tempo
bpm = 120
mpqn = mido.bpm2tempo(bpm)
track.append(mido.MetaMessage('set_tempo', tempo=mpqn))
# Set time signature
time_signature = (4, 4)
clocks_per_click = 24
notated_32nd_notes_per_beat = 8
track.append(mido.MetaMessage('time_signature', numerator=time_signature[0], denominator=time_signature[1],
                           clocks_per_click=clocks_per_click, notated_32nd_notes_per_beat=notated_32nd_notes_per_beat))
# Add note events
note_on_time = 0
note_off_time = 0
velocity = 64
for frame in range(chroma_norm.shape[1]):
 # Get pitch values from chroma features
 pitches = np.where(chroma_norm[:, frame] > 0.5)[0] + 24
 if len(pitches) > 0:
     # Note on
     note_on_time = int(frame * 512 / sr)  # Convert frame index to time in ticks
     for pitch in pitches:
         track.append(mido.Message('note_on', note=pitch, velocity=velocity, time=0))
     # Note off
     note_off_time = int((frame+1) * 512 / sr)  # Convert frame index to time in ticks
     for pitch in pitches:
         track.append(mido.Message('note_off', note=pitch, velocity=velocity, time=note_off_time - note_on_time))
# Save MIDI file
# midi_filename = 'i2polyphonic.mid'
midi_filename = 'i2polyphonic_test.mid'
# midi.save(midi_filename)
print("The time difference is :", timeit.default_timer() - starttime)
'''
The time difference is : 0.4281404999999978
The time difference is : 0.4072299999999984
The time difference is : 0.392059291999999
'''
from matplotlib import pyplot as plt
names = ['1 time', '2 time', '3 time']
values = [0.42, 0.40, 0.39]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Conversion speed  Compare')
plt.show()


print('Part III evalute our midi transfer way:', '--------------------')
# Load MIDI file
# source__i2polyphonic.midi is not transfer by our code , 
# it's from i2polyphonic.wav directly by standard libuary
# midi_ref = mido.MidiFile('source__i2polyphonic.midi')

# # Print MIDI messages
# for msg in midi_ref.play():
#     print(msg)



midi_est = mido.MidiFile('i2polyphonic.mid')

# Print MIDI messages
for msg in midi_est.play():
    print(msg)


# Load the MIDI and WAV files
# midi_data = pretty_midi.PrettyMIDI('i2polyphonic.mid')
# fs, wav_data = wavfile.read('i2polyphonic.wav')


# Load the MIDI and WAV files
midi_file = 'i2polyphonic.mid'
wav_file = 'i2polyphonic.wav'


import struct
import wave


def read_midi_file(file_path):
    with open(file_path, 'rb') as f:
        chunk_type = f.read(4)
        if chunk_type != b'MThd':
            raise ValueError('Invalid MIDI file')

        header_size = struct.unpack('>I', f.read(4))[0]
        file_format = struct.unpack('>H', f.read(2))[0]
        num_tracks = struct.unpack('>H', f.read(2))[0]
        time_division = struct.unpack('>H', f.read(2))[0]

        # Skip remaining header data
        f.read(header_size - 6)

        # Read track data
        tracks = []
        for i in range(num_tracks):
            track_type = f.read(4)
            if track_type != b'MTrk':
                raise ValueError('Invalid MIDI file')

            track_size = struct.unpack('>I', f.read(4))[0]
            track_data = f.read(track_size)
            tracks.append(track_data)

        return file_format, time_division, tracks


def read_wav_file(file_path):
    with wave.open(file_path, 'rb') as f:
        num_channels = f.getnchannels()
        sample_width = f.getsampwidth()
        sample_rate = f.getframerate()
        num_frames = f.getnframes()
        data = f.readframes(num_frames)

        return num_channels, sample_width, sample_rate, data


def plot_data(one, two):
    x_labels = ['MIDI rate', 'wav rate']
    y_values = [one ,two]

    plt.bar(x_labels, y_values)
    plt.title('Difference between MIDI file and WAV file')
    plt.xlabel('Data types')
    plt.ylabel('Values')
    plt.show()


# Read MIDI file
midi_format, midi_time_division, midi_tracks = read_midi_file(midi_file)
print(f'MIDI format: {midi_format}')
print(f'MIDI time division: {midi_time_division}')
print(f'MIDI tracks: {len(midi_tracks)}')

# Read WAV file
wav_num_channels, wav_sample_width, wav_sample_rate, wav_data = read_wav_file(wav_file)
print(f'WAV num channels: {wav_num_channels}')
print(f'WAV sample width: {wav_sample_width}')
print(f'WAV sample rate: {wav_sample_rate}')
print(f'WAV time division: {wav_sample_rate/1000}')
print(f'WAV data size: {len(wav_data)}')



 # Plot the difference between MIDI file and WAV file
plot_data(midi_time_division, wav_sample_rate/1000 )

