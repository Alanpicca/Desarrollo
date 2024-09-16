ingreso_accesorios = float(input("ingrese los montos ingresados por accesorios: "))
ingreso_reparacion = float(input("introduzca el monto ingresado de la reparacion: "))
egreso_accesorios = float(input("introduzca el monto que pago el accesorio: "))
egreso_repuesto = float(input("introduzca el monto que pago los repuestos: "))
ganancia_accesorio = ingreso_accesorios - egreso_accesorios
ganancia_reparacion = ingreso_reparacion - egreso_repuesto
#mostrar las ganancias
print(f"la ganancia de los accesorios es de: {ganancia_accesorio} y la ganancia por reparacion es de: {ganancia_reparacion}")