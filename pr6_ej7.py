'''
Práctica 6 ejercicio 7

Escribe un programa que pida un número (límite) y luego te pida números hasta 
que la suma de los números introducidos supere el límite inicial.
El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 25
Escribe otro valor: 7
Escribe otro valor: 14
El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56

'''

limite = int(input('Escribe el límite: '))

suma = 0
valor = int(input('Escribe un valor: '))
suma += valor
lista_valores = [valor]

while suma <= limite:
    valor = int(input('Escribe otra valor: '))
    lista_valores.append(valor)
    suma += valor

print (f'El límite a superar es {limite}. La lista creada es', end = " ")
[print(numero, end = ", ") if numero != lista_valores[-1] else print(numero, end = " ") for numero in lista_valores]
print (f'ya que la suma de estos números es: {suma}')