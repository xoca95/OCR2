# -*- coding: utf-8 -*-
"""
Programa: OCR
Descripcion: Obtiene caracteristicas de un conjunto de imagenes binarizadas que contienen numeros y las guarda en un archivo csv
"""
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg #importo libreria para el manejo de imagenes
import csv #importo libreria para crear archivos csv
import os #importo libreria para acceder a las carpetas con las imagenes

'''
Nombre de la funcion: rutaImagen
Descripcion: Permite obtener la ruta y el nombre de la imagen a analizar
Parametros de entrada: directorio, nombreDeImagen
Resultado: Devuelve la direccion completa del archivo
'''
def rutaImagen(directorio,nombreDeImagen):
    #directorio es la direccion de la imagen nombreDeImagen es el nombre de la imagen
    nuevaRutaImagen=directorio+'/'+nombreDeImagen #variable que permite obtener la direccion y el nombre de la imagen
    return nuevaRutaImagen #devuelvo el valor obtenido

'''
Nombre de la funcion: imagen
Descripcion: Permite leer una imagen, la cual es interpretada como una matriz
Parametros de entrada: ruta (direccion del archivo)
Resultado: Genera una matriz que representa a la imagen
'''    
def imagen(ruta):
    imagen=mpimg.imread(ruta) #se obtiene la imagen y se guarda en una variable
    return imagen #devuelvo el vaolr obtenido

'''
Nombre de la funcion: dimencionesImagen
Descripcion: obtiene el largo y el ancho de una imagen (matriz)
Parametros de entrada: imagen (matriz)
Resultado: Un  arreglo con las dimenciones de la imagen
'''
def dimencionesImagen(imagen):
    dimenciones=imagen.shape #obtengo las dimenciones de la imagen
    return dimenciones #devulevo el valor obtenido

'''
Nombre de la funcion: numeroFilas
Descripcion: obtengo la cantidad de filas total de la imagen (matriz)
Parametros de entrada: dimencion (arreglo con las dimenciones de la matriz)
Resultado: obtengo la cantida de filas en la imagen
'''    
def numeroFilas(dimencion):
    numeroEnFilas=dimencion[0] #obtengo el numero total de Filas de la imagen (largo)
    return numeroEnFilas #devuelvo el valor obtenido

'''
Nombre de la funcion: numeroColumnas
Descripcion: obtengo la cantidad de columnas total de la imagen(matriz)
Parametros de entrada: dimencion (arreglo con las dimenciones de la matriz)
Resultado: obtengo la cantidad de columnas en la imagen
'''
def numeroColumnas(dimencion):
    numeroEnColumnas=dimencion[1] #obtengo el numero total de columnas de la imagen (ancho)
    return numeroEnColumnas #devuelvo el valor obtenido

'''
Nombre de la funcion: relacionTamaño
Descripcion: calculo la relacion que existe entre la divicion de largo y ancho
Parametros de entrada:largo y ancho (numero de filas y de columnas respectivamente)
Resultado: obtengo un numero que representa la relacion largo ancho
'''
def relacionTamaño(largo,ancho):
    relacion_Tamaño=largo/ancho#relacion_Tamaño es la relacion del largo entre el ancho de la imagen
    return relacion_Tamaño #devuelvo el valor obtenido

'''
Nombre de la funcion: areaNumero
Descripcion: cuento los pixeles que representan al numero en la imagen
Parametros de entrada: filas, columnas (dimenciones) y la imagen
Resultado: La cantidad de pixeles del numero
'''
def areaNumero(Filas,Columnas,imagen):
    area_Numero=0 #variable para contar los bits del area del numero en la imagen
    for i in range(0,Filas): #for para recorrer las filas de la imagen
        for j in range(0,Columnas): #for para recorrer las columnas de la imagen
            if(imagen[i][j]!=0): #condicion para clasificar el valor del bits del numero
                area_Numero=area_Numero+1 #si se cumple aumenta el contador del area del numero en la imagen
    return area_Numero #delvuelvo el valor obtenido

'''
Nombre de la funcion: filaCentral
Descripcion: obtengo el numero de la fila ubicada en la posicion central de la imagen
Parametros de entrada: filas (filas totales)
Resultado:la fila central de la imagen
'''
def filaCentral(Filas):
    fila_central=int(Filas/2) #mitad en filas de la imagen
    return fila_central #devuelvo el valor obtenido

'''
Nombre de la funcion: columnaCentral
Descripcion: obtengo el numero de la columna ubicada en la posicion central de la imagen
Parametros de entrada: columnas (columnas totales)
Resultado:la columna central de la imagen
'''
def columnaCentral(columnas):
    columna_central=int(columnas/2) #mitad en columnas de la imagen
    return columna_central #devuelvo el valor obtenido

'''
Nombre de la funcion: filaPosicionadaEnUncuarto
Descripcion: obtengo el numero de la fila ubicada en la posicion un cuarto de la imagen
Parametros de entrada: filas (filas totales)
Resultado:la fila un cuarto de la imagen
'''
def filaPosicionadaEnUnCuarto(fila_central):
    filaUnCuarto=int(fila_central/2) #fila ubicada en un cuarto de la imagen
    return filaUnCuarto #devuelvo el valor obtenido

'''
Nombre de la funcion: filaPosicionadaEnTrescuartos
Descripcion: obtengo el numero de la fila ubicada en la posicion tres cuartos de la imagen
Parametros de entrada: filas (filas totales)
Resultado:la fila tres cuartos de la imagen
'''
def filaPosicionadaEnTresCuartos(fila_central,fila_un_cuarto):
    filaTresCuartos=fila_central+fila_un_cuarto #fila ubicada en tres cuartos de la imagen
    return filaTresCuartos #devuelvo el valor obtenido

'''
Nombre de la funcion: columnaPosicionadaEnUnCuarto
Descripcion: obtengo el numero de la columna ubicada en la posicion un cuarto de la imagen
Parametros de entrada: columnas (columnas totales)
Resultado:la columna un cuarto de la imagen
'''
def columnaPosicionadaEnUnCuarto(columna_central):
    columnaUnCuarto=int(columna_central/2) #columna ubicada en un cuarto de la imagen
    return columnaUnCuarto #devuelvo el valor obtenido

'''
Nombre de la funcion: columnaPosicionadaEntresCuartos
Descripcion: obtengo el numero de la columna ubicada en la posicion tres cuartos de la imagen
Parametros de entrada: columnas (columnas totales)
Resultado:la columna tres cuartos de la imagen
'''
def columnaPosicionadaEnTresCuartos(columna_central,columna_un_cuarto):
    columnaTresCuartos=columna_central+columna_un_cuarto #columna ubicada en tres cuartos de la imagen
    return columnaTresCuartos #devuelvo el valor obtenido

'''
Nombre de la funcion: cortesEnUnaFila
Descripcion: analizo la cantidad de veces que el numero de la imagen es cortado en una fia determinada
Parametros de entrada: fila (cualquier fila), numero_columnas (columnas totales de la imagen) y la imagen
Resultado: cortes en una fila
'''
def cortesEnUnaFila(fila,numero_columnas,imagen):
    cortesEnLaFila=0 #contador de cortes en una fila de la imagen
    auxiliar=imagen[fila][0] #variable que ayudara a comparar los cortes del numero
    for i in range(0,numero_columnas): #for i para recorrer la fila obtenida de la imagen
        if(auxiliar!=imagen[fila][i]): #condicion para verificar los cortes
            auxiliar=imagen[fila][i] #cambio de valor de aux porque encontro un corte 
            cortesEnLaFila=cortesEnLaFila+1 #aumenta el contador de los cortes en la fila obtenida de la imagen
    #fin del for i
    return cortesEnLaFila #devuelvo el valor obtenido

'''
Nombre de la funcion: pixelesDelNumeroEnUnaFila
Descripcion: permite contar los pixeles de un numero en una imagen en una fila determinada
Parametros de entrada: Fila (cualquier fila), numero_columnas (columnas totales de la imagen) y la imagen
Resultado: los pixeles correspondientes al numero en la imagen de una fila
'''
def pixelesDelNumeroEnUnaFila(fila,numero_columnas,imagen):
    pixelesDelNumeroEnFila=0 #variable para contar los pixeles del numero en una fila de la imagen
    for i in range(0,numero_columnas): #for i para recorrer la fila de la imagen
        if(imagen[fila][i]!=0): #comparacion para obtener los pixeles del numero en una fila de la imagen
            pixelesDelNumeroEnFila=pixelesDelNumeroEnFila+1 #aumenta el contador de los pixeles del numero en una fila de la imagen
    return pixelesDelNumeroEnFila #devuelvo el valor obtenido

'''
Nombre de la funcion: cortesEnUnacolumna
Descripcion: analizo la cantidad de veces que el numero de la imagen es cortado en una columna determinada
Parametros de entrada: columna (cualquier columna), numero_filas (filas totales de la imagen) y la imagen
Resultado: cortes en una columna
'''
def cortesEnUnaColumna(columna,numero_filas,imagen):
    cortesEnColumna=0 #contador de cortes en una columna de la imagen
    auxiliar=imagen[0][columna] #Variable que ayudara a  comparar los cortes
    for i in range(0,numero_filas): # for i para recorre la columna deseada de la imagen
        if(auxiliar!=imagen[i][columna]): #condicion para verificar los cortes de la imagen
            auxiliar=imagen[i][columna] #cambio de valor de aux porque encontro un corte de la imagen
            cortesEnColumna= cortesEnColumna+1 #aumenta el contador de los cortes en la columna de la imagen
    return cortesEnColumna #devuelvo el valor obtenido

'''
Nombre de la funcion: pixelesDelNumeroEnUnaColumna
Descripcion: permite contar los pixeles de un numero en una imagen en una columna determinada
Parametros de entrada: columna (cualquier columna), numero_filas (filas totales de la imagen) y la imagen
Resultado: los pixeles correspondientes al numero en la imagen de una columna
'''
def pixelesDelNumeroEnUnaColumna(columna,numero_filas,imagen):
    pixelesDelNumeroEnColumna=0 #variable para contar los bits del numero en la columna central de la imagen
    for i in range(0,numero_filas): #for i para recorrer la columna de la imagen
        if(imagen[i][columna]!=0): #comparacion para reconocer los pixeles del numero en la columna de la imagen
            pixelesDelNumeroEnColumna=pixelesDelNumeroEnColumna+1 #aumenta el contador de los pixeles del numero en la columna de la imagen
    return pixelesDelNumeroEnColumna #devuelvo el valor obtenido

'''
Nombre de la funcion: creaciondataSet
Descripcion: Manda a traer al resto de funciones para obtener las caracteristicas de la imagen y guardarla en un archivo csv
Parametros de entrada: ninguno
Resultado: un archivo csv con las caracteristicas del cunjunto de imagenes
'''
def creacionDataSet():
    archivo= open('DataSet.csv', 'w', newline='') #se abre el archivo csv o se crea si no esta creado
    salida = csv.writer(archivo) #se transfiere el archivo a esta variable para poder escribir en el
    clase=-1 #se crea la variable clase que servira para indicar a que numero pertenecen las caracteristicas obtenidas
    carpetaDeImagenes='arialSegmented' #nombre de la carpeta que contiene las imagenes
    #inicia for
    #existen 3 variables: dirName que indica el nombre del directorio principal y subcarpetas
    #subdirList que indica las subcarpetas de cada carpeta
    #fileList que proporciona una lista con los nombres de los archivos de cada carpeta
    for dirName, subdirList, fileList in os.walk(carpetaDeImagenes): #for para recorer los archivos de la carpeta principal
        #for para recorer las subcarpetas. fname es para obtener el nombre de cada imagen
        for fname in fileList: #for para obtener los nombre de las imagenes
            rutaDeLaImagen=rutaImagen(dirName,fname) #obtengo la ruta de la imagen y su nombre
            imagenNueva=imagen(rutaDeLaImagen) #genero una matriz que representa a la imagen a analizar
            dimencionesDeLaImagen=dimencionesImagen(imagenNueva) #obtengo el largo  y ancho de la imagen (matriz) y las guardo en un arreglo
            numeroDeFilas=numeroFilas(dimencionesDeLaImagen) #obtengo el numero de filas total (largo de la imagen)
            numeroDeColumnas=numeroColumnas(dimencionesDeLaImagen) #obtengo el numero de columnas total (ancho de la imagen)
            #comienzo a obtener las caracteristicas de la imagen
            #Primer caracteristica: relacion de las dimenciones de la imagen
            relacionLargoEntreAncho=relacionTamaño(numeroDeFilas,numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable relacionLargoEntreAncho
            #Segunda caracteristica: cantidad de pixeles del numero en la imagen
            areaDelNumero=areaNumero(numeroDeFilas,numeroDeColumnas,imagenNueva)#mando a traer esta funcion y la guardo en la variable areaDelNumero
            #ubico la fila central de la imagen
            FilaCentral=filaCentral(numeroDeFilas) #mando a traer esta funcion y la guardo en la variable filaCentral
            #ubico la columna central de la imagen
            ColumnaCentral=columnaCentral(numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable ColumnaCentral
            #Tercera caracteristica: cortes del numero en la fila central de la imagen
            CortesEnLaFilaCentral=cortesEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable CortesEnLaFilaCentral
            #Cuarta caracteristica: pixeles  del numero en la fila central de la imagen
            pixelesDelNumeroEnLaFilaCentral=pixelesDelNumeroEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroenLaFilaCentral
            #Quinta caracteristica: cortes del numero en la columna central de la imagen
            cortesEnLaColumnaCentral=cortesEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaCentral
            #Sexta caracteristica: pixeles del numero en la columna central de la imagen
            pixelesDelNumeroEnLaColumnaCentral=pixelesDelNumeroEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaCentral
            #ubico la fila posicionada en un cuarto de la imagen (la relacion es base a las filas)
            filaEnUnCuarto=filaPosicionadaEnUnCuarto(FilaCentral) #mando a traer esta funcion y la guardo en la variable filaEnUnCuarto
            #ubico la fila posiciona en tres Cuartos de la imagen (la relacion es base a las filas)
            filaEnTresCuartos=filaPosicionadaEnTresCuartos(FilaCentral,filaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable filaEnTresCuartos
            #ubico la columna posicionada en un cuarto de la imagen (la relacion es base a las columnas)
            columnaEnUnCuarto=columnaPosicionadaEnUnCuarto(ColumnaCentral) #mando a traer esta funcion y la guardo en la variable columnaEnUnCuarto
            #ubico la columna posicionada en tres cuartos de la imagen (la relacion es base a las columnas)
            columnaEnTresCuartos=columnaPosicionadaEnTresCuartos(ColumnaCentral,columnaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable columnaEnTresCuartos
            #Septima caracteristica: cortes del numero en la fila un cuarto de la imagen
            cortesEnLaFilaUnCuarto=cortesEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaUnCuarto
            #Octava caracteristica: pixeles del numero en la fila ubicada en un cuarto de la imagen
            pixelesDelNumeroEnLaFilaUnCuarto=pixelesDelNumeroEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaUnCuarto
            #Novena caracteristica: cortes del numero en la fila tres cuartos de la imagen
            cortesEnLaFilaTresCuartos=cortesEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaTresCuartos
            #Decima caracteristica: pixeles del numero en la fila ubicada en tres cuartos de la imagen
            pixelesDelNumeroEnLaFilaTresCuartos=pixelesDelNumeroEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaTresCuartos
            #Onceava caracteristica: cortes del numero en la columna ubicada en un cuarto de la imagen
            cortesEnLaColumnaUnCuarto=cortesEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaUnCuarto
            #Doceava caracteristica: pixeles del numero en la columna ubicada en un cuarto de la imagen
            pixelesDelNumeroEnLaColumnaUnCuarto=pixelesDelNumeroEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaUnCuarto
            #Treceava caracteristica: cortes del numero en la columna ubicada en tres cuartos de la imagen
            cortesEnLaColumnaTresCuartos=cortesEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaTresCuartos
            #Catorceava caracteristica: pixeles del numero en la columna ubicada en tres cuartos de la imagen
            pixelesDelNumeroEnLaColumnaTresCuartos=pixelesDelNumeroEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaTresCuartos
            salida.writerow([relacionLargoEntreAncho,areaDelNumero,CortesEnLaFilaCentral,pixelesDelNumeroEnLaFilaCentral,cortesEnLaColumnaCentral,pixelesDelNumeroEnLaColumnaCentral,cortesEnLaFilaUnCuarto,pixelesDelNumeroEnLaFilaUnCuarto,cortesEnLaFilaTresCuartos,pixelesDelNumeroEnLaFilaTresCuartos,cortesEnLaColumnaUnCuarto,pixelesDelNumeroEnLaColumnaUnCuarto,cortesEnLaColumnaTresCuartos,pixelesDelNumeroEnLaColumnaTresCuartos,clase]) #escribo las caracteristicas en el archivo csv
        #fin del for fname
        clase=clase+1 #aumento la clase en uno cuando termine de leer una subcarpeta
    #fin del for dirName
    archivo.close() #Se cierra el archivo
#funcion principal que realiza en su interior realiza todos los procesos para crear el dataset
creacionDataSet() #mando a traer a la funcion creaciondataset