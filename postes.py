# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:50:53 2018

@author: evertonferc
"""
def postes(n):
    #x = int(input('Entre com a distancia (em mm): '))
    x = n
#    i = 39
#    
#    if x%40 == 0:
#        #print ('Distância entre postes igual a 40m')
#        return print(int(x/40), 'postes com distância de 40m entre os vãos') 
#    elif x%i == 0 or x%i == 1:
        
    j = 40
    while x%j != 0 and x%j < 1:
        
        j -= 1
    
    if j == 40 and x%j == 0:
        return print(int(x/40), 'postes com distância de', j, 'm entre os vãos')
    elif j == 40:
        l = x//40
        r = round(x/(l+1),1)
        t = x - r * l
        return print(l, 'postes com distância de ', r, 'm entre os vãos e 1 ponte com distância ', round(t,1),'m do penultimo poste')
    elif x%j == 0:
        return print(int(x/j), 'postes com distância de ', j, 'm entre os vãos')
    elif x%j == 1 and j != 40:
        return print(int((x//j)-1), 'postes com distância de ', j, 'm entre os vãos e 1 ponte com distância ', round(j+1,1),'m do penultimo poste')
    