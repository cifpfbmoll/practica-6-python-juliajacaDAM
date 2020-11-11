'''
Práctica 6, ejercicio 3

Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
Escribe una nota: 7.5
Escribe una nota: 0
Escribe una nota: 10
Escribe una nota: -1
Las notas que has Escrito son [7.5, 0.0, 10.0]

'''

lista_notas = list()
nota = float(input('Escribe una nota: '))

while  0 <= nota <= 10:
    lista_notas.append(nota)
    nota = float(input('Escribe otra nota: '))


print('Las notas que has escrito son', lista_notas)