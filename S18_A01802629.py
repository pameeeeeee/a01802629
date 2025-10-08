temperaturas = [22, 24, 19, 21, 25, 23, 20]
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.2f}°C\n")
for i, temp in enumerate(temperaturas, start=1):
    if temp > promedio:
        print(f"Día {i}: {temp}°C está arriba de la media")
    elif temp < promedio:
        print(f"Día {i}: {temp}°C está debajo de la media")
    else:
        print(f"Día {i}: {temp}°C está exactamente en la media")

estudiantes = ["Ana", "Luis", "María", "Pedro", "Sofía"]
promedios = [8.5, 6.0, 9.2, 5.8, 7.0]
promedio_general = sum(promedios) / len(promedios)
for promedio in promedios: 
    if promedio < promedio_general:
        print(promedio)
reprobados = []
for i in (len(promedios)):
    if promedios[i] < promedio_general:
        reprobados.append(estudiantes[i])
print("Estudiantes reprobados:", reprobados)


compras = ["leche", "pan", "huevos", "frutas"]
ya_comprado = [False, False, False, False]
print("Artículos que aún no ha comprado:")
for i in range(len(compras)):
    if not ya_comprado[i]:
        print(compras[i])
        
for i in range(len(compras)):
    if not ya_comprado[i]:
        respuesta = input(f"¿Ya compraste {compras[i]}? (s/n): ")
        if respuesta.lower() == "s":
            ya_comprado[i] = True
print("Artículos ya comprados:")
for i in range(len(compras)):
    if ya_comprado[i]:
        print(compras[i])


numeros = [5, 2, 9, 1, 5, 6]
maximo = max(numeros)
minimo = min(numeros)
ordenados = sorted(numeros)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
print("Lista ordenada:", ordenados)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Números pares:", pares)
print("Números impares:", impares)


nombres_usuarios = []
while True:
    nuevo_nombre = input("Introduce un nombre de usuario: ")
    if nuevo_nombre not in nombres_usuarios:
        nombres_usuarios.append(nuevo_nombre)
        print("Nombre de usuario añadido.")  
    else:
        print("El nombre de usuario ya existe. Por favor, elige otro.")

