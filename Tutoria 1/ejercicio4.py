def calcularSalario():
    #pedir entrasdas
    horasLaboradas = int(input("Ingrese horas laboradas: "))
    salarioHora = int(input("Ingrese salario horas: "))
    horasExtra = int(input("Horas extra: "))
    pagoSalarioExtra = int(input("Pago salario extra: "))

    #calcular
    salarioBase = horasLaboradas*salarioHora
    SalarioExtra = horasExtra*pagoSalarioExtra
    salarioBruto = salarioBase+SalarioExtra

    #calculo de deducciones
    Dpopular = salarioBruto*0.01
    Ds = salarioBruto*0.0550
    Dc = salarioBruto * 0.0284
    deduccionTotal= Dpopular+Ds+Dc

    #calculo de salario liquido
    salarioLiquido = salarioBruto-deduccionTotal

    #Imprimir
    print("El salario bruto es de {}, las deducciones son de {} y el salario liquido es de {}".format(salarioBruto,deduccionTotal,salarioLiquido))

calcularSalario()
