import pyaudio
import numpy as np
from matplotlib import pyplot as plt
import time

def read_audio(RECORD_SECONDS, RATE):
    """
    Reads audio from microphone and stores input in a list
    Output: frames (list)
    """

    # sets standard parameters for what normally would go into a WAV file
    # seconds to record and record rate are already set by user
    CHUNKSIZE = 1024 # fixed chunk size
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    # initialize portaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, 
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True, 
                    frames_per_buffer=CHUNKSIZE)

    frames = []

    # read audio from microphone, turn it into a string, store it in a list of frames
    for i in range(0, int(RATE / CHUNKSIZE * RECORD_SECONDS)):
        data = stream.read(CHUNKSIZE)
        frames.append(np.divide(np.fromstring(data, dtype=np.int16), 1024.0))

    # close stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return frames

def spectrum_plot():
    """
    Uses read_audio to take in microphone input, runs fft, generates power vs. frequency graphs
    in real time.
    """
    
    # initialize matplotlib graphs, ion allows for interactive graphing
    plt.ion()
    plt.show()

    RECORD_SECONDS = 0.03
    RATE = 44100
    
    for i in range(1000):
        
        # clear plot, set axis limits
        plt.clf()
        plt.ylim((0, 10000))
        plt.xlim((0, 5000))
        
        numpydata = np.hstack(read_audio(RECORD_SECONDS, RATE))

        n = numpydata.size

        spectrum = np.fft.fft(numpydata)
        freq = np.fft.fftfreq(n, 1./RATE)

        # plots data
        # x axis is frequency (hz)
        # y axis is power
        plt.plot(freq, np.absolute(spectrum))
        plt.draw()
        i += 1
        # time.sleep(0.05)
    
    plt.close()

if __name__ == "__main__":
    spectrum_plot()