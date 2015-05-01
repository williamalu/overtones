import pyaudio
import numpy as np
from matplotlib import pyplot as plt

CHUNKSIZE = 1024 # fixed chunk size
RATE = 44100
RECORD_SECONDS = 5


# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)

for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
	# do this as long as you want fresh samples
	data = stream.read(CHUNKSIZE)
	numpydata = np.fromstring(data, dtype=np.int16)

# plot data
plt.plot(numpydata)
plt.show()

# close stream
stream.stop_stream()
stream.close()
p.terminate()