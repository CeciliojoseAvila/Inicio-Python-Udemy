#nombre = input("¿Cuál es tu nombre: \r\n")
#print("Hola mi nombre es " + nombre)

edad = input("¿Cuál es tu edad?: \r\n")
edad = int(edad)
if edad >= 18:
    print("Puedes votar")
else:
    print("Aún no Puedes votar")

    #par o impar
numero = input("Agrega un numero y te diré si es par o impar: \r\n")
numero= int(numero)
if numero % 2 ==0:
    print(f"El número {numero} es par ")
else:
    print(f"El número {numero} es impar ")
