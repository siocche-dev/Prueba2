continuar = "si"
while continuar == "si":
    preciomed = 60000
    preciodesp = 8000
    
    edad = int (input("Ingrese su edad:"))
    tramo = input ("Ingrese su tramo: A, B, C o D): ") .upper()
    
#Descuentos
    dsctomedicamento = 0

    if edad <= 30:
        if tramo =="A" or tramo == "B":
            dsctomedicamento = 0.18
        if tramo == "C" or tramo == "D":
            dsctomedicamento = 0.12
    elif edad > 30 and edad <= 60:
        if tramo =="A" or tramo == "B":
            dsctomedicamento = 0.12
        if tramo == "C" or tramo == "D":
            dsctomedicamento = 0.08
    #Despacho
    dsctodespacho = 0
    if (tramo == "A" or tramo == "C") and edad <= 60:
        dsctodespacho = 0.10
        if edad >= 55:
            dsctodespacho += 0.05
    #Calculos
    valormedfinal = preciomed - (preciomed * dsctomedicamento)
    valordespfinal = preciodesp - (preciodesp * dsctodespacho)

    print ("El valor del medicamento es: ", int (valormedfinal))
    print ("El valor del despacho es: ", int(valordespfinal))
    
    continuar = input ("¿Desea consulta por otra persona? (si/no): ") .lower()