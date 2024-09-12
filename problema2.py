nombre = str(input("Ingrese su nombre: ")).upper()
sexo = str(input("Ingrese su sexo: "))

if sexo == "F":
    if nombre[0] < "M":
        print(nombre, sexo, "Grupo A", sep=", ")
    else:
        print(nombre, sexo, "Grupo B", sep=", ")
elif sexo == "M":
    if nombre[0] > "N":
        print(nombre, sexo, "Grupo A", sep=", ")
    else:
        print(nombre, sexo, "Grupo B", sep=", ")