#!/usr/bin/env python
from os import system
from os import chdir
from os import getcwd

#Primero pedimos al usuario 
carpeta=(input('Introduce el nombre de la carpeta de tu proyecto: '))
repocvs=(input('Introduce el nombre de un repositorio para CVS: '))
#Creamos la carpeta
system('mkdir ' + carpeta)
#Nos movemos a la carpeta
chdir(carpeta)
print(getcwd())
#Iniciamos el repositorio con CVS
system('cvs import -m "First Commit" ' + repocvs + ' David V0_1')
# #Añade todo el contendio de la carpeta
system('cvs checkout ' + repocvs)
#Nos movemos hacia la nueva carpeta
chdir(repocvs)
#Creamos un fichero con contendido
system('echo "Este repo esta hecho a partir de un script" > contenido.txt')
#Añadimos dicho archivo al estado del cvs
system('cvs add contenido.txt ')
#Hacemos un commit con el archivo creado.
system('cvs commit -m "Nuevo contenido"')
#Modificamos el archivo para tener varios commits en el repositorio.
system('echo "Este repositorio esta hecho a partir de un script en python" >> contenido.txt')
#Por último hacemos el commit para tener los últimos cambios
system('cvs commit -m "Modificiacion del contenido.txt" ')
