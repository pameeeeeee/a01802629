cantidadDeDonas= int(input ("dame una cantidad de donas"))
print("Con"+ str(cantidadDeDonas)+ "donas alcanza para"+str(cantidadDeDonas//12)+"docenas")

cantidadDeNumero1= int(input ("introduce la cantidad del primer numero"))
cantidadDeNumero2= int(input("introduce la cantidad del primer numero"))
residuo = cantidadDeNumero1 % cantidadDeNumero2
print("El residuo de la division entre" + str(cantidadDeNumero1) + " y " + str(cantidadDeNumero2) + " es " + str(residuo))

segundos = int(input ("introduce la cantidad de segundos que deseas convertir: "))
horas = segundos  // 3600
minutos = (segundos % 3600) // 60
seg = segundos % 60
print(str(segundos) + "segundos son equivalente a: " + str(horas) + str(minutos) + "minutos y " + str(seg) + "segundos. ")
