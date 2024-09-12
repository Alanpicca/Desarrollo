ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
tipo_pizza = input("¿Quieres una pizza vegetariana? (si/no): ")
if tipo_pizza.lower()== "si":
    ingredientes = ingredientes_vegetarianos
else:
    ingredientes = ingredientes_no_vegetarianos
print("Elige un ingrediente (además de mozzarella y tomate):")
for i, ingrediente in enumerate(ingredientes, 1):
    print(f"{i}. {ingrediente}")
eleccion = int(input("Introduce el número de tu ingrediente elegido: "))
ingrediente_elegido = ingredientes[eleccion - 1]
if tipo_pizza.lower() == "si":
    print(f"Elegiste una pizza vegetariana con mozzarella, tomate y {ingrediente_elegido}.")
else:
    print(f"Elegiste una pizza no vegetariana con mozzarella, tomate y {ingrediente_elegido}.")