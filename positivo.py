# Descripcion: Este archivo contiene la función principal_positivo, 
# la cual se encarga de llamar a las funciones que se encargan de obtener: 
# las unidades, decenas, centenas y miles de un número, dependiendo de la cantidad de dígitos que tenga el número.
from funciones import *

def principal_positivo(lista_num): 
     dig = digitos(lista_num)   
     if dig == 1: #Si el numero tiene 1 digito, es una unidad
        numero = obtener_unidades("".join(lista_num))
        return numero  
     elif dig == 2: #Si el numero tiene 2 digitos, tiene decenas y unidades
        numero = obtener_decenas(lista_num)
        return numero
     elif dig == 3: #Si el numero tiene 3 digitos, tiene centenas, decenas y unidades
        numero = obtener_centenas(lista_num)
        return numero
     elif dig == 4: #Si el numero tiene 4 digitos, tiene miles, centenas, decenas y unidades
        numero = obtener_miles(lista_num)
        return numero
     elif dig == 5: #Si el numero tiene 5 digitos, tiene miles, centenas, decenas y unidades, pero en caso de ser cardinales
        numero = obtener_miles_cardinales(lista_num)
        return numero
     else:
        return 2