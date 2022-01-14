

#Funciones por ejecutar (Complemento)

def buscar (lineas_1):
    flag=True
    datos=open('Agenda.txt' , 'r')
    lineas=datos.readlines()
    datos.close() 
    nombre_buscar=input("Escriba el nombre que quiere buscar: ").lower().title()
    #global flag 
    cont=0
    datos=open('Agenda.txt' , 'r')
    print(" ")
    print("Los datos del usuario es : ")
    print("Nombre:",nombre_buscar)

    for linea in lineas: 
        if linea.strip("\n")==nombre_buscar or flag==False:
            cont=cont+1
            flag=False
            print(linea)
            
            if cont>2:
                flag=True

def borrar (lineas_1): 
    datos=open('Agenda.txt' , 'r')
    lineas=datos.readlines()
    datos.close() 
    doc=input('Digite el documento de la persona que desea borrar: ')
    datos=open('Agenda.txt' , 'w')
    Nombre=' '
    Telefono=' '
    Cedula=' '
    for linea in lineas:
        if linea.strip("\n")==doc:
            indice=lineas.index(linea)
            Nombre=lineas[indice-1]
            Telefono=lineas[indice+1]
            Cedula=lineas[indice]
            print("____________________________________________")
            print("El usuario ha sido eliminado de la agenda :")
            print("____________________________________________")
            print('Usuario eliminado: ' ,Nombre)
            print('Con número de documento: ' ,Cedula)
            print('Con número de telefonico: ' ,Telefono)
            print("____________________________________________")

    
    for linea in lineas:
        if linea.strip("\n") !=Nombre.strip("\n") and linea!=Telefono and linea!=Cedula:
            datos.write(linea)
            
    datos.close()



def adicionar (lineas_1):
    datos=open('Agenda.txt' , 'r')
    lineas=datos.readlines()
    datos.close()
    L=[]
    print('Ingrese los datos de la persona que desea adicionar: ') 
    Nom=input('Digite nombre completo: ').lower().title()
    L.append(Nom)
    Ced=input('Digite número de documento: ')
    L.append(Ced)
    Tel=input('Digite número de telefono: ')
    L.append(Tel)
    print("________________________________________")
    print("El nombre del usuario registrado es : ",Nom)
    print("El nel numero de documentacion del usuario es : ",Ced)
    print("El numero del usuario es : ",Tel)
    print("________________________________________")
    datos=open('Agenda.txt' , 'a')
    
    for var in L:
        datos.write(var)
        datos.write("\n")
    datos.close()        


def listar(lineas_1):
    datos=open('Agenda.txt' , 'r')
    lineas=datos.readlines()
    datos.close()
    print(' ')
    print('El listado de usuarios se muestra a continuación: ')
    print("Nombre / Cedula / Telefono")             
    print(lineas)

  
def buscar_letra():
    datos=open('Agenda.txt' , 'r')
    lineas=datos.readlines()
    datos.close() 
    #print(' ')
    letra=input('Digite la letra por la cual quiere buscar usuarios: ').lower().title()
    for cursor in lineas:
        if cursor[0]==letra:
            print("Los nombre con la letra seleccionada son :",cursor)
    datos.close()



