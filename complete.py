

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
        text.close()
        
        spliting = [line.split() for line in content]

        
        t = [(int(lines[0]), int(lines[1]), lines[2]) for lines in spliting]

    
    return t

### FORMAS DE USAR A FUNÇÃO PHONEMEREAD():
    
#x = phonemeread()
#[a for a in x if a[coluna]==item da coluna(podendo ser numero de inicio, fim, ou o fonema)]
#a[0]= inicio, a[1]= fim, a[2]= fonema
#lembrar que os numeros são int e os fonemas são str (entao precisa do '')
    
#retorna uma lista com uma tupla com inicio, fim e o fonema









    
    
    
    
    
    
    
    
    
    
    
    