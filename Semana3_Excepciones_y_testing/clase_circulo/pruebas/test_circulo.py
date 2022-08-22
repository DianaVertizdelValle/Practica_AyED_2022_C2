# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:29:38 2022

@author: je_su
"""

from modulos.circulo import Circulo, OutOfRangeError
import unittest


class TestCirculo(unittest.TestCase):
    
    def setUp(self):
        print('\nsetUp\n')
        self.c1 = Circulo(4)
        
    def tearDown(self):
        print('tearDown')
    
    def test_area(self):
        print('test_area')
        self.assertEqual(self.c1.area, 50.27)
        
    def test_perimetro(self):
        print('test_perimetro')
        #self.assertEqual(self.c1.perimetro, 25.13)
        self.assertAlmostEqual(self.c1.perimetro, 25.13, 2)
        
    def test_excepcion(self):
        print('test_excepcion')
        with self.assertRaises(OutOfRangeError):
            self.c1.radio = -4
        
        

if __name__ == '__main__':
    
    unittest.main()
