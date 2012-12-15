"""
chords.py
Chord estimator from MP3 file
Last updated: 9 December 2012
"""
from __future__ import division 

import sys
sys.path.append('..')

from pymir import AudioFile
from pymir.audio import chordestimator
from pymir import Onsets

import matplotlib.pyplot as plt

# Load the audio
print "Loading Audio"
audiofile = AudioFile.open("../audio_files/test-stereo.mp3")
#audiofile = AudioFile.open("/Users/jsawruk/mir-samples/foo-fighters/01-The-Pretender.mp3")

plt.plot(audiofile)
plt.show()

#audiofile = audiofile[:100000]

print "Finding onsets using Spectral Flux (spectral domain)"
o = Onsets.onsetsByFlux(audiofile)
print o

print "Extracting Frames"
frames = audiofile.framesFromOnsets(o)
#for i in range(0, len(frames)):
#	print "Frame " + str(i)
#	plt.plot(frames[i])
#	plt.show()

#frameSize = 16384
#frames = audioFile.frames(frameSize)

print "Start | End  | Chord"
print "--------------------"

frameIndex = 0
startIndex = 0
for frame in frames:
    spectrum = frame.spectrum()
    chroma = spectrum.chroma()
    chord = chordestimator.getChord(chroma)

    endIndex = startIndex + len(frame)

    startTime = startIndex / frame.sampleRate
    endTime = endIndex / frame.sampleRate

    print "%.2f  | %.2f | %s" % (startTime, endTime, chord)
    
    frameIndex = frameIndex + 1
    startIndex = startIndex + len(frame)