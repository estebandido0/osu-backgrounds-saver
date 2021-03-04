import os
from shutil import copy
from PIL import Image
import sys

def isPanoramic(ruta):
    """
    Devuelve True si es que la imagen tiene altura de al menos 720 pixeles y
    su relacion de aspecto es aproximada a 16:9
    """
    with Image.open(ruta) as img:
        anchura, altura = img.size

    # Fija resolucion minima y establece relacion aprox de 16:9
    if (0.4625 < altura/anchura < 0.6625 and altura >= 720 ): 
        return True
    else:
        return False

# Revisa si se encuentra en la carpeta correcta.
if (not os.path.exists('./Songs')):
    sys.exit("No se encuentra la carpeta /Songs (contiene los beatmaps descargados).\nAsegurate de correr el programa en en mismo directorio que \"osu!.exe\"")


# Crea la carpeta en donde se almacenaran los fondos
try:
    os.mkdir('./Backgrounds')
except OSError:
    sys.exit("No se pudo crear la carpeta \"/Backgrounds\" \nPorvafor revisa que no exista una carpeta con ese nombre en el directorio de osu!")


k = 1 # Contador para evitar que se sobreescriban imagenes

try:
    for subdir, dirs, files in os.walk('./Songs'):
        for file in files:
            ruta = os.path.join(subdir, file) # Ruta relativa del archivo

            # Solo considera archivos en el primer directorio
            if (ruta.count("\\") >= 3):
                continue

            
            # Para todos los archivos con extension de imagen...
            if (ruta.endswith(".jpg") or ruta.endswith(".jpeg") or ruta.endswith(".png")):
                
                extension = ruta[ruta.find(".",-5):] # Guarda la extension del archivo
                
                #filtro de imagenes panoramicas y de resolucion alta (altura >= 720)
                if (isPanoramic(ruta) == False):
                    continue

                # Muestra que archivo se está guardando
                print(os.path.join(subdir, file))

                # Guarda la imagen y la renombra
                copy(ruta,'./Backgrounds/')
                os.rename(os.path.join('./Backgrounds', file), "./Backgrounds/fondo"+str(k)+extension)
                k = k+1
except OSError:
    sys.exit("Algo salio mal... \nAsegurate de cumplir todos los pasos en el repositorio del script.")

print("Terminado!!\nSe guardaron " + str(k-1) + " imagenes en la carpeta \"/Backgrounds\"")