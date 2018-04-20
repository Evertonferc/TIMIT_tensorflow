

import os, fnmatch
import array
import re
import numpy as np
import matplotlib.pyplot as plt

###Função que navega entre os diretórios###

def all_files(root, patterns='*', single_level=False, yield_folders=False):
    # Expand patterns from semicolon-separated string to list
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort( )
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield os.path.join(path, name)
                    break
        if single_level:
            break

###função que abre os arquivos .wav, extrai as informações do header e le NIST em binário###

def nistread(path):
    '''
    Read a NIST file (it does not treat multi-channel files yet). 
    It is based on TIMIT files avaliable in CD-ROM, which are 16 bits,
    monoaural audio files.
    
    Parameter
    ---------
    path : str 
        The full path of the directory that contain the files
    

    Returns
    --------
    signal : numpy.ndarray
        Contain the bits of the signal on .wav file
    fs : float
        Its sampling rate    
    bits : float
        Its bits/sample (16 or 8)
    version : float
        Version of nist file
    
    '''
    
    
    with open(path, 'rb') as wave:
        bytes_read = wave.read()
    wave.close()

    # extraction and treatment of header
    header = str(bytes_read[0:1023])

    fs = float((re.search('(?<=sample_rate -i )\w+', header)).group(0))
    bits = float((re.search('(?<=sample_sig_bits -i )\w+', header)).group(0))
    version = float((re.search('(?<=database_version -s3 )\w+', header)).group(0))


    if bits==16:
        signal = np.array(array.array('h', bytes_read[1024:]))
        return signal, fs, bits, version


    elif bits==8:
        signal = np.array(array.array('b', bytes_read[1024:]))
        return signal, fs, bits, version
    else:
        print('this file is not in 16 bits nor 8 bits')

###função que abre os arquivos .phn

def phonemeread(path):
    '''
    Read a PHN file; convert the begin and the end of respective phoneme in string
    and organize in tuples.
    
    Parameters
    ---------
    path : str 
        The full path of the directory that contain the files
    

    Returns
    --------
    phoneme : list of tuples
        Contain tuples with 3 elements: int, int and str
    
    phoneme[0] = begin
    phoneme[1] = end
    phoneme[2] = phoneme
    
    '''
    
    with open(path, 'r') as text:
       content = text.readlines()
    text.close()
        
    spliting = [line.split() for line in content]
    
    phoneme = [(int(lines[0]), int(lines[1]), lines[2]) for lines in spliting]

    return phoneme

### FORMAS DE USAR A FUNÇÃO PHONEMEREAD():
    
#x = phonemeread()
#[a for a in x if a[coluna]==item da coluna(podendo ser numero de inicio, fim, ou o fonema)]
#a[0]= inicio, a[1]= fim, a[2]= fonema
#lembrar que os numeros são int e os fonemas são str (entao precisa do '')
    
#retorna uma lista com uma tupla com inicio, fim e o fonema

#('C:/Users/evert/Desktop/Testando/Alguns dados para teste/TRAIN/DR1/FDML0', '*.wav')

def processing(dirpath):
    ###Recebe um caminho de diretório e le o nome de todos os arquivos .wav
    ##muda a extensão da str .wav para .phn. Com as strings .wav ele alimenta
    ###a função nistread, e com as strings .phn, ele alimenta a função phonemeread
    ###faz um teste para saber quantos arquivos leu
    
    cont = 0 
    for path in all_files(dirpath, '*.WAV'):
        name_files = os.path.splitext(path)[0]
        phonemestr = name_files + '.PHN'
        a, b = nistread(path), phonemeread(phonemestr)
        
        cont += 1
    return nistread(path), phonemeread(phonemestr)





    
    
    
    
    
    
    
    
    
    
    
    