# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 16:59:19 2018

@author: evertonferc
"""
import numpy as np
import numpy.matlib as mat
import scipy.signal as sig

'''PRELIMINARIES'''
   
'''Type III DCT matrix routine (see Eq. (5.14) on p.77 of [1])'''
def dctm(N,M):
    ''' PRONTO '''
    return (np.sqrt(2.0/M) * np.cos(mat.repmat(np.arange(0,N).reshape(N,1),1,M)*mat.repmat(np.pi*(np.arange(1,M+1)-0.5)/M,N,1))) #o vetor original é [0:N-1], mas em python o intervalo final é aberto, ex: a[0:10], vai extrair os itens do 0 a 9 
#cria uma matriz N por M com valores da equação
'''Cepstral lifter routine (see Eq. (5.12) on p.75 of [1])'''
def ceplifter(N, L):
    ''' PRONTO '''
    return (1 + 0.5 * L * np.sin(np.pi*(np.arange(0, N))/L )) #mesmo caso anterior

def mfcc(speech, fs, Tw, Ts, alpha, R, M, N, L):
    '''PRELIMINARIES'''
    Nw = round(Tw*fs) #frame duration (samples), Tw(s) is given and fs is extracted of .wav file
    Ns = round(Ts*fs) #frame shift (samples), Ts(s) is given and fs is extracted of .wav file
    
    nfft = int(2**(np.ceil(np.log2(abs(Nw))))) #length of FFT analysis 
    K = int(nfft/2+1)  #length of the unique part of the FFT 
    
    
    ''' FEATURE EXTRACTION '''
    ''' Preemphasis filtering (see Eq. (5.1) on p.73 of [1])'''
    speech = sig.lfilter([1, -alpha], 1, speech)
    #ALPHA is the preemphasis coefficient e vai ser dado na função principal
    ''' Framing and windowing (frames as columns)'''
    if (len(speech)-Nw)%Ns != 0:
        rest = (len(speech)-Nw)%Ns
        speech = np.append(speech, np.zeros(Ns-rest))
    print(M)
    print(K)
    print(R)
    print(fs)
    H = trifbank(M, K, R, fs)
    DCT = dctm(N,M)
    
    window = 0.54-0.46*np.cos(2*np.pi*np.arange(Nw)/(Nw-1))
    
    index = np.arange(0, len(speech)-Nw+1, Ns)#um vetor de 0 ao ultimo frame mais
    # um numero, para que quando o i pegar o ultimo elemento, que pegue o final do speech

    idx_phoneme = 0
    begin_ph = matrix_ph[idx_phoneme, 0]
    end_ph   = matrix_ph[idx_phoneme, 1]
    ph       = matrix_ph[idx_phoneme, 2]
    ph_filename = algo(ph)
    
    for i in index:
        # Extracting a window from speech
        subspeech = (speech[i:i+Nw])
        subspeech = subspeech * window
        subspeech = np.append(subspeech, np.zeros(nfft - len(subspeech)))
        MAG = abs(np.fft.fft(subspeech, nfft))
        FBE = H.dot(MAG[0:K])
        CC = DCT.dot(np.log(FBE)) #conferir se nao é multiplicação matricial
        lifter = ceplifter( N, L )
        CC = np.diag(lifter).dot(CC)
    
        if begin_ph >= i and i > end_ph    :
            append(cc, ph_filename)
        else:
            idx_phoneme =+ 1
            begin_ph = matrix_ph[idx_phoneme, 0]
            end_ph   = matrix_ph[idx_phoneme, 1]
            ph       = matrix_ph[idx_phoneme, 2]
            ph_filename = algo(ph) #colocar o .txt e o diretorio para ele ser reconhecivel
            append(cc, ph_filename)
            
    return CC, FBE
    
    
    