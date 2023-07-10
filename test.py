import unittest
from metodo_biseccion import biseccion
from newton_raphson import newton_raphson
from integracion_numerica import sum_rieman, metodo_trapecio
import math

class TestMetodosNumericos(unittest.TestCase):
    
    def test_biseccion(self):
        def f(x):
            return math.sin(x) - math.exp(-x)
        
        resultado = biseccion(f, 0, 1, 2*10**-2, 7)
        
        self.assertAlmostEqual(resultado, 0.5859375, delta=2*10**-2)
    
    def test_newton_raphson(self):
        def f(x):
            return math.sin(x) - math.exp(-x)

        resultado = newton_raphson(f, 0.5, 2*10**-2, 7)
        
        self.assertAlmostEqual(resultado, 0.5884347152526223, delta=2*10**-2)

    def test_sum_rieman(self):
        def f(x):
            return x * math.cos(x**2) 
        
        resultado = sum_rieman(f, 0, 1, 1000)

        self.assertAlmostEqual(resultado, 0.4204651626977245, delta= 1)

    def test_metodo_trapecio(self):
        def f(x):
            return math.sqrt(x + 1)
        
        resultado = metodo_trapecio(f, -1, 1, 5)

        self.assertAlmostEqual(resultado, 1.8377382733191294, delta= 1)

if __name__ == '__main__':
    unittest.main()
    