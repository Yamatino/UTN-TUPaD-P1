#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Lucas")

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresar nombre")
apellido = input("Ingresar apellido")
edad = input("Ingresar edad")
residencia = input("Ingresar residencia")

informacion_personal(nombre,apellido,edad,residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

def calcular_area_circulo(radio):
    return 3.14 * radio**2

def calcular_perimetro_circulo(radio):
    return 2*3.14*radio

radio = float(input("Porfavor ingrese el radio del circulo"))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El Area del circulo con radio {radio} es {area} y su perimetro es {perimetro}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos para convertir a horas"))
print(segundos_a_horas(segundos))

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for x in range(1,11):
        print(numero * x)

numero = int(input("Ingrese un numero para saber su tabla de multiplicar del 1 al 10"))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    print(f"La suma da {a+b}")
    print(f"La resta da {a-b}")
    print(f"La multiplicacion da {a*b}")
    print(f"La division da {a/b}")

a = int(input("Ingrese primer numero"))
b = int(input("Ingrese segundo numero"))

operaciones_basicas(a,b)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    return peso/(altura**2)

peso = int(input("Ingrese su peso en KG"))
altura = float(input("Ingrese su altura en metros"))

print(f"Su IMC es {calcular_imc(peso,altura)}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    print((celsius*(9/5)) + 32)

celsius = int(input("Ingrese la temperatura en celsius para obtener fahrenheit"))

celsius_a_fahrenheit(celsius)

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función

def calcular_promedio(a,b,c):
    print(f"El promedio es {(a+b+c)/3}")

a = int(input("Ingrese primer numero"))
b = int(input("Ingrese segundo numero"))
c = int(input("Ingrese tercer numero"))

calcular_promedio(a,b,c)