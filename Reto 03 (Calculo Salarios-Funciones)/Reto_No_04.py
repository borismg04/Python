import Funciones_Reto as freto #iMPORTACION 

ops="si" #DEFINICION DE WHILE 

while ops=="si" or ops=="SI" or ops=="Si":#BUCLE PARA CONTINUAR INGRESANDO DOCENTES LN:44
    
    Nombre = input("Bienvenido El departamento de Talento Humano de la Universidad El Bosque, digite su Nombre Apellido: ")#Introduccion al programa ingresar nombre
    horas_laboradas=int(input("Ingrese la cantidad de horas laboradas: "))#ingreso de horas laboradas 
    lim_extra=40
    valor_hora =int(input("Ingrese el valor de hora laborada : "))#ingreso de valor de hora laborada 
    #importacion de condiciones y funciones para los calculos del programa
    sueldo_bruto1 = freto.sueldo_bruto(horas_laboradas,valor_hora,lim_extra)
    dcto_parafiscales1=freto.parafiscales(sueldo_bruto1)
    dcto_salud=freto.salud1(sueldo_bruto1)
    dcto_pension=freto.pension1(sueldo_bruto1)
    sueldo_neto = freto.sueldo_neto1(sueldo_bruto1,dcto_salud,dcto_pension)
    prov_prima = freto.prov_prima1(sueldo_bruto1)
    prov_cesantias=freto.prov_cesantias1(sueldo_bruto1)
    prov_intcesantias=freto.int_cesantias1(sueldo_bruto1)
    vacaciones=freto.vacaciones1(sueldo_bruto1)
    #RESULTADOS
    print("")
    print("------SUELDO BRUTO------")
    print("")
    print(Nombre,"Su Sueldo Bruto es : $", sueldo_bruto1)
    print("")
    print("-------DESCUENTO-------")
    print("")
    print(Nombre,"El descuento por Parafiscales segun su Sueldo Bruto es : $", dcto_parafiscales1)
    print(Nombre,"El descuento de Salud segun su Sueldo Bruto es : $",dcto_salud)
    print(Nombre,"El descuento de Pensionb segun su Sueldo Bruto es : $",dcto_pension)
    print("")
    print("------SUELDO NETO------")
    print("")
    print(Nombre,"Su Sueldo Neto es : $", sueldo_neto)
    print("")
    print("------PROVISIONES------")
    print("")
    print(Nombre,"Su provision por prima es : $",prov_prima)
    print(Nombre,"Su provision por cesantias es : $",prov_cesantias)
    print(Nombre,"Su provision por interes de cesantias es : $",prov_intcesantias)
    print(Nombre,"Su provision por vacaciones es : $",vacaciones)
    print("")
    ops = input("Desea ingresar otro docente digite (SI) de lo contrario digite (NO):")#BUCLE PARA CONTINUAR INGRESANDO DOCENTES
    print("")
print("GRACIAS POR SU VISITA , HASTA PRONTO ")

    





