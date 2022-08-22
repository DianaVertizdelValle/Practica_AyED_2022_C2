# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:32:05 2022

@author: je_su
"""

from modulos.circulo import Circulo, OutOfRangeError

def main():
    
    try:
        c1 = Circulo(-5)
        
    except OutOfRangeError as msg:
        print(msg)
    else:
        print(c1.radio) 
        print(c1.perimetro)
    
    
if __name__ == "__main__":
    
    main()