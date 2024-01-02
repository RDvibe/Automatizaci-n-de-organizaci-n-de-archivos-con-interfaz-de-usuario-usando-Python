# Organizador de Archivos

Este programa te permite organizar tus archivos en carpetas específicas según su extensión. Simplemente selecciona el directorio que deseas organizar, y el programa clasificará automáticamente los archivos en las carpetas correspondientes.

## Instrucciones de Uso

### 1. Instalación de Dependencias

Asegúrate de tener Python y las siguientes bibliotecas instaladas. Puedes instalarlas ejecutando:

```
pip install tk


pip install pyinstaller
```

2. Ejecución del Programa
Para ejecutar el programa, simplemente ejecuta el script organizador_archivos.py con Python:


python organizador_archivos.py
O si deseas convertirlo en un ejecutable:

```
pyinstaller --onefile organizador_archivos.py
El ejecutable estará en la carpeta dist.

```

Extensiones Organizadas
.txt: Archivos_TXT
.png: Imágenes_PNG
.jpg: Imágenes_JPG
.JPG: Imágenes_JPG
.exe: Ejecutables
.pdf: Archivos_PDF
.doc: Documentos
.docx: Documentos
.html: Páginas_web
.py: Archivos_Python

#Personalización
Para personalizar la organización, simplemente añade nuevas extensiones y asigna una carpeta específica en el diccionario de extensiones en el script.

Ejecuta el programa y utiliza la interfaz gráfica para añadir extensiones personalizadas.
