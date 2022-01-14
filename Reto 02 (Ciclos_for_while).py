listadias=[]
opcion1="si" 
Nombre= input("Buen dia, digite su nombre : ");#inicio de conversacion 
Apellido=input("Digite su apellido : ") 
print("Hola",Nombre,Apellido);#ingreso de de datos (Nombre y apellido )
#Ingreso de temperaturas y lectura de dias (Contador)
while opcion1=="si" or opcion1=="Si" or opcion1=="SI":
    dia=(input("Ingrese el dia de las tomas de temperaturas :"))
    tempmax=int(input("Primera toma (MAX) : "))
    tempmin=int(input("Segunda toma (MIN) : "))
    listadias.append((dia,tempmax,tempmin))
    opcion1=input("Desea ingresar otro dato ? ")
print("")
print("Longitud de la lista :",len(listadias))
#Contador de lecturas erroneas de temperaturas maximas. 
contmax=0
for i in range(len(listadias)):
    if (listadias[i][1]) > 35:
        contmax=contmax+1
        print("")
#Contador de lecturas erroneas de temperaturas minimas. 
contmin=0
for i in range(len(listadias)):
    if (listadias[i][2]) < 5 :
        contmin=contmin+1
        print("")
#Contador de lecturas erroneas de temperaturas para MAX & MIN.
contadortotal=0
cont_min=0
promedio_max=0
promedio_min=0
totalmin =0
totalmax =0
for i in range(len(listadias)):
    if (listadias[i][1]) > 35 and (listadias[i][2]) < 5 :
        contadortotal=contadortotal+1
        print("")
    else:
        totalmax = totalmax + (listadias[i][1])
        totalmin = totalmin + (listadias[i][2])
        cont_min = cont_min + 1
        promedio_max = totalmax / cont_min
        promedio_min = totalmin / cont_min
#Contador de cantidadde dias con errores 
contador_error =0
porcetaje_error=0
for i in range(len(listadias)):
    if (listadias[i][1]) > 35 or (listadias[i][2]) < 5 :
        contador_error = contador_error +1
        print("____________________________________")
porcetaje_error = contador_error / (len(listadias)) * 100
media_max = round(promedio_max, 2)
media_min = round(promedio_min, 2)
print("")
#LISTA DE RESULTADOS.   
print("")
print(Nombre,Apellido,"Los dias con ERROR:(Temperatura Minimo) son : ", cont_min)
print("")
print(Nombre,Apellido,"Los dias con ERROR:(Temperatura Minimo) son : ", contmax)
print("")
print(Nombre,Apellido,"Los dias con ERROR :Para Temperaturas MAX & MIN con error son: ", contadortotal)
print("")
print(Nombre,Apellido,"Los dias total erroneos son: ", contador_error)
print("")
print(Nombre,Apellido,"PROMEDIO DE TEMPERATURA MAXIMA (MEDIA): ", promedio_max)
print("")
print(Nombre,Apellido,"PROMEDIO DE TEMPERATURA MINIMA (MEDIA):", promedio_min)
print("")
print(Nombre,Apellido,"El porcentaje errpneo de los datos ingrados por dias es del ", porcetaje_error, "%")
print("")
print("Gracias")
print("__________________________________________________________________________________________________________")
