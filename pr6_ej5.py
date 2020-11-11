'''
Práctica 6 Ejercicio 5

Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista.
Para acabar de escribir los números, escribe un número que no sea mayor que el anterior.

El programa termina escribiendo la lista de números:
Escribe un número: 6
Escribe un número mayor que 6: 10
Escribe un número mayor que 10: 12
Escribe un número mayor que 12: 25
Escribe un número mayor que 25: 9

Los números que has escrito son: 6, 10, 12, 25  (Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista, haced esto así a partir de ahora)
'''

numeros = [-999999999999]
numero = int(input('Escribe un número: '))

while numero > numeros[-1]:
    numeros.append(numero)
    numero = int(input(f'Escribe un número mayor que {numeros[-1]}: '))
    
print('Los números que has escrito son: ', end= "")
[print(numero, end = ", ") if numero != numeros [-1] else print (numero, end =".") for numero in numeros[1:] ] 