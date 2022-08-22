# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:38:25 2022

@author: je_su
"""

# lista = [1,2,3]
# print(lista[4])
# print('Empieza mi programa')


# try:
#     arch = open('./datos/mi_archivo.txt')
#     dict_1 = {'key1':'valor1', 'key2':'valor2'}
#     print(dict_1['key1'])

# except FileNotFoundError:
#     arch = open('./datos/mi_archivo.txt', mode='w')
#     arch.write('Agrego una linea al archivo')

# except KeyError as msg: 
#     print(f"la clave {msg} del diccionario no existe")
    
# else:
#     contenido = arch.read()
#     print(contenido)

# finally:
#     arch.close()


# print('Termina mi programa')


def calcular_imc(altura:float, peso:int):
    
    if altura <= 0 or altura >= 2.5:
        raise KeyError("ingrese una altura razonable")
    
    imc = peso/(altura**2)
    return imc


if __name__ == '__main__':
     
    calculado = False
    while not calculado:    
        try:
            altura = float(input('ingrese su altura: '))
            peso = int(input('ingrese su peso: '))
            imc = calcular_imc(altura, peso)
            
        except KeyError as msg:
            print(msg)
        except ValueError:
            print("ingrese valores numéricos")    
        else:
            print("su imc es:", imc)
            calculado = True











