#importacion de documentos y librerias

import io
import funciones as fn

#Menu 
menu = ''' ----------------------------------------
Bienvenidos a la agenda de beneficiarios (Universidad el Bosque)
----------------------------------------

Por favor eliga una opcion valida.

    1 - Ingrese nuevo ususario.
    2 - Buscar usuario.
    3 - Borrar usuario.
    4 - Adicionar usuario. 
    5 - Lista de usuarios registrados.
    6 - Buscar por letra en nombre del beneficiario.
    7 - Salir.

----------------------------------------
¿ Cual es su opción?:  '''

#Lectura del archivo Agenda.txt, para su llenado.
datos=open('Agenda.txt' , 'r')
flag=True 
lineas=datos.readlines()

datos.close()

#Ingreso de datos

#Ingreso de datos al menu 

escoger = int(input(menu))
if escoger == 1:
    datos=open('Agenda.txt' , 'r+')
    datos.close()
    cantidad= int(input("Digite No. de usuarios que desea ingresar: "))
    for i in range (cantidad):
        L=[]
        print('\nBeneficiario N°', i+1)
        nombre=input("Digite nombre completo: ").lower().title()
        L.append(nombre)
        documento=input("Digite el número de documento: ")
        L.append(documento)
        celular=input("Digite el número de celular: ")
        L.append(celular)
        print("________________________________________")
        print("El nombre del usuario registrado es : ",nombre)
        print("El nel numero de documentacion del usuario es : ",documento)
        print("El numero del usuario es : ",celular)
        print("________________________________________")

        datos=open('Agenda.txt' , 'a')
        for variable in L:
            datos.write(variable)
            datos.write("\n")
        datos.close()     

#Funciones Menu.
while True:
    escoger = int(input(menu))
    if escoger==2: 
        busqueda=fn.buscar(lineas)
    
    elif escoger==3:
        borrado=fn.borrar(lineas)

    elif escoger==4:
        adicion=fn.adicionar(lineas)
    
    elif escoger==5:
         lista=fn.listar(lineas)

    elif escoger==6:
        inicial=fn.buscar_letra()

    elif escoger==7:
        break