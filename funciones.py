from datos import *

def digitos(numero):
    digitos = len(numero) #cuenta la cantidad de digitos que tiene la cadena de numeros
    return digitos

def limpiar_numero(numero): #Funcion para limpiar el numero
    numero_limpio = numero.replace(",","") #Elimina las comas de la cadena
    return numero_limpio
    
def obtener_unidades(numero): #Funcion que recibe un numero y retorna su nombre en caso de ser unidad
    return dic_unidades[numero]

def obtener_decenas_nombres(numero): #Funcion que recibe un numero y retorna su nombre en caso de ser decena y termina en 0
    for num in dic_decenas_nombres.keys(): #itera sobre las llaves del diccionario
        if num == numero: #Si la llave es igual al numero
            return dic_decenas_nombres[num] #retorna el valor de la llave
        
def obtener_centenas_nombres(numero): #Funcion que recibe un numero y retorna su nombre en caso de ser centena y termina en 0
    for num in dic_centena_nombres.keys():
        if num == numero:
            return dic_centena_nombres[num]

def obtener_nombres_especiales(numero): #Funcion que recibe un numero y retorna su nombre en caso de ser un numero especial
    for num in dic_num_nombres_especiales.keys():
        if num == numero:
            return dic_num_nombres_especiales[num]
        
def obtener_miles_nombres(numero): #Devuelve el primer numero mas mil 
    if numero == "1":
        return "MIL"
    else:
        num = obtener_unidades(numero)
        return num + " MIL"
    
def ob_miles_nombres_cardinales(cardinal):
    num = cardinal[0] + cardinal[1]#Obtiene el primer y segundo digito del numero para encontrar una llave que haga match en el diccionario
    cardinal_nom = obtener_decenas(num)
    return cardinal_nom + " MIL"

def ob_miles_nombres_numeros_compuestos(compuesto):
    num = compuesto[0] + compuesto[1]#Obtiene el primer y segundo digito del numero para encontrar una llave que haga match en el diccionario
    compuesto_nom = obtener_decenas(num)
    if compuesto.count("0") < 3: #Si el numero tiene menos de 3 ceros
        cientos = obtener_numeros_restantes([compuesto[2],compuesto[3],compuesto[4]])
        return compuesto_nom + " MIL "+ cientos
    else:
        return compuesto_nom + " MIL"
    
def obtener_numeros_restantes(numeros):
    if numeros[0] == "0" and numeros[1] == "0": 
       unidades = obtener_unidades(numeros[2])
       return unidades
    elif numeros[0] == "0" and numeros[1] != "0":
        centenas = obtener_decenas([numeros[1],numeros[2]])
        return centenas
    else:
        cientos = obtener_centenas(numeros)
        return cientos
    
def obtener_miles_cardinales(Lista_numero): #funcion para obtener los miles en caso de ser cardinales
    if Lista_numero[1] == "0" and Lista_numero[2] == "0" and Lista_numero[3] == "0" and Lista_numero[4] == "0":
        return ob_miles_nombres_cardinales(Lista_numero)
    elif Lista_numero[1] != "0":
        if Lista_numero[2] != "0":
             miles = ob_miles_nombres_numeros_compuestos(Lista_numero)
             return miles
        else:
            return ob_miles_nombres_numeros_compuestos(Lista_numero)
    elif Lista_numero[1] == "0":
        miles = ob_miles_nombres_cardinales(Lista_numero)
        cientos = obtener_numeros_restantes([Lista_numero[2],Lista_numero[3],Lista_numero[4]])
        return miles + " "+ cientos

        
def obtener_decenas(Lista_numero):
    if Lista_numero[1] == "0":
        decena = obtener_decenas_nombres(Lista_numero[0])
        return decena
    elif Lista_numero[0] == "1":
        if Lista_numero[1] in ["1","2","3","4","5"]:
            decena = obtener_nombres_especiales("".join(Lista_numero))
            return decena
        else:
            unidad = obtener_unidades(Lista_numero[1])
            return "DIECI"+ unidad    
    elif (Lista_numero[0] == "2"):
          for num in dic_unidades.keys():
              if str(num) == Lista_numero[1]:
                  return "VEINTI"+ dic_unidades[num]     
    else:
        return obtener_decenas_nombres(Lista_numero[0]) + " Y " + obtener_unidades(Lista_numero[1])
    
def obtener_centenas(lista_numero): # si un numero tiene de 3 digitos entra a esta funcion
    if "".join(lista_numero) == "100": # si el numero es 100 retorna 100
        return "CIEN"
    elif lista_numero[1] == "0" and lista_numero[2] == "0": # si el segundo y tercer digito son 0, se llama a la funcion obtener centenas_nombres
        centena = obtener_centenas_nombres(lista_numero[0])
        return centena
    elif lista_numero[1] == "0" and lista_numero[2] != "0": 
        u = obtener_unidades(lista_numero[2])
        return obtener_centenas_nombres(lista_numero[0]) + " "+ u
    elif lista_numero[1] != "0":
        d = [lista_numero[1], lista_numero[2]]
        numero = obtener_decenas(d)
        return obtener_centenas_nombres(lista_numero[0]) + " "+ numero
    
def obtener_miles(Lista_numero): #Funcion para obtener los miles
    if Lista_numero[1] == "0" and Lista_numero[2] == "0" and Lista_numero[3] == "0":
       return obtener_miles_nombres(Lista_numero[0])
    elif Lista_numero[1] == "0" and Lista_numero[2] == "0" and Lista_numero[3] != "0":
       miles = obtener_miles_nombres(Lista_numero[0])
       unidad = obtener_unidades(Lista_numero[3])
       return miles + " "+ unidad
    elif Lista_numero[1] == "0" and Lista_numero[2] != "0":
        miles = obtener_miles_nombres(Lista_numero[0])
        decenas_Lista = [Lista_numero[2], Lista_numero[3]]
        decena = obtener_decenas(decenas_Lista)
        return miles + " "+decena
    elif Lista_numero[1] != "0":
        miles = obtener_miles_nombres(Lista_numero[0])
        centena = [Lista_numero[1],Lista_numero[2], Lista_numero[3]]
        centenas = obtener_centenas(centena)
        return miles+ " " + centenas
            