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
    r, t = 0,2
    
#    while x%j != 0:
#        
#        j -= 1
#    
    if j == 40 and x%j == 0:
        return print(int(x/40), 'postes com distância de', j, 'm entre os vãos')
    else:    
        while abs(r - round(t,1)) > 1:
            l = x//j
            r = round(x/((x//j)+1),1)
            t = x - r * l
            
            j -= 1
            if r == t:
                return print(l+1, 'postes com distância de ', r, 'm entre os vãos')
            else:
                return print(l, 'postes com distância de ', r, 'm entre os vãos e 1 ponte com distância de', round(t,1),'m do penultimo poste \n erro de:',abs(r-round(t,1)))
#    elif x%j == 0:
#        return print(int(x/j), 'postes com distância de ', j, 'm entre os vãos')
#    elif x%j == 1 and j != 40:
#        return print(int((x//j)-1), 'postes com distância de ', j, 'm entre os vãos e 1 ponte com distância ', round(j+1,1),'m do penultimo poste')
    
    
    