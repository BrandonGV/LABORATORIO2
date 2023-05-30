numeros = []
suma = 0

while True:
    try:
        numero = int(input("Ingrese un número entero (o un valor no numérico para terminar): "))
        numeros.append(numero)
        suma += numero
    except ValueError:
        break

if numeros:
    promedio = suma / len(numeros)
    print("La sumatoria de los números ingresados es:", suma)
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números.")
