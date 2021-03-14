"""
Generating Binary Beats with python.

"""

from struct import pack
from math import sin, pi
import wave
import random
from os.path import abspath

# create a bytestring containing "short" (2-byte) sine values
SAMPLE_RATE = 44100
waveData = b''
maxVol = 2**15-1.0
frequencyHz = 90.50
fileLengthSeconds = 10
for i in range(0, SAMPLE_RATE * fileLengthSeconds):
    pcmValue = sin(i*frequencyHz/SAMPLE_RATE * pi * 2)
    pcmValue = int(maxVol*pcmValue)
    waveData += pack('h', pcmValue)

# save the bytestring as a wave file
outputFileName = 'output.wav'
wv = wave.open(outputFileName, 'w')
wv.setparams((1, 2, SAMPLE_RATE, 0, 'NONE', 'not compressed'))
wv.writeframes(waveData)
wv.close()
print(f"saved {abspath(outputFileName)}")
