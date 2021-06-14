from Nodo import NodoMatrixDispersa
import os

def crearNodo(identificador,nombre, shape):
    return identificador + "[label=\""+ nombre + "\",shape="+ shape + "]\n"

def unionNodo(nodoA,nodoB):
    return nodoA + "->" + nodoB +"\n"


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
    
    def agregarOrdenadoColumna(self,nuevo,cabezaColumna):
        temp = cabezaColumna
        flag=False
        while True:
            #if para verificar si ya existe sobrescribe el nodo
            if(temp.x == nuevo.x):
                temp.y = nuevo.y
                temp.color=nuevo.color
                return temp #nos Retorna el Puntero. 
            elif(temp.x > nuevo.x):
                #Esto nos indica que hay que incertar antes de Temp
                flag = True
                break
            if (temp.siguiente is not None):
                temp=temp.siguiente
            else:
                break
        if flag:
            #agregarlo antes de temporal
            nuevo.siguiente = temp
            temp.anterior.siguiente = nuevo
            nuevo.anterior = temp.anterior
            temp.anterior = nuevo
        else:
            temp.siguiente = nuevo
            nuevo.anterior = temp
        return nuevo

    def agregarOrdenadoFila(self,nuevo,cabezaFila):
        temp = cabezaFila
        flag = False

        while True:
            if(temp.y == nuevo.y):
                temp.x = nuevo.x
                temp.color = nuevo.color
            elif(temp.y > nuevo.y):
                flag = True
                break
            if (temp.abajo is not None):
                temp = temp.abajo
            else:
                break

        if flag:
            nuevo.abajo = temp
            print(temp.abajo)
            temp.arriba.abajo = nuevo
            nuevo.arriba = temp.arriba
            temp.arriba = nuevo
        else:
            temp.abajo = nuevo
            nuevo.arriba = temp
        return nuevo
    
    def crearColumna (self,x):
        cabezaColumna = self.raiz
        columna = self.agregarOrdenadoColumna(NodoMatrixDispersa(x,-1,("X="+str(x))),cabezaColumna)
        return columna

    def crearFila(self,y):
        cabezaFila = self.raiz
        fila = self.agregarOrdenadoFila(NodoMatrixDispersa(-1,y,("Y="+str(y))),cabezaFila)
        return fila
    
    def insertarElemento (self,x,y,color):
        nuevo = NodoMatrixDispersa(x,y,color)
        nodoColumna = self.buscarCoordenadaX(x)
        nodoFila = self.buscarCoordenadaY(y)

        #Cuando no existe ni fila ni columna:
        if (nodoColumna is None and nodoFila is None):
            print("Fila y Columna no Existen se Crearan en este momento")
            #Creamos Columna
            nodoColumna = self.crearColumna(x)
            print("Columna Creada ##############################")
            #Creamos Fila
            print(self.raiz.abajo)
            nodoFila = self.crearFila(y)
            print("Fila Creada ------------------------------------------")
            #Insertamos Ordenado con Respecto Columna
            nuevo = self.agregarOrdenadoColumna(nuevo,nodoFila)
            print("----------- Nodo Insertado en Orden con Respecto Columna -----------------------")
            #Insertamos Ordenado con Respecto Fila
            nuevo = self.agregarOrdenadoFila(nuevo,nodoColumna)
            print("------------ Nodo Insertado en Orden con Respecto Fila -------------------------")

        elif(nodoColumna is None and nodoFila is not None):
            #Creamos Columna
            nodoColumna = self.crearColumna(x)
            print("Columna Creada ##############################")
            #Insertamos Ordenado con Respecto Columna
            nuevo = self.agregarOrdenadoColumna(nuevo,nodoFila)
            print("----------- Nodo Insertado en Orden con Respecto Columna -----------------------")
            #Insertamos Ordenado con Respecto Fila
            nuevo = self.agregarOrdenadoFila(nuevo,nodoColumna)
            print("------------ Nodo Insertado en Orden con Respecto Fila -------------------------")
        
        elif(nodoColumna is not None and nodoFila is None):
            #Creamos Fila
            print(self.raiz.abajo)
            nodoFila = self.crearFila(y)
            print("Fila Creada ------------------------------------------")
            #Insertamos Ordenado con Respecto Columna
            nuevo = self.agregarOrdenadoColumna(nuevo,nodoFila)
            print("----------- Nodo Insertado en Orden con Respecto Columna -----------------------")
            #Insertamos Ordenado con Respecto Fila
            nuevo = self.agregarOrdenadoFila(nuevo,nodoColumna)
            print("------------ Nodo Insertado en Orden con Respecto Fila -------------------------")
        
        elif(nodoColumna is not None and nodoFila is not None):
           #Insertamos Ordenado con Respecto Columna
            nuevo = self.agregarOrdenadoColumna(nuevo,nodoFila)
            print("----------- Nodo Insertado en Orden con Respecto Columna -----------------------")
            #Insertamos Ordenado con Respecto Fila
            nuevo = self.agregarOrdenadoFila(nuevo,nodoColumna)
            print("------------ Nodo Insertado en Orden con Respecto Fila -------------------------") 
    
    def generarGrafo(self):
        contadorFilas=0
        ContadorColumnas=0
        file = open("grafo2.dot","w")
        file.write("digraph G{\n")
        temporalFilas = self.raiz
        temporalColumnas=self.raiz
        banderaRaiz = False
        if(self.raiz.abajo is None and self.raiz.siguiente is None):
            file.write(crearNodo("raiz",("("+str(self.raiz.x)+","+str(self.raiz.y)+") \n"+self.raiz.color),"box"))
        else:
            #Imprmir Cabezeras:
            # ------------------- Imprimir Cabeceras en X -------------------------------------------------------
            while temporalColumnas != None:
                if(temporalColumnas.color == "Raiz"):
                   file.write(crearNodo("raiz",("("+str(self.raiz.x)+","+str(self.raiz.y)+") \n"+self.raiz.color),"box"))
                   #banderaRaiz=true
                else:
                    file.write(crearNodo("x"+str(temporalColumnas.x),("("+str(temporalColumnas.x)+","+str(temporalColumnas.y)+") \n"+temporalColumnas.color),"box"))
                    print("("+str(temporalColumnas.x)+","+str(temporalColumnas.y)+")\n"+temporalColumnas.color)
                    print("----------------")
                temporalColumnas = temporalColumnas.siguiente
                    #ContadorColumnas=ContadorColumnas+1
            # --------------------- Imprmir Cabezeras en Y -------------------------------------------------------
            while temporalColumnas != None:
                if(temporalColumnas.color == "Raiz"):
                    file.write(crearNodo("raiz",("("+str(self.raiz.x)+","+str(self.raiz.y)+") \n"+self.raiz.color),"box"))
                else: 
                    file.write(crearNodo("y"+str(temporalFilas.y),("("+str(temporalFilas.x)+","+str(temporalFilas.y)+") \n"+temporalFilas.color),"box"))
                    print("("+str(temporalFilas.x)+","+str(temporalFilas.y)+")\n"+temporalFilas.color)
                    print("----------------")
                temporalFilas = temporalFilas.abajo
                #contadorFilas=contadorFilas+1
        
        #---------------- A partir de Aqui Uniremos los Nodos Cabezera -----------------------------------------
            temporalColumnas=self.raiz
            temporalFilas=self.raiz
            if(self.raiz.abajo is None and self.raiz.siguiente is None):
                print("Solo Existe el Nodo Raiz y Ya fue Graficado")
            else:
                while temporalColumnas != None:
                    if(temporalColumnas.color == "Raiz"):
                        file.write("rank=same{")
                        file.write(unionNodo("raiz","x"+str(temporalColumnas.siguiente.x)))
                        file.write(unionNodo("x"+str(temporalColumnas.siguiente.x),"raiz"))
                        file.write("}")
                    else:
                        if(temporalColumnas.siguiente is None):
                            print("No hay mas Nodos Cabezera en X por crear")
                        else:
                            file.write("rank=same{ \n")
                            file.write(unionNodo("x"+str(temporalColumnas.x),"x"+str(temporalColumnas.siguiente.x)))
                            file.write(unionNodo("x"+str(temporalColumnas.siguiente.x),"x"+str(temporalColumnas.x)))
                            file.write("} \n")
                    temporalColumnas=temporalColumnas.siguiente

                while temporalFilas != None:
                    if(temporalFilas.color=="Raiz"):
                        file.write(unionNodo("raiz","y"+str(temporalFilas.abajo.y)))
                        file.write(unionNodo("y"+str(temporalFilas.abajo.y),"raiz"))
                    else:
                        if(temporalFilas.abajo is None):
                            print("No hay Mas Nodos Cabezera en Y por Crear")
                        else:
                            file.write(unionNodo("y"+str(temporalFilas.y),"y"+str(temporalFilas.abajo.y)))
                            file.write(unionNodo("y"+str(temporalFilas.abajo.y),"y"+str(temporalFilas.y)))
                    temporalFilas=temporalFilas.abajo
        file.write("}")
        file.close()
        os.system('dot -Tpng grafo2.dot -o grafo2.png') 











