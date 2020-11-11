'''
Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
Valor mínimo: 0
Valor máximo: 100
Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
Es 50 ?: mayor
Es 75 ?: menor
Es 62 ?: menor
Es 56 ?: mayor
Es 59 ?: igual

Gracias por jugar!!
Mejoras (opcionales):
    • que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
    • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.

'''

import random

minimo = int (input ( "Valor mínimo: "))
maximo = int (input ( "Valor máximo: "))

ordenador = random.randint (minimo, maximo) #A random integer in range [start, end] including the end points.
print(f'Tu numero es {ordenador}')

usuario = input('¿He adivinado el número?')

while usuario != 'igual':
    if usuario == 'mayor':
        minimo = ordenador +1

    elif usuario == 'menor':
        maximo = ordenador -1

    ordenador = random.randint (minimo, maximo) #A random integer in range [start, end] including the end points.
    print(f'Tu numero es {ordenador}')
    usuario = input('¿He adivinado el número?')

print('¡Gracias por jugar!')