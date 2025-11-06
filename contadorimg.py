# importacion de la libreria operating system
import os

# ruta principal donde se encuentran las carpetas con imagenes
ruta_principal = r"C:\clases\Imagenes"

# extensiones de imagen comunes
extensiones = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.tiff', '.bmp') 

# contador total de imagenes
total_imagenes = 0

# recorrer todas las carpetas y subcarpetas en la ruta principal
for carpeta, subcarpetas, archivos in os.walk(ruta_principal):
    cantidad_imagenes = sum(
        1 for archivo in archivos if archivo.lower().endswith(extensiones)
    )
    if cantidad_imagenes > 0:
        print(f"{os.path.basename(carpeta)} = {cantidad_imagenes} imagenes")
        total_imagenes += cantidad_imagenes

print("Total de imágenes en todas las carpetas:", total_imagenes)