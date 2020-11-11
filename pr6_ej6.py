'''
Práctica 6 Ejercicio 6
Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios.
Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la lista de números.

Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Vuelve a probar: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 13
Escribe otro número entre 6 y 50: 4
Los números situados entre 6 y 50 que has escrito son: 45, 13

'''

print('Escrbe dos números, de manera que el segundo sea mayor que el primero')
numero_1 = int(input('Escribe un número: '))
numero_2 = int(input(f'Escribe un número mayor que {numero_1}: '))

while numero_2 <= numero_1:
    numero_2 = int(input (f'{numero_2} no es mayor que {numero_1}. Vuelve a introducir un número: '))

numeros_medios = []
numero_medio = int(input(f'Escribe un número entre: {numero_1} y {numero_2}: '))

while numero_1 < numero_medio < numero_2:
    numeros_medios.append(numero_medio)
    numero_medio = int(input(f'Escribe otro número entre {numero_1} y {numero_2}: '))

print(f'Los números situados entre {numero_1} y {numero_2} que has escrito son: ', end = ' ')
[print(numero, end = ", ") if numero != numeros_medios [-1] else print (numero, end =".") for numero in numeros_medios ]