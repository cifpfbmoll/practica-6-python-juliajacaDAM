'''
Escribe un programa que te pida los nombres y notas de alumnos.
Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá
que no quieres introducir más notas de este alumno.
Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos.
Nota: La lista en la que se guardan los nombres y notas tiene esta estructura
[[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

Dame un nombre: Héctor Quiroga
Escribe una nota: 4
Escribe otra nota: 8.5
Escribe otra nota: 12
Dame otro nombre: Inés Valls
Escribe una nota: 7.5
Escribe otra nota: 1
Escribe otra nota: 2
Escribe otra nota: -5
Dame otro nombre:
Las notas de los alumnos son:
Héctor Quiroga: 4.0 - 8.5
Inés Valls: 7.5 - 1.0 - 2.0

'''
cuaderno_notas = []

alumno = input('Escribe el nombre de un alumno: ')

while alumno != "" "":
    alumno_notas = [alumno]
    nota = float(input(f'Escribe la nota para {alumno}: '))

    while 0 <= nota <= 10 :
        alumno_notas.append(nota)    
        nota = float(input(f'Escribe otra nota para {alumno}: '))
    
    cuaderno_notas.append(alumno_notas)

    alumno = input('Escribe otro nombre de alumno: ')

# print(cuaderno_notas)
# prueba = [['ana', 5, 5 ,5], ['paola', 5, 10,4]]

print('Las notas de los alumnos son: ')

for i in range(len(cuaderno_notas)):
    for j in range(len(cuaderno_notas[i])):
        if j == 0:
            print(cuaderno_notas[i][j], end = ': ')
        elif j == len(cuaderno_notas[i])-1:
            print(cuaderno_notas[i][j], end = '\n')
        else:
            print(cuaderno_notas[i][j], end = '-')
