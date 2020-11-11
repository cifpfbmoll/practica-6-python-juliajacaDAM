'''
Desarrolla un programa junto con tu compañero, apoyándote en la “metodología pair programming” que tenga las siguientes características:
Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
Dicho problema resuélvelo con bucles for y while. 
Justifica en el propio programa porque una opción es adecuada y la otra no.
¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente una solución es más eficiente? Investiga para comprobarlo.

'''

'''
Problema: el usuario tiene 3 intentos para sacar un 7 tirando dos dados de 6
'''

from random import randint

print('ESTO ES CON UN BUCLE FOR')
for intento in range(0,3):
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    resultado_intento = dado1 + dado2
    print('Tu resultado ha sido: ',resultado_intento)
    if resultado_intento == 7:
        print('¡Lo has conseguido con un for!')

# ------------------------------------------------------------------
print('ESTO ES CON UN BUCLE WHILE')
intentos = 0
fallo = True
while fallo and intentos < 3:
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    resultado_intento = dado1 + dado2
    print('Tu resultado ha sido: ',resultado_intento)
    if resultado_intento == 7:
        fallo = False
        print('¡Lo has conseguido con un while!')
    intentos +=1


# A pesar de que en este caso se conocen el números de veces que se ha de pasar por el blucle y un for sería /
# lo recomendado en este caso, también es cierto que es más eficiente salir del bucle en cuanto la condición de sacar/
# un 7 en los dados se cunpla, por lo que nos ahorraríamos tiempo de ejecución de programa con un bucle while. EL número de /
# veces que se pasa en el bucle se puede controlar perfectamente en un while con un contador