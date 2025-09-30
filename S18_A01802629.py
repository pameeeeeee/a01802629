
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
