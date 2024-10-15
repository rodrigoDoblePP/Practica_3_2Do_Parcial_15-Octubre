#3- Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por 
#fruta, 
#un número de kilos 
#mostrar el precio de ese número de kilos de fruta.

print (" ")
print ("Piedra Gonzalez Rodrigo 3-W - 1204")
print (" ")

precios_de_frutas = {  # Creamos un diccionario con las frutas y precios
    "Durazno": 60,
    "Limon": 90,
    "Cereza": 40,
    "Mandarina": 70,
}

fruta = input("Ingresa la fruta que deseas comprar: ")  # Pedimos la fruta a comprar
kilos = float(input("Ingresa el numero de kilos: "))  # Preguntamos por los kilos a llevar

if fruta in precios_de_frutas:  # Verifica si la fruta está en el diccionario
    precio_total = precios_de_frutas[fruta] * kilos
    print("Precio: $", precio_total)  # Mostramos el precio calculado
else:
    print("Lo lametamos chaval, no tenemos esa fruta en el diccionario.") #Mensaje de alerta
