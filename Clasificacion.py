# -*- coding: utf-8 -*-
"""
Programa: Clasificacion
Descripcion: Permite clasificar un numero  contenido en una imagen binarizada
"""
#impprto las libreria adecuadas para trabajar
import matplotlib.image as mpimg #importo libreria para el manejo de imagenes
import csv #importo la libreria para el manejo de archivos csv
import math #importo la libreria para poder usar raiz cuadrada
import OCR as Funciones #importo el proyecto OCR y un objeto para acceder a sus funciones y no reescribir codigo

'''
Nombre de la funcion: lecturaDelDataset
Descripcion: Permite acceder a un archivo csv y guardar los datos en una matriz
Parametros de entrada: Ninguno
Resultado: Obtengo una matriz
'''
def lecturaDelDataSet():
    f= open('DataSet.csv') #abro un archivo csv
    lns=csv.reader(f) #obtengo la informacion del archivo
    dataset=list(lns) #guardo la informacion obtenida en una matriz
    f.close() #cierro el archivo
    return dataset #devuelvo la matriz con los datos

'''
Nombre de la funcion: convertirDataset
Descripcion: Cambio el tipo de los datos del dataset de string a flotantes para realizar operaciones
Parametros de entrada: dataset (matriz con los datos)
Resultado: Un dataset con datos tipo flotante
'''
def convertirDataSet(dataset):
    fila=0 #inicio un contador que marcara el inicio de las filas en el dataset
    for i in dataset: #inicia el for para recorrer el dataset
        dataset[fila][0]=float(dataset[fila][0]) #convierto este dato a tipo flotante
        dataset[fila][1]=float(dataset[fila][1]) #convierto este dato a tipo flotante
        dataset[fila][2]=float(dataset[fila][2]) #convierto este dato a tipo flotante
        dataset[fila][3]=float(dataset[fila][3]) #convierto este dato a tipo flotante
        dataset[fila][4]=float(dataset[fila][4]) #convierto este dato a tipo flotante
        dataset[fila][5]=float(dataset[fila][5]) #convierto este dato a tipo flotante
        dataset[fila][6]=float(dataset[fila][6]) #convierto este dato a tipo flotante
        dataset[fila][7]=float(dataset[fila][7]) #convierto este dato a tipo flotante
        dataset[fila][8]=float(dataset[fila][8]) #convierto este dato a tipo flotante
        dataset[fila][9]=float(dataset[fila][9]) #convierto este dato a tipo flotante
        dataset[fila][10]=float(dataset[fila][10]) #convierto este dato a tipo flotante
        dataset[fila][11]=float(dataset[fila][11]) #convierto este dato a tipo flotante
        dataset[fila][12]=float(dataset[fila][12]) #convierto este dato a tipo flotante
        dataset[fila][13]=float(dataset[fila][13]) #convierto este dato a tipo flotante
        dataset[fila][14]=float(dataset[fila][14]) #convierto este dato a tipo flotante
        fila+=1 #aumento la variable fila para permitirme acceder a todas las filas del dataset
    return dataset #devuelvo el dataset convertido

'''
Nombre de la funcion: distancias
Descripcion: obtengo las distancias entre la nueva instancia y los datos del dataset
Parametros de entrada: dataset, y las caracteristicas de la nueva imagen
Resultado: un nuevo dataset con las distancias
'''
def distancias(dataset,caracteristica1,caracteristica2,caracteristica3,caracteristica4,caracteristica5,caracteristica6,caracteristica7,caracteristica8,caracteristica9,caracteristica10,caracteristica11,caracteristica12,caracteristica13,caracteristica14):
    fila=0 #inicio un contador que marcara el inicio de las filas en el dataset
    for i in dataset: #inicio el for para recorrer el dataset
        #Realizo la primer parte de la formula, que es una sumatoria de las diferencias entre caractristicas del dataset y la nueva instancia elevadas al cuadrado
        sumatoria=((dataset[fila][0]-caracteristica1)**2)+((dataset[fila][1]-caracteristica2)**2+((dataset[fila][2]-caracteristica3)**2)+((dataset[fila][3]-caracteristica4)**2)+((dataset[fila][4]-caracteristica5)**2)+((dataset[fila][5]-caracteristica6)**2)+((dataset[fila][6]-caracteristica7)**2)+((dataset[fila][7]-caracteristica8)**2)+((dataset[fila][8]-caracteristica9)**2)+((dataset[fila][9]-caracteristica10)**2)+((dataset[fila][10]-caracteristica11)**2)+((dataset[fila][11]-caracteristica12)**2)+((dataset[fila][12]-caracteristica13)**2)+((dataset[fila][13]-caracteristica14)**2))
        distancia=math.sqrt(sumatoria) #calculo la raiz cuadrada, la ultima parte de la formula
        dataset[fila].append(distancia) #agrego el valor obtenido al dataset
        dataset[fila].append(fila+1) #agrego la pocicion al elemento
        fila+=1 #aumento la variable fila para acceder a todas las filas del dataset
    return dataset #devuelvo el dataset con las distancias de todos  los datos o instancias

'''
Nombre de la funcion: datasetOrden
Descripcion: ordeno el dataset en referencia a la distacia, la mas corta va al inicio
Parametros de entrada: dataset, con las distancias
Resultado: dataset ordenado
'''
def datasetOrden(dataset):
    dataset.sort(key=lambda dataset: dataset[15]) #ordeno el dataset en base las distancias
    return dataset #devuelvo el dataset ordenado

'''
Nombre de la funcion: imagen
Descripcion: obtengo la ruta de la instancia a clasificar
Parametros de entrada: Ninguno
Resultado: una imagen para analizar
'''
def imagen():
    print('indica el nombre de la imagen deseada: ')
    nombre=input() #pido el nombre de la imagen
    ruta='C:/Users/ALAN/Documents/Python Scripts/imagen/imagenes' #carpeta con las imagenes a analizar
    nombreCompleto=ruta+'/'+nombre #ruta Y nombre de la imagen
    img=mpimg.imread(nombreCompleto) #ruta de la imagen
    return img #devuelvo a la imagen obtenida

'''
Nombre de la funcion: vecinos
Descripcion: considero el numero de vecinos para clasificar
Parametros de entrada: Ninguno
Resultado: El numero de vecinos a evaluar
'''
def vecinos():
    print("Numero de vecinos a considerar: ") #indico que se necesitan vecinos para evaluar
    k_vecinos=int(input()) #guardo el numero de vecinos en una variable
    return k_vecinos #devuelvo el numero de vecinos deseados

'''
Nombre de la funcion: clasificar
Descripcion: permite clasificar una nueva instancia o imagen
Parametros de entrada: dataset, kvecinos (numero de vecinos)
Resultado: decidir a que numero pertenece
'''
def clasificar(dataset,kVecinos):
    clase_0=0 #contador que indica la clase 0 (numero 0)
    clase_1=0 #contador que indica la clase 1 (numero 1)
    clase_2=0 #contador que indica la clase 2 (numero 2)
    clase_3=0 #contador que indica la clase 3 (numero 3)
    clase_4=0 #contador que indica la clase 4 (numero 4)
    clase_5=0 #contador que indica la clase 5 (numero 5)
    clase_6=0 #contador que indica la clase 6 (numero 6)
    clase_7=0 #contador que indica la clase 7 (numero 7)
    clase_8=0 #contador que indica la clase 8 (numero 8)
    clase_9=0 #contador que indica la clase 9 (numero 9)
    for i in range(0,kVecinos): #inicia for para recorrer a los vecinos mas cercanos
        if(dataset[i][14]==0): #condicion para conocer si un vecino pertenece a la clase 0
            clase_0+=1 #aumento de la clase 0
        if(dataset[i][14]==1): #condicion para conocer si un vecino pertenece a la clase 1
            clase_1+=1 #aumento de la clase 1
        if(dataset[i][14]==2): #condicion para conocer si un vecino pertenece a la clase 2
            clase_2+=1 #aumento de la clase 2
        if(dataset[i][14]==3): #condicion para conocer si un vecino pertenece a la clase 3
            clase_3+=1 #aumento de la clase 3
        if(dataset[i][14]==4): #condicion para conocer si un vecino pertenece a la clase 4
            clase_4+=1 #aumento de la clase 4
        if(dataset[i][14]==5): #condicion para conocer si un vecino pertenece a la clase 5
            clase_5+=1 #aumento de la clase 5
        if(dataset[i][14]==6): #condicion para conocer si un vecino pertenece a la clase 6
            clase_6+=1 #aumento de la clase 6
        if(dataset[i][14]==7): #condicion para conocer si un vecino pertenece a la clase 7
            clase_7+=1 #aumento de la clase 7
        if(dataset[i][14]==8): #condicion para conocer si un vecino pertenece a la clase 8
            clase_8+=1 #aumento de la clase 8
        if(dataset[i][14]==9): #condicion para conocer si un vecino pertenece a la clase 9
            clase_9+=1 #aumento de la clase 9
            
    #ubico al numero de la clase y el total de vecinos pertenecientes a ella en una matriz
    clases=[[0,clase_0],[1,clase_1],[2,clase_2],[3,clase_3],[4,clase_4],[5,clase_5],[6,clase_6],[7,clase_7],[8,clase_8],[9,clase_9]]
    clases.sort(key=lambda clases: clases[1]) #ordeno la matriz conforme al mayor numero de vecinos ordenados
    return clases

'''
Nombre de la funcion: imprencion
Descripcion: Muestra los resultados obtenidos
Parametros: clasificacion (numero de instancias por clase), dataset (datos) y K_vecinos
Resultado: los resultados de la clasificacion
'''
def imprecion(clasificacion,dataset,k_vecinos):
    instancias=len(dataset) #obtengo las instancias totales
    #Comienzo a imprimir la informacion mas general
    clasesEnDataset=[0,1,2,3,4,5,6,7,8,9]
    print('--------------------- Informacion general ---------------------------')
    print('Numero de intancias: ',instancias) #imprimo el numero de instancias
    print('Propiedades por instancia: 14') #imprimo el numero de caracteristicas
    print('Clases totales: 10') #imprimo el numero de clases
    print('Nombre de las clases: ') #indico el nombre de clases
    print(clasesEnDataset) #imprimo las claes
    print('---------------------------------------------------------------------\n')
    print('--------------------- vecinos mas cercanos --------------------------')
    for i in range (0,k_vecinos): #for para recorrer los vecinos mas cercanos
        #imprimo a l os vecinos mas cercanos
        print('Vecino: ',(i+1),' Instancia: ',dataset[i][16],' Distancia: ',dataset[i][15],' Clase: ',dataset[i][14])
    print('---------------------------------------------------------------------\n')
    print('--------------------- Instancias por clase --------------------------')
    for i in range (9,-1,-1):
        if(clasificacion[i][1]>0):
            print(clasificacion[i][1],' instancias pertenecen a la clase: ',clasificacion[i][0])
    print('---------------------------------------------------------------------\n')    
    if(clasificacion[9][1]==clasificacion[8][1]): #comparo si hubo un empate
        print('La imagen pertenece a la clase: ',dataset[0][14]) #en caso de empate la clase sera la del vecino mas cecarno
    else:
        print('La imagen pertenece a la clase: ', clasificacion[9][0]) #En caso contrario sera la clase con el mayor numero de vecinos
    print()




imagenNueva=imagen()#leo una imagen para sacar sus caracteristicas y clasificarla
dimencionesDeLaImagen=Funciones.dimencionesImagen(imagenNueva) #obtengo el largo  y ancho de la imagen (matriz) y las guardo en un arreglo
numeroDeFilas=Funciones.numeroFilas(dimencionesDeLaImagen) #obtengo el numero de filas total (largo de la imagen)
numeroDeColumnas=Funciones.numeroColumnas(dimencionesDeLaImagen) #obtengo el numero de columnas total (ancho de la imagen)
#comienzo a obtener las caracteristicas de la imagen
#Primer caracteristica: relacion de las dimenciones de la imagen
relacionLargoEntreAncho=Funciones.relacionTamaño(numeroDeFilas,numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable relacionLargoEntreAncho
#Segunda caracteristica: cantidad de pixeles del numero en la imagen
areaDelNumero=Funciones.areaNumero(numeroDeFilas,numeroDeColumnas,imagenNueva)#mando a traer esta funcion y la guardo en la variable areaDelNumero
#ubico la fila central de la imagen
FilaCentral=Funciones.filaCentral(numeroDeFilas) #mando a traer esta funcion y la guardo en la variable filaCentral
#ubico la columna central de la imagen
ColumnaCentral=Funciones.columnaCentral(numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable ColumnaCentral
#Tercera caracteristica: cortes del numero en la fila central de la imagen
CortesEnLaFilaCentral=Funciones.cortesEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable CortesEnLaFilaCentral
#Cuarta caracteristica: pixeles  del numero en la fila central de la imagen
pixelesDelNumeroEnLaFilaCentral=Funciones.pixelesDelNumeroEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroenLaFilaCentral
#Quinta caracteristica: cortes del numero en la columna central de la imagen
cortesEnLaColumnaCentral=Funciones.cortesEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaCentral
#Sexta caracteristica: pixeles del numero en la columna central de la imagen
pixelesDelNumeroEnLaColumnaCentral=Funciones.pixelesDelNumeroEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaCentral
#ubico la fila posicionada en un cuarto de la imagen (la relacion es base a las filas)
filaEnUnCuarto=Funciones.filaPosicionadaEnUnCuarto(FilaCentral) #mando a traer esta funcion y la guardo en la variable filaEnUnCuarto
#ubico la fila posiciona en tres Cuartos de la imagen (la relacion es base a las filas)
filaEnTresCuartos=Funciones.filaPosicionadaEnTresCuartos(FilaCentral,filaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable filaEnTresCuartos
#ubico la columna posicionada en un cuarto de la imagen (la relacion es base a las columnas)
columnaEnUnCuarto=Funciones.columnaPosicionadaEnUnCuarto(ColumnaCentral) #mando a traer esta funcion y la guardo en la variable columnaEnUnCuarto
#ubico la columna posicionada en tres cuartos de la imagen (la relacion es base a las columnas)
columnaEnTresCuartos=Funciones.columnaPosicionadaEnTresCuartos(ColumnaCentral,columnaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable columnaEnTresCuartos
#Septima caracteristica: cortes del numero en la fila un cuarto de la imagen
cortesEnLaFilaUnCuarto=Funciones.cortesEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaUnCuarto
#Octava caracteristica: pixeles del numero en la fila ubicada en un cuarto de la imagen
pixelesDelNumeroEnLaFilaUnCuarto=Funciones.pixelesDelNumeroEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaUnCuarto
#Novena caracteristica: cortes del numero en la fila tres cuartos de la imagen
cortesEnLaFilaTresCuartos=Funciones.cortesEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaTresCuartos
#Decima caracteristica: pixeles del numero en la fila ubicada en tres cuartos de la imagen
pixelesDelNumeroEnLaFilaTresCuartos=Funciones.pixelesDelNumeroEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaTresCuartos
#Onceava caracteristica: cortes del numero en la columna ubicada en un cuarto de la imagen
cortesEnLaColumnaUnCuarto=Funciones.cortesEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaUnCuarto
#Doceava caracteristica: pixeles del numero en la columna ubicada en un cuarto de la imagen
pixelesDelNumeroEnLaColumnaUnCuarto=Funciones.pixelesDelNumeroEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaUnCuarto
#Treceava caracteristica: cortes del numero en la columna ubicada en tres cuartos de la imagen
cortesEnLaColumnaTresCuartos=Funciones.cortesEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaTresCuartos
#Catorceava caracteristica: pixeles del numero en la columna ubicada en tres cuartos de la imagen
pixelesDelNumeroEnLaColumnaTresCuartos=Funciones.pixelesDelNumeroEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaTresCuartos

DataSetOriginal=lecturaDelDataSet() #leo el dataset
DataSetConvertido=convertirDataSet(DataSetOriginal) #convierto el dataset a flotantes
#Calculo las distancias en el dataset
DataSetConDistancias=distancias(DataSetConvertido,relacionLargoEntreAncho,areaDelNumero,CortesEnLaFilaCentral,pixelesDelNumeroEnLaFilaCentral,cortesEnLaColumnaCentral,pixelesDelNumeroEnLaColumnaCentral,cortesEnLaFilaUnCuarto,pixelesDelNumeroEnLaFilaUnCuarto,cortesEnLaFilaTresCuartos,pixelesDelNumeroEnLaFilaTresCuartos,cortesEnLaColumnaUnCuarto,pixelesDelNumeroEnLaColumnaUnCuarto,cortesEnLaColumnaTresCuartos,pixelesDelNumeroEnLaColumnaTresCuartos)
DataSetOrdenado=datasetOrden(DataSetConDistancias) #ordeno el dataset
numeroDeVecinos=vecinos() #pido el numero de vecinos a considerar
clasificacionDeInstancia=clasificar(DataSetOrdenado,numeroDeVecinos) #clasifico el numero de vecinos
imprecion(clasificacionDeInstancia,DataSetOrdenado,numeroDeVecinos)