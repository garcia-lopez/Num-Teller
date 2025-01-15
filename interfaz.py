from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from nuevo_numero import * #importar la funcion digitar_numero

ventana = Tk() #Creacion de la ventana
ventana.title("Num-Teller")
ventana.resizable(False, False) #bloquear el tamaño de la ventana
ventana.geometry("410x500")
ventana.iconbitmap("calculadora_ico.ico") #icono de la app
# Establecer el color de fondo a rosado
ventana.configure(bg="pink",borderwidth=5, relief="groove" )
#Variables()
numero = StringVar() # Variable para almacenar el número ingresado
resultado = StringVar()  # Variable para almacenar el resultado de la conversión a palabras

def agregar_coma(num, numero_actual):  # Función para agregar una coma
    numero.set(numero_actual + str(num))
    sin_comas = numero_actual.replace(",", "")  # Quitar las comas para contar los dígitos numéricos solamente
    lista_sin_comas = list(sin_comas)
    if len(numero_actual) >= 1 and numero_actual.startswith("0"):  # Verificar si el número comienza con "0" pero no es solo "0"
      #se utiliza para verificar si una cadena comienza con el prefijo especificado. 
      # Este método devuelve True si la cadena comienza con el prefijo y False en caso contrario.
      messagebox.showerror("Error", "Número no válido")
      limpiar()

    elif len(sin_comas) == 4:  # Agrega una coma después de dos dígitos
        lista = list(sin_comas) # Convertir la cadena en una lista
        lista.insert(2, ",") # Insertar una coma en la posición 2
        coma = "".join(lista) # Convertir la lista en una cadena
        return coma + str(num) # Retornar la cadena con la coma y el número

    elif len(sin_comas) == 3:  # Agrega una coma en caso de que el número sea 2,000 por ejemplo
        lista = list(sin_comas) #convertir la cadena en una lista
        lista.insert(1, ",") #insertar una coma en la posicion 1
        coma = "".join(lista) #convertir la lista en una cadena
        return coma + str(num)  #retornar la cadena con la coma y el numero
    
    elif len(sin_comas) == 5: # Agrega una coma después de tres dígitos, en caso de ser 100,000 por ejemplo
        lista = list(sin_comas)
        lista.insert(3, ",")
        coma = "".join(lista)
        return coma + str(num)

    elif len(sin_comas) > 6: # Agrega una coma después de cada tres dígitos, si el numero tiene más de 6 digitos
        numero.set("")  # Limpiar el Entry de números
        numero_con_comas = ""
        for i, digito in enumerate(sin_comas[::-1], start=1): #Explicacion más abajo
            numero_con_comas = digito + numero_con_comas  # Agregar el dígito actual al inicio de la cadena
            if i % 3 == 0 and i != len(sin_comas):  # Si el dígito actual es el tercero y no es el último
                numero_con_comas = "," + numero_con_comas  # Agregar una coma después del tercer dígito
        return numero_con_comas + str(num) # Agregar el dígito actual al final de la cadena
    else:
        return numero_actual + str(num) # Agregar el dígito actual al final de la cadena
    
def numero_negativo(lista_numero): #funcion para verificar si el numero es negativo
   if lista_numero and lista_numero[0] == "-": # si la lista no está vacía y el primer elemento es "-"
        lista_numero.pop(0) #eliminar el simbolo "-" de la lista
        numero_actual = "".join(lista_numero) #concatenar la lista para obtener el numero
        return numero_actual #retornar el numero

def agregar_numero(num):  # función para agregar números en la caja de texto
    try:
        numero_actual = str(numero.get())
        numero.set(numero_actual + str(num))
        lista = list(numero_actual)
        
        if "-" in lista:  # verificar si el número es negativo 
            if lista.index("-") == 0:  # verificar si el signo negativo está en la primera posición para evitar restas
                lista_numero = numero_negativo(lista)
                numero.set("")
                numeros = agregar_coma(num, lista_numero)
                numero.set("-" + numeros)
            else:
                messagebox.showerror("Error", "No se admiten restas")
                limpiar()
        elif "." in lista:  # verificar si el número tiene punto decimal
            parte_entera, parte_decimal = numero_actual.split(".")  # separar la parte entera de la parte decimal
            numero.set('')  # limpiar la caja de texto
            total = parte_entera + "." + parte_decimal  # concatenar la parte entera con la parte decimal
            numero.set(total + str(num))  # mostrar el resultado en la caja de texto

        elif "." in lista and "-" in lista:  # verificar si el número es negativo y tiene punto decimal
            parte_entera, parte_decimal = numero_actual.split(".")  # separar la parte entera de la parte decimal
            total = "-" + parte_entera + "." + parte_decimal  # concatenar la parte entera con la parte decimal y el signo negativo
            numero.set(" ")
            numero.set(total + str(num))  # mostrar el resultado en la caja de texto  
        else:
            numeros = agregar_coma(num, numero_actual)
            if numeros is not None: #si el numero es diferente de None
                numero.set(numeros) #mostrar el numero en la caja de texto
    except Exception as e:
        messagebox.showerror("Error", "Número no válido")

       
def agregar_especial(especial): #funcion para agregar caracteres especiales
    numero_actual = str(numero.get())
    numero.set(numero_actual + str(especial))

def limpiar(): #funcion para limpiar las cajas de texto
    numero.set("")
    resultado.set("")
    
def calcular():  # función para calcular el número ingresado
    try:
        num = numero.get()  # obtener el número ingresado 
        palabras = digitar_numero(num)  # llamar a la función digitar_numero 
        if palabras == 2:
            messagebox.showinfo("Información", "Número no válido todavía, estamos trabajando en ello.")
            limpiar()
        elif palabras is None:
            error()
            limpiar()
        else:
            resultado.set(palabras)  # llamar a la función digitar_numero y mostrar el resultado en la caja de texto
    except Exception as e:
        messagebox.showerror("Error", "Número no válido")
        limpiar()


    
#Componentes
#Darle estilo a la etiqueta de la app
estilo_etiqueta = Style()
estilo_etiqueta.configure("Fondo.TLabel",background="pink", foreground="#192841", font=("Roboto", 15, "bold"))

#Darle estilo a la etiqueta de numeros y resultado
decorador = Style()
decorador.configure("Decorador.TLabel",background="#3C3839", foreground="#5B524B", font=("Roboto", 15, "bold"))

#Darle estilo a los botones
#Estilo para los botones
estilo = Style() #crear objeto de estilo
estilo.configure("TButton", font=("Roboto", 15), bg='pink', fg='#5B524B')# padding, Se establece el relleno interno de los botones. Esto afecta al espacio dentro del botón alrededor del texto.
#cambios que ocurriran cuando el mouse este sobre el boton
estilo.map("TButton",foreground= [("active","!disabled","pink")],background=[('active', 'pink')]) # Con el método map(), se definen los cambios que ocurrirán cuando el mouse esté sobre los botones.
#foreground: Define el color del texto cuando el botón está en estado activo ("active") y no está desactivado ("!disabled"). En este caso, el color del texto se establece en verde ("green").
#background: Define el color de fondo cuando el botón está en estado activo ("active"). En este caso, el color de fondo se establece en negro ("black").
# cada botón que creado después de configurar el estilo "TButton" heredará automáticamente 
# las propiedades de estilo definidas en ese estilo, como la fuente, el relleno y los colores, 
# sin necesidad de especificar el parámetro style al crearlos.

#etiquetas
Lbl1 = Label(ventana, text="NUM-TELLER",style="Fondo.TLabel", justify="center") #nombre de la app
Lbl1.place(x=18, y=15)
LblDeco = Label(ventana ,text=" |  |  |  |  |  |",style="Decorador.TLabel")#decorador de carga solar
LblDeco.place(x=259, y=15, width=110, height=27)

#Etiqueta para el ingreso de numeros
Lbl2 = Label(ventana, text="Número :",style="Fondo.TLabel") # etiqueta de caja de texto numeros
Lbl2.place(x=18, y=60)

#Etiqueta para el resultado
Lbl3 = Label(ventana, text="Palabras :",style="Fondo.TLabel") # etiqueta de caja de texto palabras
Lbl3.place(x=10, y=100)

#Cajas de texto
Entry(ventana, textvariable=numero, state="readonly", justify="center", font=("Roboto", 15)).place(x=110, y=60, width=280, height=30) #caja de texto para la entrada del numero
Entry(ventana, textvariable=resultado, state="readonly", justify="center", font=("Roboto", 9)).place(x=110, y=100, width=280, height=30) #caja de texto para mostrar el resultado, es decir el numero en palabras

# Calcular las posiciones de los botones
x_start = 0
y_start = 170
button_width = 80
button_height = 40
x_spacing = 50
y_spacing = 20

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('0', 3, 0), ('.', 3, 1), ('-', 3, 2),
    ('Calcular', 4, 0), ('Limpiar', 4, 1)
]


for button_text, row, col in buttons:
    x_pos = x_start + col * (button_width + x_spacing)
    y_pos = y_start + row * (button_height + y_spacing)
    button = Button(ventana, text=button_text)
    if button_text.isdigit():
        button.config(command=lambda num=button_text: agregar_numero(num)) #si el texto del boton es un numero, se llama a la funcion agregar_numero
    elif button_text in ['.']:
        button.config(command=lambda esp=button_text: agregar_especial(esp)) #si el texto del boton es un caracter especial, se llama a la funcion agregar_especial  

    elif button_text in ['-']:  
        button.config(command=lambda esp=button_text: agregar_especial(esp)) #si el texto del boton es un caracter especial, se llama a la funcion agregar_especial  
    elif button_text == "Limpiar":
        button.config(command=limpiar)
    elif button_text == "Calcular":
        button.config(command=calcular)
    button.place(x=x_pos, y=y_pos)

ventana.mainloop()

#Explicacion de la funcion agregar_coma
# sin_comas[::-1]: Esto crea una copia invertida de la lista sin_comas.
# El [::-1] es una técnica de slicing que indica que queremos obtener una copia de la lista pero en orden invertido. 
# Esto es útil cuando se quiere iterar sobre una lista en reversa.
#enumerate(..., start=1): enumerate() es una función de Python que toma una secuencia (en este caso, la lista invertida sin_comas) 
# y la convierte en una secuencia de tuplas (índice, elemento), donde índice es el índice del elemento en la lista y elemento es el 
# elemento en sí mismo. El parámetro start=1 especifica desde qué número empezar a contar los índices.
# En este caso, los índices empezarán en 1 en lugar de en 0.
#for i, digito in ...: Este es el bucle for en sí mismo. 
# i es el índice del elemento en la lista (comenzando desde 1 debido al parámetro start=1 en enumerate()), 
# y digito es el elemento en sí mismo. Por cada iteración del bucle, i tomará el valor del índice y 
# digito tomará el valor del elemento correspondiente en la lista.

