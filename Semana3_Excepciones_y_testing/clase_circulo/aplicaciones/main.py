# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:32:05 2022

@author: je_su
"""

from modulos.circulo import Circulo

def main():
    
    c1 = Circulo(5)
    print(c1.radio)
    print("área del círculo:", c1.area)
    print("perímetro del círculo:", c1.perimetro)
    
    
if __name__ == "__main__":
    
    main()