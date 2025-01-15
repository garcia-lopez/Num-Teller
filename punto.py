from funciones import *
from positivo import *  
from negativo import *

def principal_decimal(numero):
 parte_entera, parte_decimal = numero.split(".") #separar la parte entera de la parte decimal 
 
 if "-" in parte_entera: #verificar si la parte entera es negativa
     lista_entera = list(parte_entera) #convertir la parte entera en una lista
     lista_decimal = list(parte_decimal) #convertir la parte decimal en una lista
     entero = principal_negativo(lista_entera) #llamar a la funcion principal_negativo
     decimal = principal_positivo(lista_decimal) #llamar a la funcion principal_positivo
     return entero + " PUNTO " + decimal #retornar el resultado
 
 elif not "-" in parte_entera: #si la parte entera no es negativa
     lista_entera = list(parte_entera) #convertir la parte entera en una lista
     lista_decimal = list(parte_decimal) #convertir la parte decimal en una lista
     entero = principal_positivo(lista_entera) #llamar a la funcion principal_positivo
     decimal = principal_positivo(lista_decimal)
     return entero + " PUNTO " + decimal #retornar el resultado
 else:
     return 2