'''
Práctica 6. Ejercicio 1
Escribe un programa que te pida palabras y las guarde en una lista.
Para terminar de introducir palabras, simplemente pulsa Enter. 
l programa termina escribiendo la lista de palabras.
Escribe una palabra: viaje
Escribe más palabras: aventura
Escribe más palabras: cómic
Escribe más palabras:
Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']
'''

palabras = []
palabra = input('Escribe una palabra: ')

while palabra != "" "":
    palabras.append(palabra)
    palabra = input('Escribe más palabra: ')


print('las palabras que has escrito son', palabras)

