#!/usr/bin/env python
#Importamos una libreria
import os

#Pedimos al usuario su usuario de linux.
nameuser=input('Introduce el nombre de tu usuario de linux: ')

#Pedimos al usuario su correo electrónico.
emailuser=input('Introduce un correo electrónico: ')

#Pedimos al usuario su usuario de gitlab.
gituser=input('Introduce tu usuario de GitLab: ')

#Pedimos al usuario que introduzca el nombre del repositorio(módulo) creado en CVS.
namerepo=input('Introduce el nombre de tu repositorio: ')

#Con esta variable evitamos la duplicación de nombre a la hora de la migración
newrepo=namerepo+'labgit'

#Modificamos el fichero de los autores introduciendo la información anterior.
fichero = open("authors-file.txt", "a")

#El texto que vamos a añadir será el siguiente 'userid=[usuario] [correo electrónico]'
fichero.write('userid=' + nameuser + ' ' + emailuser +'\n')

#Por último cerramos el fichero
fichero.close()

#Con el siguiente comando podemos crear el nuevo repositorio a partir de varias variables.
os.system('git cvsimport -C '+newrepo+' -r cvs -k -a -vA authors-file.txt -d $CVSROOT '+namerepo)

#Cambiamos el directorio de trabajo a la nueva carpeta creada
os.chdir(newrepo)

#Añadimos la ruta por SSH (previamente configurado), con el nombre del usuario y el repo.
os.system('git remote add origin ssh://git@localhost:8022/' + gituser + '/' + namerepo + '.git')

#Por útlimo hacemos un push de todo y otro push a los tags.
os.system('git push -u origin --all && git push -u origin --tags')

