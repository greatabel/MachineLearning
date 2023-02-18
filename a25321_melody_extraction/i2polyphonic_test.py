import wave

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
with wave.open("polyphonic.wav", "wb") as new_wav_file:
    # Set the parameters for the new WAV file
    new_wav_file.setnchannels(num_channels)
    new_wav_file.setsampwidth(sample_width)
    new_wav_file.setframerate(frame_rate)

    # Modify the data to create polyphonic style
    new_wav_data = b''
    for i in range(0, len(wav_data), num_channels * sample_width):
        new_wav_data += wav_data[i:i+sample_width] * num_channels

    # Write the modified data to the new WAV file
    new_wav_file.writeframes(new_wav_data)
