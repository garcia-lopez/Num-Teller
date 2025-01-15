from os import system
from positivo import *
from negativo import *
from punto import *
from error import *
from tkinter import messagebox

def digitar_numero(numero):
    while True:
        lista_num = list(limpiar_numero(numero))  # Convierte el número en una lista para que sea más fácil de manejar
        if numero.isalpha() == True:
            error()
        elif lista_num[0] == "-" and lista_num[1].isdigit() == True and lista_num[1] != "0" and not "." in lista_num:  # Comprueba si el número es negativo, el primer elemento de la lista sería "-" y el segundo sería un número
            num = principal_negativo(lista_num)
            return num
        elif lista_num[0] == "-" and lista_num[1] == "0":  # Mensaje de error en caso que ingrese un número negativo con 0
            return None
        elif "." in lista_num:  # Comprueba si el número tiene punto decimal
            num = principal_decimal(limpiar_numero(numero))
            return num
        else:
            num = principal_positivo(lista_num)
            return num
           
