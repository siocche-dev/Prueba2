from random import randint

num1 = int(input("Ingrese un número minimo: "))
num2 = int(input("Ingrese un número maximo: "))

numero = randint(num1,num2)

#Impar
if numero %2 ==0:
    if numero +1 <= num2:
        numero = numero  + 1
    else:
        numero = numero - 1
        
turno  = 1
adivino = False  

intento1 = 0
intento2 = 0
  
while turno <= 3 and adivino == False:
    intento = int (input("Ingrese su numero: "))
    
    if intento == numero:
            print ("¡Felicidades! Has adivinado el número.")
            adivino = True
    else:
        if intento < numero:
                print ("El número secreto es mayor.")
        else:
                print ("El número secreto es menor.")
        if turno  == 1:
            intento1 = intento 
        elif turno == 2:
            intento2 = intento
    
        distancia1 = abs(numero - intento1)
        distancia2 = abs(numero - intento2)
    
        print ("Te dare una pista ") 
        if distancia1 < distancia2:
            print ("El primer intento esta mas cerca", intento1, "que de" , intento2)
        elif distancia2 < distancia1:
            print ("El segundo intento esta mas cerca", intento2, "que de" , intento1)
        else: 
            print ("Ambos intentos estan cerca")
    
    turno    += 1
if adivino == False:
    print ("Lo siento, perdiste. El número correcto era:", numero)