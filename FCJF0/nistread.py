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


import numpy as np
import struct
import array
import matplotlib.pyplot as plt
mylist = []
n = 23398
#with open('SA1.wav', "rb") as f:
#    for i in range (0, n):
#        a = np.array('f')
#        x = np.fromfile(a)
#print(x)

with open("SA1.wav", "rb") as wave:
    for i in range (0, n):
        s = struct.unpack('=h', wave.read(2))
        data = list(s)
        mylist.append(data[0])
    dados_lidos = mylist[512:]
wave.close()

with open('SA1.wav', 'rb') as wave:
    bytes_lidos = wave.read()
wave.close()

# extracao e tratamento de header
header_lido = bytes_lidos[0:1023]
#lembrar de por um if 
# converte bytes em amostras de acordo com informacao do header
dados_lidos = array.array('h', bytes_lidos[1024:])


print(dados_lidos)
print(type(s))
print(type(data))
print(type(mylist))
print(type(dados_lidos))
plt.plot(dados_lidos)
plt.show()
#print(s)



