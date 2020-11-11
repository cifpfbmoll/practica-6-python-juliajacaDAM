'''
Práctica 6 ejercicio 4

Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. 
El programa termina escribiendo los dos números tal y como se pide:
Escribe un número: 6
Escribe un número mayor que 6: 6
6 no es mayor que 6. Vuelve a introducir un número: 1
1 no es mayor que 6. Vuelve a introducir un número: 8
Los números que has escrito son 6 y 8

'''
print('Escrbe dos números, de manera que el segundo sea mayor que el primero')
numero_1 = int(input('Escribe el primer número: '))
numero_2 = int(input(f'Escribe un número mayor que {numero_1}: '))

while numero_2 <= numero_1:
    numero_2 = int(input (f'{numero_2} no es mayor que {numero_1}. Vuelve a introducir un número: '))

print(f'Los números que has escrito son {numero_1} y {numero_2}')