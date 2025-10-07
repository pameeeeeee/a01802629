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
print(f"Promedio general de los alumnos: {promedio_general:.2f}")
aprobados = [p for p in promedios if p >= 6.0]
porcentaje_aprobados = (len(aprobados) / len(promedios)) * 100
print(f"Porcentaje de alumnos aprobados: {porcentaje_aprobados:.2f}%")
reprobados = [estudiantes[i] for i, p in enumerate(promedios) if p < 6.0]
print("Estudiantes que reprobaron:", reprobados)


