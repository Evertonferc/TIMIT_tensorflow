

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
        vazio = []
        
        t = [(int(lines[0]), int(lines[1]), lines[2]) for lines in spliting]
        #vazio.append([begin, end, phoneme])
        
        #x = [[line[i][:] for line in spliting] for i in range(len(spliting[0]))]
        
        
        #col1 = [int(b) for b in range(len(spliting)) for spliting[b]]
    
       # begin, end = [int(b) for b in x[0]], [int(e) for e in x[1]]
        #phoneme = x[2]
        
       # test = [(a,b,c) for a in begin for b in end for c in phoneme if begin.index(a) == end.index(b) and phoneme.index(c)]
        #test = [(a,b,c) for i in range(len(begin)) for a in begin[i] for b in end[i] for c in phoneme[i]]
        
        
        #x = [[line[i][:] for line in spliting] for i in range(len(spliting[0]))]
        #test = dict(((x,[y,z]) for x in phoneme for (y,z) in (begin,end))
        #test1 = [dict(x,[y,z]) for x in phoneme for y in begin for z in end if x.index() == y.index() and z.index()]
        
        
       
        
    #for lines in t:
    #a = int(lines[1])
    #b = int(lines[0])
    #p = lines[2]
    #vazio.append([b, a, p])
    
        #begin, end, phoneme = [(int(lines[0]), for lines in spliting], [int(lines[1]) for lines in spliting]
    
    return t
    
    
    
    
    
    
    
    
    
    
    
    