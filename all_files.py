# -*- coding: utf-8 -*-
import os, fnmatch
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

###para salvar numa variavel o nome de todos os arquivos lidos:
#thefiles = list(all_files('/tmp', '*.py;*.htm;*.html'))
            
###para imprimir todos os dados dos arquivos lidos:
#for path in all_files('/tmp', '*.py;*.htm;*.html'):
#   print path

#no caso para ler os arquivos wav, usar o programa nistread.py no
#lugar do print path