import time
from os import system
from funciones import *
from error import *

def principal_negativo(lista_num):
        i = lista_num.index("-") #Obtener el indice del simbolo "-"
        lista_num.pop(i) #Eliminar el simbolo "-" de la lista
        num = "".join(lista_num) #concatenar la cadena luego de eliminar "-" para obtener el numero
        dig = digitos(num)     
        if dig == 1: #Si el numero tiene 1 digito, es una unidad
         numero = "MENOS " + obtener_unidades(num)
         return numero  
        elif dig == 2: #Si el numero tiene 2 digitos, tiene decenas y unidades
         numero = "MENOS " + obtener_decenas(lista_num)
         return numero
        elif dig == 3: #Si el numero tiene 3 digitos, tiene centenas, decenas y unidades
         numero = "MENOS " + obtener_centenas(lista_num)
         return numero
        elif dig == 4: #Si el numero tiene 4 digitos, tiene miles, centenas, decenas y unidades
         numero = "MENOS " + obtener_miles(lista_num)
         return numero
        elif dig == 5: #Si el numero tiene 5 digitos, tiene miles, centenas, decenas y unidades, pero en caso de ser cardinales
         numero = "MENOS " + obtener_miles_cardinales(lista_num)
         return numero
        elif dig == 6:
            pass
        else:
            return 2