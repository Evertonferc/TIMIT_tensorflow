# function [signal, fs, bits, begins, version] = nistread(filename)
# Read a NIST file (it does not treat multi-channel files yet).
# It is based on TIMIT files avaliable in CD-ROM, which are 16 bits,
# monoaural audio files.

#Inputs:
#-------
#filename:    name of the files

#Outputs:
#--------
#signal   vector/matrix containing the signal read from filename
#fs       its sampling rate
#bits     its bits/sample (always 32)
#begins   the delay of first samples of signal
#version  version of nist file

#import wave
#import scipy.io.wavfile

#def nistread(SA):
#    fid = open(filename, "r")
#    print fid
#    return
#import scipy.io.wavfile
#rate, data = scipy.io.wavfile.read('SA1.wav')
#print (fid[1:16])
#print(type(fid[1:16]))
import numpy as np
import struct
import matplotlib.pyplot as plt
mylist = []
n = 23398
#with open('SA1.wav', "rb") as f:
#    for i in range (0, n):
#        a = np.array('f')
#        x = np.fromfile(a)
#print(x)

with open("SA1.wav", "rb") as f:
    for i in range (0, n):
        s = struct.unpack('=i', f.read(4))
        mylist.append(s[0])
        dados_lidos = mylist[512:]



print(dados_lidos)
#plt.plot(dados_lidos)
#plt.show()
#print(s)



#with open('SA1.wav', "rb") as f:
#    for i in range (0, n):
#        s = struct.unpack('=i', f.read(4))
#        mylist.append(s[0])

#print(mylist)
#import scikits
#from scikits.audiolab import Sndfile, play
#f = Sndfile('SX127', 'r')
#data = f.read_frames(f.nframes)
#play(data) # Just to test the read data


#import wave, struct

#waveFile = wave.open('SA1.wav', 'r')

#length = waveFile.getnframes()
#for i in range(0,length):
#    waveData = waveFile.readframes(1)
#    data = struct.unpack("<h", waveData)
#    print(int(data[0]))


#x = open("SA1.wav", "r")
    # Read the whole file at once
    #data = binary_file.read()
    #print(data)

    # Seek position and read N bytes
#x.seek(0)  # Go to beginning
#couple_bytes = x.read()
#print(couple_bytes)



# Create an int from bytes. Default is unsigned.
#some_bytes = couple_bytes
#i = int.from_bytes(some_bytes, byteorder='big')
#print(i)

#import wave
#x = wave.openfp('SA1.wav','rb')
#print(x)
