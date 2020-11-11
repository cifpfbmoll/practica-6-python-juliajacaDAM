'''
Práctica 6 Ejercicio 8

Escribe un programa que te pida primero un número y luego te pida números
hasta que la suma de los números introducidos coincida con el número inicial.
El programa termina escribiendo la lista de números.

Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 45
45 es demasiado grande. Escribe otro valor: 1
Escribe otro valor: 39
El límite a alcanzar es 50. La lista creada es: 10, 1, 39

'''

limite = int(input('Escribe el límite: '))

suma = 0
valor = int(input('Escribe un valor: '))

while valor > limite:
    print(f'{valor} es demasiado grande')
    valor = int(input('Escribe otro valor: '))


lista_valores = [valor]
suma += valor

while suma < limite:
    valor = int(input('Escribe otro valor: '))
    suma += valor

    if suma > limite:
        print(f'{valor} es demasiado grande')
        suma -= valor
    
    elif suma < limite:
        lista_valores.append(valor)

    else:
        lista_valores.append(valor)
        print(f'El límite a alcanzar es {limite}. La lista creada es: ', end = " ")
        [print(numero, end = " ") for numero in lista_valores]


if valor == limite:
        print('Has llegado al límite con el primer valor')
