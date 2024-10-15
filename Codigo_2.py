#2- Preguntar al usuario nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
print (" ")
print ("Piedra Gonzalez Rodrigo 3-W - 1204")
print (" ")

nombre = input ("¿Cual es tu nombre?: ")     #Solicitamos el nombre y lo guardamos en la variable nombre
edad   = int(input("¿Cuantos años tienes?: ")) # Solicitamos la edad y lo guardamos en la variable edad
direccion = input ("¿Cual es tu direccion?: ") #Solicitamos la direccion y lo guardamos en la variale direccion
telefono = int(input("¿Cual es tu numero de telefono?: ")) #Solicitamos el telefono y lo guardamos en la variable telefono

Datos_Del_usuario = {   #Guardamos los datos ingresados en un diccionario 
    "Nombre": nombre,
    "Edad":   edad,
    "Direccion": direccion,
    "Telefono": telefono,
} 
print(" ")                         #Imprimimos un espacio
print (nombre, "\nTiene",               #Imprimimos el texto deseado con las variables ya ingresadas 
       edad, " años \n"
       "Y vive en", direccion,
       "\nY su numero de telefono es" ,telefono,)
print (" ") #Imprimimos espacio 