

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

def nistread():
    for path in all_files('C:/Users/evert/Desktop/Testando/Alguns dados para teste/TRAIN/DR1/FCJF0', '*.wav'):
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

def phonemeread():
    
    for path in all_files('C:/Users/evert/Desktop/Testando/Alguns dados para teste/TRAIN/DR1/FCJF0', '*.PHN'):
        with open(path, 'r') as text:
           content = text.readlines()
        content = [line.strip() for line in content]
        text.close()
        
        spliting = [col.split() for col in content]
        
        x = [[linha[i][:] for linha in spliting] for i in range(len(spliting[0]))]
        i, f, ph = int(x[1])    
        
        
        #x = [spliting[i] for i in spliting]
        
        
        return x
    
    
    
    
    
    
    
    
    
    
    
    
    
    