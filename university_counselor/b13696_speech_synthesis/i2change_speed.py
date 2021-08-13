# import wave

# CHANNELS = 1
# swidth = 2
# Change_RATE = 0.8

# spf = wave.open('output0.wav', 'rb')
# RATE=spf.getframerate()
# signal = spf.readframes(-1)

# wf = wave.open('changed0.wav', 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(swidth)
# wf.setframerate(RATE*Change_RATE)
# wf.writeframes(signal)
# wf.close()


# import wave
# import sys
# from pydub import AudioSegment

# import soundfile as sf
# import pyrubberband as pyrb
# #sound = AudioSegment.from_file("deviprasadgharpehai.mp3")
# # sound = AudioSegment.from_mp3(sys.argv[1])
# # sound.export("output0.wav", format="wav")

# # print(sys.argv[1])


# y, sr = sf.read("output0.wav")
# # Play back at extra low speed
# y_stretch = pyrb.time_stretch(y, sr, 0.5)
# # Play back extra low tones
# y_shift = pyrb.pitch_shift(y, sr, 0.5)
# sf.write("change0.wav", y_stretch, sr, format='wav')

import ffmpy
import glob
files = glob.glob("*.wav")
for item in files:
	print(item)
	ff = ffmpy.FFmpeg(inputs={item: None}, outputs={"output/"+'90percent'+item: ["-filter:a", "atempo=0.9"]})
	ff.run()








