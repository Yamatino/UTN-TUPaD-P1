#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Es mas util usar un string y contar posiciones

numero = input("Ingresar un numero entero")

print(len(numero))

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingresar un numero entero"))
numero2 = int(input("Ingresar otro numero entero para sumar"))

for i in range(numero1+1,numero2):
    print(i)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

numero = int(input("Ingresar numero para sumar"))
numerosuma = int(input("Ingrese otro numero para sumarlo"))

numero = numero + numerosuma

while numerosuma != 0:
    numerosuma = int(input("Ingresar otro numero para sumar, ingrese 0 para frenar la suma y ver resultado "))
    numero = numero + numerosuma

print(numero)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numeroazar = random.randint(0,9)
numeroadivinado = int(input("Ingresar un numero del 0 al 9 para adivinar"))
contador = 0

while numeroadivinado != numeroazar:
    contador = contador + 1
    numeroadivinado = int(input("Erroneo , intente otro numero"))

print(f"Felicidades, pudiste adivinarlo en {contador+1} intentos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,-1,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("ingrese un numero entero positivo"))

suma = 0

for i in range(numero+1):
    suma += i

print(f"La suma de los numeros de 0 a {numero} es de {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador = 0

pares = 0
impares = 0
positivos = 0
negativos = 0

#facilmente escalable modificando el contador en el while (el target)

while contador < 100:
    numero = int(input("Ingrese un numero para contabilizar"))
    #pares o impares
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    #positivos o negativos
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    #avanzamos el loop
    contador = contador + 1

#Resultados

print(f"De los numeros ingresados hay {pares} pares, {impares} impares, {positivos} positivos y {negativos} negativos")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0

while contador < 5:
    numero = int(input("Ingrese un numero para sumar al promedio"))
    suma = suma + numero
    contador = contador + 1


print(f"Fueron ingresados {contador} valores, el promedio entre todos ellos da {suma/contador}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#para este ejercicio tuve que googlear una manera de invertir el texto del numero en este caso con "slicing"


numero = input("Introduce un número: ")

numero_invertido = numero[::-1]

print(f"El {numero} cuando es invertido es {numero_invertido}")