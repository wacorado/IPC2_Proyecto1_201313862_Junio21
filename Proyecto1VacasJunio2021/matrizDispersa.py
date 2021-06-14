from Nodo import NodoMatrixDispersa
import os

class MatrizDispersa():
    def __init__(self):
        self.raiz = NodoMatrixDispersa(-1,-1, "Raiz")
    
    def buscarCoordenadaX(self,x):
        temp = self.raiz
        while temp is not None:
            if(temp.x==x):
                return temp
            temp = temp.siguiente
        return None
    
    def buscarCoordenadaY(self,y):
        temp = self.raiz
        while temp is not None:
            if(temp.y==y):
                return temp
            temp = temp.abajo
        return None

    #-------------- Metodo para Crear fila en la matriz, CrearFila ----------------------------------------

    def insertarOrdenadoY(self,nuevo, cabezaFila):
        temp = cabezaFila
        bandera = True
        while True:
            if temp.y==nuevo.y:
                temp.x=nuevo.x
                temp.color=nuevo.color
                return temp
            elif(temp.y>nuevo.y):
                bandera=True
                break
            if temp.abajo is not None:
                temp=temp.abajo
            else:
                break
            if bandera is True:
                nuevo.abajo=temp
                temp.arriba.abajo=nuevo
                nuevo.arriba=temp.arriba
                temp.arriba=nuevo
            else:
                temp.abajo=nuevo
                nuevo.arriba=temp
            return nuevo

    # ------------- Metodo para Crear Columna en la matriz, CrearColumna -----------------------------------
    def insertarOrdenadoEnX(self, nuevo, cabezaColumna):
        temp=cabezaColumna
        
    def insertarOrdenadoX(self,nuevo,cabezaColumna):
        temp = cabezaColumna
        bandera = False
        while True:
            if(temp.x == nuevo.x):
                # SI LA POSICION ES LA MISMA SOBRE ESCRIBO
                temp.y = nuevo.y
                temp.dato = nuevo.dato
                return temp #RETORNAMOS EL PUNTERO
            elif(temp.x > nuevo.x):
                # TENGO QUE INSERTARLO ANTES DE TEMP
                bandera = True
                break
            if temp.siguiente is not None:
                temp = temp.siguiente
            else:
                # TENGO QUE INSERTAR NUEVO DESPUES DE TEMP
                # bandera = FALSE
                break
        if bandera:
            # INSERTARLO ANTES DE TEMPORAL
            nuevo.siguiente = temp
            temp.anterior.siguiente = nuevo
            nuevo.anterior = temp.anterior
            temp.anterior = nuevo
        else:
            temp.siguiente = nuevo
            nuevo.anterior = temp
        return nuevo

    def crearColumna(self,x):
        cabezaColumna=self.raiz
        columna=self.insertarOrdenadoX(NodoMatrixDispersa(x,0,"sinColor"),cabezaColumna)
        return columna
    
    def crearFila(self,y):
        cabezaFila=self.raiz
        fila=self.insertarOrdenadoY(NodoMatrixDispersa(0,y,"SinColor"),cabezaFila)
        return fila
    
    def insertarNodo(self, x,y,color):
        #Obtenemos los nodos para las coordenadas  
        nuevo=NodoMatrixDispersa(x,y,color)
        nodoColumna = self.buscarCoordenadaX(x)
        nodoFila = self.buscarCoordenadaY(y)

        #Cuando FILA Y COLUMNA no Existen
        if nodoColumna is None and nodoFila is None: 
            print("Opcion cuando no existe nodo y columna")
             #aqui crearemos Columna
            nodoColumna=self.crearColumna(x)
             #aqui creamos fila
            nodoFila=self.crearFila(y)
             #agregamos en la listadoblemente enlazada de forma enlazada de las columnas
            nuevo=self.insertarOrdenadoX(nuevo,nodoFila)
             #agregamos en la listadoblemente enlazada de forma enlazada de las filas
            nuevo=self.insertarOrdenadoY(nuevo,nodoColumna)
            return

        elif nodoColumna is None and nodoFila is not None:
            print("cuando no existe x pero si existe y")
            #creamos Columna
            nodoColumna=self.crearColumna(x)
            #insertamos ordenado en Columna
            nuevo=self.insertarOrdenadoX(nuevo,nodoFila)
            #insertamos ordenado en Fila
            nuevo=self.insertarOrdenadoY(nuevo,nodoColumna)
        
        elif nodoColumna is not None and nodoFila is None:
            print("cuando columna existe y fila no existe")
            #creamos Fila
            nodoFila=self.crearFila(y)
            #insertar ordenado columna
            nuevo=self.insertarOrdenadoX(nuevo,nodoFila)
            #insertar ordeando Fila
            nuevo=self.insertarOrdenadoY(nuevo,nodoColumna)

        elif nodoColumna is not None and nodoFila is not None:
            print("cuando exite fila y columna")
            #insertar ordenado Columna
            nuevo=self.insertarOrdenadoX(nuevo,nodoFila)
            #insertar ordenado Fila
            nuevo=self.insertarOrdenadoY(nuevo,nodoColumna)

    def generarGrafico(self):
        contadorFilas=0
        contadorColumnas=0
        file = open("grafo.dot","w")
        file.write("digraph G{\n")
        temporalFilas = self.raiz
        temporalColumnas=self.raiz
        if(self.raiz.abajo is None and self.raiz.siguiente is None):
            file.write(crearNodo("raiz",("("+str(self.raiz.x)+","+str(self.raiz.y)+") \n"+self.raiz.color),"box"))
            contadorFilas=0
            ContadorColumnas=0
        else:

            while temporalFilas != None:
                file.write(crearNodo(str(temporalFilas.y),("("+str(temporalFilas.x)+","+str(temporalFilas.y)+") \n"+temporalFilas.color),"box"))
                #file.write(crearNodo("("+str(temporalFilas.x)+","+str(temporalFilas.y),")\n"+temporalFilas.color))
                print("("+str(temporalFilas.x)+","+str(temporalFilas.y)+")\n"+temporalFilas.color)
                contadorFilas=contadorFilas+1
                temporalFilas = temporalFilas.abajo
                print("-----------------------------------------------------------------------------------------------\n")
        
            while temporalColumnas != None:
                file.write(crearNodo(str(temporalColumnas.x),("("+str(temporalColumnas.x)+","+str(temporalColumnas.y)+") \n"+temporalColumnas.color),"box"))
                print("("+str(temporalColumnas.x)+","+str(temporalColumnas.y)+")\n"+temporalColumnas.color)
                contadorColumnas=contadorColumnas+1
                temporalColumnas = temporalColumnas.siguiente
                print("-----------------------------------------------------------------------------------------------\n")
        #unimos los nodos de la lista doble Columnas equivalente a X
            for i in range(contadorColumnas):
                file.write("rank=same{")
                file.write(unionNodo(str(temporalColumnas.x),str(temporalColumnas.x+1)))
                file.write(unionNodo(str(temporalColumnas.x+1),str(temporalColumnas.x)))
                file.write("}")

            for i in range(contadorFilas):
                file.write(unionNodo(str(temporalFilas.y),str(temporalFilas.y+1)))
                file.write(unionNodo(str(temporalFilas.y+1),str(temporalFilas.y)))
        file.write("}")
        file.close()
        os.system('dot -Tpng grafo.dot -o grafo.png') 
    
def crearNodo(identificador,nombre, shape):
    return identificador + "[label=\""+ nombre + "\",shape="+ shape + "]\n"

def unionNodo(nodoA,nodoB):
    return nodoA + "->" + nodoB +"\n"
