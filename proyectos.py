#Esto es un comentario de una sola linea 
"""Esto es un comentario de
varias lineas"""

#inicializando variables
nombre="Nikole Lorena Molina Bravo"
edad=14
estado=True
nota=5.0 

#Mostrar el contenido de las variables print()
print(nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#Vamos a utilizar la función input para recoger datos por medio del teclado.
nombre=input("¿Cuál es tu nombre? ")
edad=input("¿Cuál es tu edad? ")
estado=input("¿Cuál es tu estado? ")
nota=input("¿Cuál es tu nota? ")

#Para visualizar que guardamos en las variables anteriores.
print("Hola,",nombre,"un gusto conocerte")
print("Tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)