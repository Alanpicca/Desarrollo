"""En una empresa, se manufacturan un promedio de diez mil engranajes al mes. Este mes se requiere medir el porcentaje de eficiencia con respecto al mes anterior (10000 engranajes).
Si se hicieron la misma cantidad de engranajes, el porcentaje de eficiencia sería del 100%, por el contrario, si se hicieron menos, la eficiencia es menor y viceversa.
El programa debería pedir el ingreso de la cantidad de engranajes hechos este mes y compararlos con datos guardados del anterior mes e imprimir por pantalla el porcentaje de eficiencia.
Si la eficiencia supera el 100%, imprimir por pantalla un mensaje similar a "Exedente de engranajes"""

engranajes_antes = int(input("ingresa los engranajes del mes anterior: "))
engranajes_ahora = int(input("ingresa los engranajes de este mes: "))
eficiencia = (engranajes_ahora*100)/engranajes_antes
if eficiencia > 100:
    print(f"Exedente de engranajes \nEficiencia del {eficiencia}%")
else:
    print(f"Eficiencia del {eficiencia}%")