#una empresa de servicio técnico de celulares necesita realizar el balance mensual.
#la empresa cuenta con lo siguiente: ingresos por accesorios. ingresos por reparación y los egresos de la mercaderia(accesorios y repuestos)
#como crees que podrías ayudar a esta empresa a saber cuales son sus ingresos, sus egresos y su ganancia, en el caso de no obtener ganancia
#mostrar un mensaje que muestre que no obtuviste ganancia.

ingresosacc=float(input("ingrese los valores ingresados por venta de accesorios del mes: ")) 
ingresosrepa=float(input("ingrese los valores ingresados por reparaciones del mes: ")) 
egresos=float(input("ingrese los egresos del mes:")) 


totalingresos=ingresosacc + ingresosrepa 
ganancia= totalingresos - egresos 

if totalingresos > ganancia: 
    print(f"el total de los ingresos fue de {totalingresos}, los egresos totales son de {egresos} y la ganacia que tuvimos fue de {ganancia}") 
else: print("no obtuvo ganancias")