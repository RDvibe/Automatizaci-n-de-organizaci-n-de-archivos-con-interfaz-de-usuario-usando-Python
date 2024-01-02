import os
import shutil
import sys
import tkinter as tk
from tkinter import filedialog

def organizar_archivos():
    descargas_dir = filedialog.askdirectory()
    if descargas_dir:
        try:
            estado.set("Organizando archivos...")
            ventana.update()  # Actualizar la ventana para mostrar el mensaje de estado
            
            # Carpeta para otros tipos de archivos
            otros_dir = 'Varios'
            
            # Recorre los archivos en el directorio en cuestión
            for filename in os.listdir(descargas_dir):
                if os.path.isfile(os.path.join(descargas_dir, filename)):
                    # Obtiene la extensión del archivo
                    ext = os.path.splitext(filename)[1]
                    
                    # Si la extensión no está en el diccionario, solicitar al usuario el nombre de la carpeta
                    if ext not in extensiones:
                        # Verificar si se está ejecutando como un ejecutable o en un entorno de desarrollo
                        if getattr(sys, 'frozen', False):  # Verificar si está congelado (ejecutándose como un ejecutable)
                            carpeta_personalizada = input(f"Ingrese el nombre de la carpeta para el formato {ext}: ")
                        else:  # Entorno de desarrollo
                            carpeta_personalizada = tk.simpledialog.askstring("Carpeta Personalizada", f"Ingrese el nombre de la carpeta para el formato {ext}:")
                        
                        extensiones[ext] = carpeta_personalizada
            
                    # Mueve el archivo a la carpeta correspondiente o a "Varios"
                    if ext in extensiones:
                        target_dir = os.path.join(descargas_dir, extensiones[ext])
                    else:
                        target_dir = os.path.join(descargas_dir, otros_dir)
            
                    # Crea la carpeta si no existe
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
            
                    # Mueve el archivo a la carpeta
                    shutil.move(os.path.join(descargas_dir, filename), os.path.join(target_dir, filename))
            
            estado.set("Organizado con éxito.")
        except Exception as e:
            estado.set("Error al organizar archivos: " + str(e))

# Crear una ventana
ventana = tk.Tk()
ventana.title("Organizador de Archivos")
ventana.configure(bg="black")  # Establecer fondo negro

# Botón para abrir el cuadro de diálogo de selección de directorio
boton = tk.Button(ventana, text="Seleccionar Directorio", command=organizar_archivos, bg="black", fg="white", relief="raised", padx=30, pady=5, bd=3)  # Personalizar botón
boton.pack(pady=20)

# Texto de instrucciones
fuente_instrucciones = ("Arial", 12)  # Cambia la fuente y el tamaño según tus preferencias
instrucciones = tk.Label(ventana, text="""¡Bienvenido al Organizador de Archivos!

Este programa te permite organizar de manera fácil y rápida tus archivos en carpetas específicas según su extensión. Simplemente elige el directorio que deseas organizar, y el programa se encargará de clasificar automáticamente los archivos en las carpetas correspondientes.

Extensiones Organizadas:
- .txt: Archivos_TXT
- .png: Imágenes_PNG
- .jpg: Imágenes_JPG
- .exe: Ejecutables
- .pdf: Archivos_PDF
- .doc: Documentos
- .docx: Documentos
- .html: Páginas_web
- .py: Archivos_Python

¿Tu extensión no está en la lista? No hay problema. Puedes añadir manualmente nuevas extensiones y asignarles una carpeta específica. Personaliza tu organización como desees.""", fg="white", bg="black", font=fuente_instrucciones, justify="left", wraplength=400)
instrucciones.pack(pady=20)

# Variable de estado
estado = tk.StringVar()
estado.set("")  # Inicialmente, no se muestra ningún mensaje de estado

# Etiqueta para mostrar el estado
etiqueta_estado = tk.Label(ventana, textvariable=estado, fg="white", bg="black")
etiqueta_estado.pack()

# Diccionario de extensiones y nombres de carpetas por defecto
extensiones = {
    ".txt": "Archivos_TXT",
    ".png": "Imágenes_PNG",
    ".jpg": "Imágenes_JPG",
    ".JPG": "Imágenes_JPG",
    ".exe": "Ejecutables",
    ".pdf": "Archivos_PDF",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".html": "Páginas_web",
    ".py": "Archivos_Python"
}

# Función para agregar una extensión personalizada
def agregar_extension():
    ext = entrada_extension.get()
    carpeta = entrada_carpeta.get()
    extensiones[ext] = carpeta
    entrada_extension.delete(0, tk.END)
    entrada_carpeta.delete(0, tk.END)

# Etiqueta y entrada para la extensión personalizada
lbl_extension = tk.Label(ventana, text="Extensión:", fg="white", bg="black")
lbl_extension.pack()
entrada_extension = tk.Entry(ventana, width=30)
entrada_extension.pack()

# Etiqueta y entrada para el nombre de la carpeta personalizada
lbl_carpeta = tk.Label(ventana, text="Nombre de la carpeta:", fg="white", bg="black")
lbl_carpeta.pack()
entrada_carpeta = tk.Entry(ventana, width=30)
entrada_carpeta.pack()

# Botón para agregar la extensión personalizada
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_extension, bg="black", fg="white", relief="raised", padx=10, pady=5, bd=3)
boton_agregar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()