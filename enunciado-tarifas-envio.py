kg = float(input("Ingrese el peso del paquete en kg: "))
distancia = float(input("Ingrese la distancia del envío en km: "))

if kg <= 1:
    tarifa_peso = 10
elif kg <= 5:
    tarifa_peso = 20
else:
    tarifa_peso = 30

if distancia <= 100:
    tarifa_distancia = 5
elif distancia <= 500:
    tarifa_distancia = 15
else:
    tarifa_distancia = 25

tarifa_total = tarifa_peso + tarifa_distancia

print(f"El costo total del envío es: ${tarifa_total}")