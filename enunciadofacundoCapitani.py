# Realiz un algoritmo que solicite dos números enteros y los guarde en dos variables. Luego, el programa debe intercambiar
# el valor de estas dos variables sin utilizar una tercera variable auxiliar. 
# Finalmente, el programa debe mostrar el contenido de las variables para comprobar que el intercambio se ha realizado correctamente.

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

num1, num2 = num2,num1  

print(f"los valores intercambiados de los numeros son: {num1} y {num2}")