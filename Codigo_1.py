#1- Guardar en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
print (" ")
print ("Piedra Gonzalez Rodrigo 3-W - 1204")
print (" ")

thisdict =	{             #Guardamos en una variable el diccionario
  "Euro": "€",
    "Dolar":  "$",
         "Yen":      "¥"
}

divisa = input ("Ingresa la divida que quieras solicitar: ")  #Solicitamos la divisa e ingresamos
if divisa in thisdict:               #Si en la variable divisa  se leen los mismos valores del diccionario
    print ("Esta es la divisa que ingresaste y su simbolo Es : ", (thisdict[divisa])) #imprimimos mensaje con el simbolo de el 
    #valor ingresado
else:                                                     #si no se encuentran los mismos valores
    print("La divisa que ingresaste no esta en el diccionario") #Imprimimos un mensaje de alerta
    
    
