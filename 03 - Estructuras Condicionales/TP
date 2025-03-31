#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese nota obtenida del 1 al 10 "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar

numero = int(input("Ingrese un numero par "))

if numero % 2 != 0:
    print("Porfavor ingrese un numero par ")
else:
    print("Ha ingresado un numero par ")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

password = input("Ingrese su contraseña de entre 8 y 14 caracteres")

passlargo = len(password)

if passlargo >= 8 and passlargo <= 14:
    print("La contraseña es adecuada ")
else:
    print("Porfavor ingrese una contraseña entre 8 y 14 caracteres ")

#6) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print (f"La moda es {moda}, la mediana es {mediana} y la media es {media} ")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha ")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda ")
elif media == moda == mediana:
    print("No hay sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla

#nota: Al no tener una manera (por lo menos que haya visto) en los ejercicios de comparar, google alternativas para completar el ejercicio y encontre endswith

palabra = input("Porfavor ingrese una frase o palabra")

vocales = ('a', 'e', 'i', 'o', 'u')

if palabra.endswith(vocales,-1):
    print(palabra + "!")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Porfavor ingresar tu nombre ")
opcion = int(input("Ingresar 1 si quiere su nombre en mayusculas, 2 para minusculas y 3 si solo quiere su primera letra mayuscula"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

terremoto = float(input("Ingrese la magnitud del terremoto "))

if terremoto < 3:
    print("Muy leve (imperceptible)")
elif terremoto >= 3 and terremoto <= 4:
    print("Leve (ligeramente perceptible)")
elif terremoto >= 4 and terremoto <= 5:
    print(" Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto >= 5 and terremoto <= 6:
    print("Fuerte puede causar daños en estructuras débiles")
elif terremoto >= 6 and terremoto <= 7:
    print("Muy fuerte (puede causar daños significativos)")
elif terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

#nota: Busque un modulo para analizar fechas sino habria que definirlas todas manual

import datetime


hemisferio = input("En que hemisferio se encuentra? Escriba N para norte y S para sur").upper()

mes = int(input("Ingrese el mes que es "))
dia = int(input("Ingrese el dia que es "))

#una vez conseguida la info la hago una variable para despues comparar

fecha = datetime.date(2025, mes, dia)

#periodo 1
if fecha >= datetime.date(2024,12,21) and fecha <= datetime.date(2025,3,20):
    if hemisferio == "N":
        print("Es Invierno")
    else:
        print("Es Verano")

#periodo 2
elif fecha >= datetime.date(2025,3,21) and fecha <= datetime.date(2025,6,20):
    if hemisferio == "N":
        print("Es Primavera")
    else:
        print("Es Otoño")

#periodo 3
elif fecha >= datetime.date(2025,6,21) and fecha <= datetime.date(2025,9,20):
    if hemisferio == "N":
        print("Es Verano")
    else:
        print("Es Invierno")

#periodo 4
elif fecha >= datetime.date(2025,9,21) and fecha <= datetime.date(2025,12,20):
    if hemisferio == "N":
        print("Es Otoño")
    else:
        print("Es Primavera")

#hay un caso limite donde la fecha es entre el 22 de diciembre y hasta 1 de enero donde por como funcionan los rangos y los años no puedo definirlo comodamente
#esta contemplado en la linea de abajo

else:
    if hemisferio == "N":
        print("Es Invierno")
    else:
        print("Es Verano")