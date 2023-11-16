### Script para analizar y relanzar aquellas trayectorias con NewtonX que hayan terminado con error. 
### Se debe ejecutar en la carpeta donde están todas las trayectorias o en su defecto cambiar el directorio principal
### Con el fin de visualizar y tener una lista con las que terminan con errores, se crea un documento con dicha info


import os
import shutil
import re


new=open(str('TRAJS_CON_ERROR.dat'),"w")

# Se define una función que será la encargada de buscar y crear una copia de las carpetas de aquellas trayectorias que tengan un error
def buscar_y_copiar_carpeta():
    # Directorio principal donde se encuentran las carpetas TRAJ
    # Si no se ejecuta desde el mismo hay que cambiar el path
    directorio_principal = './'

    # Patrón para buscar carpetas que empiezan con TRAJ y números del 1-100 (Si son más o menos hay que adecuar esto)
    patron = 'TRAJ[1-9][0-9]?|TRAJ100'

    # Buscar carpetas que coincidan con el patrón
    carpetas_encontradas = [carpeta for carpeta in os.listdir(directorio_principal) if os.path.isdir(os.path.join(directorio_principal, carpeta)) and carpeta.startswith('TRAJ') and bool(re.match(patron, carpeta))]

    # El patrón de busqueda dentro de los archivos es el que indica que las trajs han terminado con error
    texto_a_buscar = 'moldyn.pl:   ::ERROR::'

    carpetas_con_patron = []  # Para guardar las carpetas que cumplen con el patron

    for carpeta in carpetas_encontradas:
        ruta_carpeta = os.path.join(directorio_principal, carpeta)
        archivo_log = os.path.join(ruta_carpeta, 'moldin.log')

        # El archivo moldin.log existe en la carpeta actual
        if os.path.exists(archivo_log):
            with open(archivo_log, 'r') as file:
                lineas = file.readlines()
                encontrado = any(texto_a_buscar in linea for linea in lineas)

            # Si se encuentra el texto en el archivo, hacer una copia de la carpeta
            if encontrado:
                nueva_carpeta = f'{carpeta}_CP'
                ruta_nueva_carpeta = os.path.join(directorio_principal, nueva_carpeta)
                shutil.copytree(ruta_carpeta, ruta_nueva_carpeta)
                print(f'Copiada carpeta {carpeta} a {nueva_carpeta}')

                # Copiar el archivo control.dyn de la carpeta INFO_RESTART --> SE COPIA AL TRAJX_CP
                # HA DE CORRERSE LAS NUEVAS TRAYECTORIAS DESDE LAS CARPETAS CP !!!!!!!!!!!!!
                ruta_info_restart = os.path.join(ruta_carpeta, 'INFO_RESTART')
                if os.path.exists(ruta_info_restart):
                    archivo_control_dyn = os.path.join(ruta_info_restart, 'control.dyn')
                    if os.path.exists(archivo_control_dyn):
                        shutil.copy(archivo_control_dyn, os.path.join(ruta_nueva_carpeta, 'control.dyn'))
                        print(f'Copiado control.dyn desde {carpeta}/INFO_RESTART a {nueva_carpeta}')

                carpetas_con_patron.append(carpeta)  # Agregar carpeta a la lista

    print("\nCarpetas encontradas con el patrón:")
    for carpeta_patron in carpetas_con_patron:
        print(carpeta_patron)
        print(carpeta_patron,file=new)

# Ejecutar la función
buscar_y_copiar_carpeta()

