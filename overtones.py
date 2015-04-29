import pyaudio
import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint

CHUNKSIZE = 1024 # fixed chunk size
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, 
				channels=CHANNELS, 
				rate=RATE, 
				input=True, 
				frames_per_buffer=CHUNKSIZE)

np.set_printoptions(threshold=np.nan)
frames = []
for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
	data = stream.read(CHUNKSIZE)
	# pprint(np.fromstring(data, dtype=np.int16))
	frames.append(np.divide(np.fromstring(data, dtype=np.int16), 1024.0))

# print len(frames)
# print len(frames[0])
# for i in range(len(frames)):
	# print sum(frames[i]) / len(frames[i])
numpydata = np.hstack(frames)
numpydata = np.fft.fft(numpydata)
freq = np.fft.fftfreq(numpydata.shape[-1])
print numpydata.shape[-1]

# plot data
plt.plot(freq, numpydata)
plt.show()

# close stream
stream.stop_stream()
stream.close()
p.terminate()

# import pyaudio
# import wave

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()