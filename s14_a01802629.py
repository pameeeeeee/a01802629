edad = int(input("¿Cuál es tu edad? "))
if edad >= 18:
    print("Eres adulto.")
else:
    print("No eres adulto.")


edad = int(input("¿Cuál es tu edad? "))
if 13 <= edad <= 19:
    print("Eres adolescente.")
else:
    print("No eres adolescente.")


nacimiento = int(input("¿En qué año naciste? "))
edad = 2025 - nacimiento
print("Tienes", edad, "años")
