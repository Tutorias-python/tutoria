def produccion():
    # Pedir entradas
    litros = float(input("Ingrese la cantidad de litros: "))
    precio = float(input("Ingrese precio por galon: "))

    #Calcular
    galones = litros/3.785 #convertir los litros a galones
    total = precio*galones #sacar el total de pago por los galones

    #Imprimir el resultado
    print("El pago total es de {}".format(total))

#main
produccion()
