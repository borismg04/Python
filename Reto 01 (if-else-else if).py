Nombre= input("Buen dia, digite su nombre : ");#inicio de conversacion 
Apellido=input("Digite su apellido : ");
print("Hola",Nombre,Apellido);#ingreso de de datos (Nombre y apellido )
opcion=int(input("Desea conocer el descuento de su matricula para el siguiente periodo = Digite 1 (SI) / Digite 2 (NO) :"))#Condicin no 1=entrada al prorama o salida de la consulta  
if opcion== 1 :#Opcion No 1 para entrar a la consulta de los descuentos de la matricula 
    print("Si")
    e=0 #acumulado 1 
    s=0 #acumulado 2 
    c=0 #acumulado #3
    edad = int(input("Por favor digite su edad : ")); # intro no 1 edad para aplicar descuentos
    rango_15_18=float(0.25)#descuento 1 por edad 
    rango_19_21=float(0.15)#descuento 2 por edad 
    rango_22_25=float(0.10)#descuento 3 por edad 
    if edad >= 15 and edad<= 18: #condicion uno por rago de edad 
        print(Nombre,Apellido,"El descuento es del : ",rango_15_18*100,"%")
        e = e + (0.25*100)
    elif edad >=19 and edad<= 21: #condicion dos por rago de edad 
        print(Nombre,Apellido,"El descuento es del : ",rango_19_21*100,"%")
        e = e + (0.15*100) 
    elif edad >=22 and edad<=25: #condicion tres por rago de edad 
        print(Nombre,Apellido,"El descuento es del : ",rango_22_25*100,"%")
        e = e + (0.10*100)
    else:
        print(Nombre,Apellido,"Por su edad no tiene Beneficio") # condicion si no cumple 
        e = e + 0
    salarios=float(input("Por favor,digite cuantos salarios le ingresa a su familia : "))# intro no 2 salarios para aplicar descuentos
    salario_0_1=float(0.30)#descuento 1 por salario
    salario_1_2=float(0.20)#descuento 2 por salario
    salario_2_3=float(0.10)#descuento 3 por salario
    salario_3_4=float(0.05)#descuento 4 por salario
    if salarios >= 0.1 and salarios <= 1: #condicion uno por rago de salario
        print(Nombre,Apellido,"El descuento es del : ",salario_0_1*100,"%")
        s = s + (0.30*100)
    elif salarios >=1.1 and salarios<= 2:#condicion dos por rago de salario
        print(Nombre,Apellido,"El descuento es del : ",salario_1_2*100,"%")
        s= s + (0.20*100)
    elif salarios >=2.1 and salarios<=3: #condicion tres por rago de salario
        print(Nombre,Apellido,"El descuento es del : ",salario_2_3*100,"%")
        s = s + (0.10*100)
    elif salarios >=3.1 and salarios<=4: #condicion cuatro por rago de salario
        print(Nombre,Apellido,"El descuento es del : ",salario_3_4*100,"%")
        s = s + (0.05*100)
    else :
        print(Nombre,Apellido,"Por sus salarios familiares no tiene Beneficio")# condicion si no cumple 
        s = s + 0
    calificacion= int(input ("Por favor, digite cual fue su puntaje : "))# intro no 3 puntaje para aplicar descuentos
    calificacion_80_86=float(0.30)#descuento 1 por puntaje
    calificacion_86_91=float(0.35)#descuento 2 por salario
    calificacion_91_96=float(0.40)#descuento 3 por salario
    if calificacion >= 80 and calificacion<= 86: 
        print(Nombre,Apellido,"El descuento es del : ",calificacion_80_86*100,"%")#condicion uno por puntaje
        c = c + (0.30*100)
    elif calificacion>=86 and calificacion<= 91: 
        print(Nombre,Apellido,"El descuento es del : ",calificacion_86_91*100,"%")#condicion dos por puntaje
        c = c + (0.35*100)
    elif calificacion>=92 and calificacion<=100: 
        print(Nombre,Apellido,"El descuento es del : ",calificacion_91_96*100,"%")#condicion tres por puntaje
        c = c + (0.40*100)
    else :  
        print (Nombre,Apellido,"No tiene beneficio por su calificacion",calificacion,"Ptos");# condicion si no cumple 
        c = c + 0
    print(Nombre,Apellido, "El acumulado de descuentos para su matricula del siguiente periodo es de  :",e+s+c,"%")#variables acumulados 
    print ("Gracias por su visita")

elif opcion == 2 :#salida del programa
    print("!!! Ok,Hasta pronto !!!")
print("Fin.")