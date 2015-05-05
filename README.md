# overtones

A project to decompose a musical tone into its composite sine waves.

## Creators
**Michael "The Mongolian Throat Singer" Costello**
- <https://github.com/mcostello>

**William "The Swashbuckler" Lu**
- <https://github.com/williamalu>

## How to run:
**Installing Packages**

The python packages needed to run this code are PyAudio, numpy, and matplotlib.

*PyAudio*: Download the appropriate package from [PyAudio's website](https://people.csail.mit.edu/hubert/pyaudio/) and follow their instructions.

*numpy*: If you are in Ubuntu, type the following command into terminal:
```
sudo apt-get install python-numpy
```
Alternatively, you could install the entire scipy stack:
```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```
If you are not in Ubuntu, installation instructions for your OS can be found on [scipy's website] (http://www.scipy.org/install.html).

*matplotlib*: if you are in Ubuntu, type the following command into terminal:
```
sudo apt-get install python-matplotlib 
```
If you are not in Ununtu, or have problems with the download, further download instructions can be found on [matplotlib.org](http://matplotlib.org/users/installing.html).

**Running Overtones**

To use overtones, navigate to the directory that contains overtones.py and type to following command into terminal:
```
python overtones.py
```
This should start overtones and a matplotlib graph should appear with the power spectrum of the audio detected by your microphone. This graph should be updating in almost real time. If nothing appears or if the graph is obviously incorrect, your audio settings might be accessing the wrong microphone on your computer. Double-check that your default microphone is set correctly.

## Resources Consulted
[A. Levy (stackoverflow)] (http://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform)

[Frank Zalkow (stackoverflow)] (http://stackoverflow.com/questions/24974032/reading-realtime-audio-data-into-numpy-array)
