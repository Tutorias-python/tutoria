def calcularpiscina():
    # pedir entradas
    a = int(input("Ingrese altura de la piscina: "))
    l = float(input("Ingrese el largo de la piscina: "))
    precio = int(input("Ingrese el precio: "))

    # calcular
    metrocubico = a*l*a
    total = precio*metrocubico

    #Imprimir
    print("El total a paga es de "+total+" de colones")

calcularpiscina()
