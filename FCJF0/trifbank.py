# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:30:23 2018

@author: evertonferc
"""
import numpy as np

'''HANDY INLINE FUNCTION HANDLES'''

'''Forward and backward mel frequency warping (see Eq. (5.13) on p.76 of [1]) 
Note that base 10 is used in [1], while base e is used here and in HTK code'''

def hz2mel(hz): # Hertz to mel warping function
    ''' PRONTO '''
    return (1127*np.log(1+hz/700))

def mel2hz(mel): # mel to Hertz warping function
    ''' PRONTO '''
    return (700*np.exp(mel/1127)-700)


def trifbank( M, K, R, fs):
    f_min = 0 #filter coefficients start at this frequency (Hz)
    f_low = R[0]       # lower cutoff frequency (Hz) for the filterbank 
    f_high = R[1]      # upper cutoff frequency (Hz) for the filterbank 
    f_max = 0.5*fs     # filter coefficients end at this frequency (Hz)
    f = np.linspace( f_min, f_max, num= K ) # frequency range (Hz), size 1xK
#    fw = hz2mel( f )
    
    '''filter cutoff frequencies (Hz) for all filters, size 1x(M+2)'''
    
    c = mel2hz(hz2mel(f_low)+np.arange(0,M+2)*((hz2mel(f_high) - hz2mel(f_low))/(M+1)) )
    cw = hz2mel(c)
    
    H = np.zeros( [M, K]) 
    
    for m in range(M):
       k = np.nonzero((f >= c[m]) == (f <= c[m+1]))
       H[m,k] = (f[k]-c[m])/(c[m+1]-c[m])
       k = np.nonzero((f >= c[m+1]) == (f <= c[m+2]))
       H[m,k] = (c[m+2]-f[k])/(c[m+2]-c[m+1])
       
    return H
