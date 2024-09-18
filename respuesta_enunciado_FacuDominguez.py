try:
    tipo_vehiculo = str(input("Ingrese el tipo de vehículo(Automovil, Camioneta o Camion): ")).upper()
    if tipo_vehiculo not in ["CAMION", "CAMIONETA", "AUTOMOVIL"]:
        raise ValueError("Debe ingresar el tipo de vehículo: Automovil, Camioneta o Camion")
except ValueError as e:
    print(f"Error: {e}")
else:
    try:
        peso_vehiculo = float(input("Ingrese el peso del vehículo(en kilogramos): "))
    except ValueError:
        print("Error: Debe ingresar el peso del vehículo en kilogramos")
        precio = 0
    else:
        match tipo_vehiculo:
            case "AUTOMOVIL":
                if peso_vehiculo < 1000:
                    precio = 50000
                else:
                    precio = 70000
            case "CAMIONETA":
                if peso_vehiculo < 2500:
                    precio = 120000
                else:
                    precio = 160000
            case "CAMION":
                if peso_vehiculo < 18000:
                    precio = 1500000
                elif peso_vehiculo >= 18000 and peso_vehiculo <= 25000:
                    precio = 1900000
                else:
                    precio = 2400000
        print(f"El precio del servicio es de ${precio}")
finally:
    print("Gracias por utilizar éste programa")