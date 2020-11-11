'''
Práctica 6 ejercicio 13
Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.
'''
'''
Este es el ejercicio viejo
Práctica 5. Ejercicio 12

print('Averigua si tu número favorito es primo o no')
numero= int(input('Escribe aquí el número '))

primo = True
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False

print(f'El número {numero} es primo') if primo else print(f'El número {numero} no es primo')
'''

print('Averigua si tu número favorito es primo o no')

numero= int(input('Escribe aquí el número '))
esPrimo = True

divisor = 2
while esPrimo and numero > divisor:
    # print(divisor)
    if numero % divisor == 0:
        esPrimo = False
    divisor += 1

print(f'El número {numero} es primo') if esPrimo else print(f'El número {numero} no es primo')

# Es mejor la opción del WHILE porque en cuanto encuentra un número que es divisor, el bucle se para, por lo que ahorra iteraciones del bucle. EL bucle for, en cambio, no para cuando encuentra un divisor, sino que tiene que dar tantas vueltas como se le haya dicho en el range