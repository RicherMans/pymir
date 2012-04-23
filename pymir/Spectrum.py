# Spectrum class
# ndarray subclass for spectral data

import math

import numpy
from numpy import *

from numpy import fft,array,arange,zeros,dot,transpose
from math import sqrt,cos,pi

class Spectrum(numpy.ndarray):
    
    def __new__(subtype, shape, dtype=float, buffer=None, offset=0,
          strides=None, order=None):
        # Create the ndarray instance of our type, given the usual
        # ndarray input arguments.  This will call the standard
        # ndarray constructor, but return an object of our type.
        # It also triggers a call to InfoArray.__array_finalize__
        obj = numpy.ndarray.__new__(subtype, shape, dtype, buffer, offset, strides,
                         order)
        
        obj.sampleRate = 0
        
        # Finally, we must return the newly created object:
        return obj
    
    def __array_finalize__(self, obj):
        # ``self`` is a new object resulting from
        # ndarray.__new__(InfoArray, ...), therefore it only has
        # attributes that the ndarray.__new__ constructor gave it -
        # i.e. those of a standard ndarray.
        #
        # We could have got to the ndarray.__new__ call in 3 ways:
        # From an explicit constructor - e.g. InfoArray():
        #    obj is None
        #    (we're in the middle of the InfoArray.__new__
        #    constructor, and self.info will be set when we return to
        #    InfoArray.__new__)
        if obj is None: return
        # From view casting - e.g arr.view(InfoArray):
        #    obj is arr
        #    (type(obj) can be InfoArray)
        # From new-from-template - e.g infoarr[:3]
        #    type(obj) is InfoArray
        #
        # Note that it is here, rather than in the __new__ method,
        # that we set the default value for 'info', because this
        # method sees all creation of default objects - with the
        # InfoArray.__new__ constructor, but also with
        # arr.view(InfoArray).
        
        self.sampleRate = getattr(obj, 'sampleRate', None)
        
        # We do not need to return anything
        
    #####################
    # Spectrum methods
    #####################
    
    # Bandwidth
    
    # Centroid
    
    # Cepstrum?
    
    # Chroma
    def chroma(self):
        chroma = [0] * 12
        for index in range(0, len(self)):
            
            # Assign a frequency value to each bin
            f = index * (self.sampleRate / 2.0) / len(self)
            
            # Convert frequency to pitch to pitch class
            if f != 0:
                pitch = int(round(69 + 12 * math.log(f / 440.0, 2)))
            else:
                pitch = 0
            pitchClass = pitch % 12
            
            chroma[pitchClass] = chroma[pitchClass] + abs(self[index])
        
        # Normalize the chroma vector
        maxElement = max(chroma)
        chroma = [c / maxElement for c in chroma]
        
        return chroma
    
    # Crest
    
    # Flatness
    
    # Flux
    
    # Kurtosis
    
    # Inverse DCT (IDCT)
    def idct(self):
        N = len(self)
        x = array(zeros(N))
        a = sqrt(2 / float(N))
        for n in range(N):
            for k in range(N):
                if k == 0:
                    x[n] += sqrt(1 / float(N)) * self[k] * cos(pi * (2*n + 1) * k / float(2 * N))
                else:
                    x[n] += a * self[k] * cos(pi * (2*n + 1) * k / float(2 * N))
        return x
    
    # Inverse FFT
    
    # MFCCs?
    
    # Rolloff
    
    # Skewness
    
    # Spread
    
    # Tilt
    