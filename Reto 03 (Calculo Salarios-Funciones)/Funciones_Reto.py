#Funciones y Calculos Reto.No.04 
def sueldo_bruto (hora_lab,valor_hora,lim_ext):
    if hora_lab > lim_ext :# Condicion si el docente labora mas de 40 Hrs
        sueldo=( lim_ext * valor_hora ) + (((hora_lab - lim_ext) * 1.5) * valor_hora)
        return sueldo
    else:#Condicion si el docente labora entre 1 hora a 40 horas
        sueldo = valor_hora * hora_lab 
        return sueldo 
def parafiscales (paraf):#Condicion para calcular descuento parafiscales
    parafis = paraf * 0.09
    return parafis
def salud1 (salud):#Condicion para calcular descuento salud
    dcto_salud = salud * 0.04
    return dcto_salud
def pension1 (pension):#Condicion para calcular descuento Pension
    dcto_pension1 = pension * 0.04
    return dcto_pension1
def sueldo_neto1 (sueldo_bru, salud, pension ):#Condicion para calcular Sueldo Neto
    sueldo_neto = sueldo_bru - (salud + pension)
    return sueldo_neto
def prov_prima1(pro_prima):#Condicion para calcular provision prima
    prima = pro_prima * 0.0833
    return prima
def prov_cesantias1 (cesan):#Condicion para calcular provision cesantias
    cesantias = cesan * 0.0833
    return cesantias
def int_cesantias1 (int_cesan):#Condicion para calcular provision int de cesantias
    int_cesantias = int_cesan * 0.01
    return int_cesantias
def vacaciones1 (vacac):#Condicion para calcular provision por vacaciones
    vacaciones = vacac * 0.0417
    return vacaciones
