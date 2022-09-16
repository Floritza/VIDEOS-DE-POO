"""
Módulo:
Es un archivo con extensión .py o .pyc (Python compilado), que posee su propio espacio de nombres
y que puede contener variables, funciones, clases o incluso otros módulos.
¿Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor.
Modularización y reutilización.
"""

# import funciones_matematicas
from modulos.funciones_matematicas import multiplicar, sumar
print(sumar(5, 6))
print(multiplicar(5, 6))