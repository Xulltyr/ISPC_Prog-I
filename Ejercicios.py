"""1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:"""
num=(input("Ingrese un numero entero de tres digitos: "))
num = sorted(num, reverse=True)
print(f"El numero dado al revez es: {num}")


"""2- Escriba un programa que pregunte al usuario la hora actual "t" del reloj y un número entero de
horas "h", que indique qué hora marcará el reloj dentro de "h" horas:"""
t = int(input("Ingresar la hora actual del reloj (formato HHMM sin dos puntos): "))
h = int(input("Ingresar un número entero de horas: "))

hora_actual = t // 100   # ejemplo: 1530 → 15
min_actual = t % 100     # ejemplo: 1530 → 30

nueva_hora = (hora_actual + h) % 24
nueva_hora_total = nueva_hora * 100 + min_actual

print(f"La hora será: {nueva_hora_total:04d}")


"""3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""
num = int(input("Ingrese un numero entero: "))
if num <= 1:
    print("No es primo.")
else:
    esPrimo = True

    for i in range(2, num):
        if num % i == 0:
            esPrimo = False
            break

    if esPrimo:
        print("Es primo.")
    else:
        print("No es primo.")

       
"""4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene laduración en minutos de 
cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue
como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0."""
print("Ingrese los tiempos de cada tramo en minutos (ingrese 0 para finalizar):")

tiempo_total = 0
tramo_numero = 1  # Iniciamos el contador de tramos

while True:
    tramo = int(input(f"Minutos del Tramo {tramo_numero}: "))
    
    if tramo == 0:
        break
    elif tramo < 0:
        print("El tiempo no puede ser negativo.")
    else:
        tiempo_total += tramo
        tramo_numero += 1

horas = tiempo_total // 60
minutos = tiempo_total % 60

print(f"Tiempo total de viaje: {horas} horas y {minutos} minutos.")


"""5- Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente
365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la diferencia es de más o menos un cuarto de día.
Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la
regla de introducir un día adicional en los años divisibles por 4 (llamados bisiestos), para tomar en consideración 
los cuatro cuartos de día acumulados.
Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.
Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario,
en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.
Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:"""
def es_bisiesto(año):
    if (año % 400 == 0):  # Si es divisible por 400
        return True
    elif (año % 100 == 0):  # Si es divisible por 100 pero no por 400
        return False
    elif (año % 4 == 0):  # Si es divisible por 4 pero no por 100
        return True
    else:
        return False

año = int(input("Ingrese un año para saber si es bisiesto: "))

if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")


"""6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el usuario."""
renglones = int(input("Ingrese la cantidad de renglones: "))
for i in range(1, renglones + 1):
    for j in range(i, 0, -1):
        print(j * 2, end=' ')
    print()


"""7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;
● La sucesión termina al llegar a uno.
Desarrolle un programa que entregue la secuencia de Collatz de un número entero:"""
def collatz(n):
    print(n, end=' ')
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)
        
        
"""8- Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen respectivamente $270, $340 y $390. 
La máquina acepta y da de vuelto monedas de $10, $50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. 
Si el monto ingresado es mayor que el precio del producto, el programa debe entregar las monedas de vuelto, una por una."""


"""9 - Anagrama. Escribe una función que reciba dos palabras y retorne verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama."""


"""10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas, numeradas de 1 a 8. 
Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se desplaza en diagonal, mientras que la torre se desplaza 
horizontal o verticalmente. Una pieza puede ser capturada por otra si está en una casilla a la cual la otra puede desplazarse:
Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de una torre, e 
indique cuál pieza captura a la otra:"""


"""11- Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a piedra, piedra le gana a tijera, 
y todas las demás combinaciones son empates. El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el marcador después de cada ronda, 
y termine cuando uno de ellos haya ganado tres rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra."""


"""12- Torneo de Tenis. Escriba un programa para simular un campeonato de tenis. Primero, debe pedir al usuario que ingrese los 
nombres de ocho tenistas. A continuación, debe pedir los resultados de los partidos juntando los jugadores de dos en dos. 
El ganador de cada partido avanza a la ronda siguiente.
El programa debe continuar preguntando ganadores de partidos hasta que quede un único jugador, que es el campeón del torneo."""


""""13- El diccionario países asocia cada persona con el conjunto de los países que ha visitado:
Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han visitado la persona a y la persona b:"""


"""14- Signo zodiacal. El signo zodiacal de una persona está determinado por su día de nacimiento. El diccionario de signos asocia a 
cada signo el período del año que le corresponde. Cada período es una tupla con la fecha de inicio y la fecha de término, 
y cada fecha es una tupla (mes, dia):
Por ejemplo, para que una persona sea de signo libra debe haber nacido entre el 24 de septiembre y el 23 de octubre.
Escriba la función determinar_signo(fecha_de_nacimiento) que reciba como parámetro la fecha de nacimiento de una persona, 
representada como una tupla (año, mes, dia), y que retorne el signo zodiacal de la persona:"""


"""15- Autores de Libros. Este problema apareció en el certamen 2 del segundo semestre de 2011 en el campus Vitacura.
Escriba las funciones necesarias para que el siguiente programa funcione:"""


"""16- Código Morse. Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
● Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
● En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras " ".
● El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse"""