#Escribe un programa que determine el tipo de membresía de un gimnasio según la edad y el género del cliente. Las reglas son las siguientes:

#Si el cliente es hombre y tiene menos de 18 años, no es elegible para una membresía.
#Si el cliente es hombre y tiene entre 18 y 30 años, la membresía es de tipo "Estudiante"
#Si el cliente es hombre y tiene entre 31 y 60 años, los  miembros es de tipo "Adulto"
#Si el cliente es hombre y tiene 61 años o más, la membresía es de tipo "Senior"
#Si el cliente es mujer y tiene menos de 18 años, no es elegible para una membresia.
#Si el cliente es mujer y tiene entre 18 y 30 años, la membresía es de tipo"Estudiante femenino"
#Si el cliente es mujer y tiene entre 31 y 60 años, la membresía es de tipo "Adulto Femenino".
#Si el cliente es mujer y tiene 61 años o más, la membresía es de tipo "Senior femenino"
#Si el género del cliente no es hombre ni mujer, no es elegible.

edad = int(input("Ingresar la edad: "))
genero = (input("ingresar genero: "))

if genero == "hombre" "mujer":
    if edad <18:
        print("no es elegible para la membresia")

elif genero == "hombre":
    if 18 <= edad <=30:
        print("Tu membresia es de tipo estudiante")
    
elif genero == "hombre":
    if 31 <= edad <=60:
        print("Tu membresia es de tipo adulto")

elif  genero == "hombre":
    if 61<= edad:
     print("Tu membresia es de tipo señor")

elif genero == "mujer":
    if 18 <= edad <= 30:
     print("Tu membresia es de tipo estudiante femenino")

elif genero == "mujer":
    if 31 <= edad <=60:
     print("Tu membresia es de tipo adulto femenino")

elif genero == "mujer": 
   if 61 <= edad:
    print("Tu membresia es de tipo senior femenino")

else:
   print("Genero elegido no es correcto.")

   



