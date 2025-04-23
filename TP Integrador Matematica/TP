#Simulación de Puertas Lógicas Básicas:
#Programa en Python que simule las puertas AND, OR y NOT. Soliciten al usuario ingresar valores binarios (0 o 1) y muestren el resultado de cada operación.
#Extensión: Agregar puertas adicionales (NAND, NOR, XOR) si lo desean.

#Definimos el ingreso del usuario como una funcion para usarlo luego

def input_binario(texto):
    while True:
            valor = int(input(texto))
            if valor in (0, 1):
                return valor
            else:
                print("Por favor, ingresa 0 o 1.")

#Definimos las puertas logicas en una funcion para usarlas luego cuando tengamos los valores

def puertas_logicas(a, b):
    print(f"\nValores ingresados: A = {a}, B = {b}")
    print(f"AND  (A and B): {a & b}")
    print(f"OR   (A or B): {a | b}")
    print(f"NOT  (not A): {1 - a} | (not B): {1 - b}")
    print(f"NAND (not (A and B)): {1 - (a & b)}")
    print(f"NOR  (not (A or B)): {1 - (a | b)}")
    print(f"XOR  (A xor B): {a ^ b}")

#Este es el programa propiamente dicho, donde se da un titulo de que hace, se pide ingresar los valores y luego ver los resultados

print("Simulador de puertas logicas")
a = input_binario("Ingresa el primer valor binario")
b = input_binario("Ingresa el segundo valor binario")
puertas_logicas(a,b)


