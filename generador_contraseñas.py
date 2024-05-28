import tkinter as tk
import string
import random
import pyperclip
from tkinter import messagebox

def generar_contrasena ( longitud ):
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join ( random.choice ( caracteres ) for i in range ( longitud ) ) # Genera una cadena aleatoria de la longitud indicada
    return contrasena 

def generar_y_mostrar_contrasena ():
    longitud = longitud_entry.get () # Obtiene la longitud indicada por el usuario
    try:
        longitud = int ( longitud )
        contrasena = generar_contrasena ( longitud )
        contrasena_label.config ( text = "Tu contraseña generada es: " + contrasena )
        contrasena_copiada_button.config ( state = "normal" )
        pyperclip.copy ( contrasena )
    except ValueError:
        messagebox.showerror ( "Error", "Por favor ingresa un número válido para la longitud" )

def copiar_contrasena_al_portapapeles ():
    contrasena = contrasena_label.cget ( "text" ).split ( ": " ) [ 1 ]
    pyperclip.copy ( contrasena )

def main ():
    global longitud_entry, contrasena_label, contrasena_copiada_button

# GUI del generador de contrasenas
    root = tk.Tk ()
    root.title ( "Generador de Contraseñas" )
    root.geometry ( "425x180" )

    frame = tk.Frame ( root )
    frame.pack ( pady = 10 )

    longitud_label = tk.Label ( frame, text = "Longitud de la contraseña:" )
    longitud_label.grid ( row = 0, column = 0 )

    longitud_entry = tk.Entry ( frame )
    longitud_entry.grid ( row = 0, column = 1 )

    generar_button = tk.Button ( frame, text = "Generar Contraseña", command = generar_y_mostrar_contrasena )
    generar_button.grid ( row = 1, columnspan = 2, pady = 10 )

    contrasena_label = tk.Label ( root, text = "" )
    contrasena_label.pack ()

    contrasena_copiada_button = tk.Button ( root, text = "Copiar al Portapapeles", state = "disabled", command = copiar_contrasena_al_portapapeles )
    contrasena_copiada_button.pack ( pady = 5 )

    root.mainloop ()

if __name__ == "__main__":
    main ()
