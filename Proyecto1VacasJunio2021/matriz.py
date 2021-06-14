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
            while temporalFilas != None:
                if(temporalFilas.color == "Raiz"):
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
                        file.write("rank=same{ \n")
                        file.write(unionNodo("raiz","x"+str(temporalColumnas.siguiente.x)))
                        file.write(unionNodo("x"+str(temporalColumnas.siguiente.x),"raiz"))
                        file.write("} \n")
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
        file.write("/* Hasta Aqui estan creados y Unidos los Nodos Cabezera */ \n")

        # ---------------------------- Se prodede a Crear los Nodos Interiores de la Matriz ----------------------------------------
        temporalFilas = self.raiz
        temporalColumnas=self.raiz

        while temporalColumnas != None:
            if(temporalColumnas.color=="Raiz"):
                print("Estoy en el Nodo Raiz iniciare a Moverme a la Derecha")
            else:
                temporalAbajo=temporalColumnas
                while temporalAbajo != None:
                    if(temporalAbajo.abajo is None):
                        print("No ha mas Nodos hacia abajo de "+temporalColumnas.color+" Por Crear")
                    if(temporalAbajo.color == ("X="+str(temporalAbajo.x))):
                        print("Este Nodo ya fue Creado xq es Cabecera")
                    else:
                        file.write(crearNodo(("Nodo"+str(temporalAbajo.x)+""+str(temporalAbajo.y)+""),("("+str(temporalAbajo.x)+","+str(temporalAbajo.y)+")\n"+temporalAbajo.color),"box"))
                    temporalAbajo=temporalAbajo.abajo
            temporalColumnas=temporalColumnas.siguiente
        # -------------------------------- Se proceden a unir los Nodos en forma Vertical -----------------------------------------
        temporalFilas = self.raiz
        temporalColumnas=self.raiz

        while temporalColumnas != None:
            if(temporalColumnas.color=="Raiz"):
                print("Estoy en el Nodo Raiz iniciare a Moverme a la Derecha")
            else:
                temporalAbajo=temporalColumnas
                while temporalAbajo != None:
                    if(temporalAbajo.abajo is None):
                        print("No ha mas Nodos hacia abajo de "+temporalColumnas.color+" Por uninr")
                    if(temporalAbajo.color == ("X="+str(temporalAbajo.x))):
                        file.write(unionNodo(("x"+str(temporalAbajo.x)),("Nodo"+str(temporalAbajo.abajo.x)+""+str(temporalAbajo.abajo.y)+"")))
                        file.write(unionNodo(("Nodo"+str(temporalAbajo.abajo.x)+""+str(temporalAbajo.abajo.y)+""),("x"+str(temporalAbajo.x))))
                        #file.write(unionNodo(("y"+str(temporalAbajo.x)),("Nodo"+str(temporalAbajo.abajo.x)+""+str(temporalAbajo.abajo.y)+""))
                        print("Este Nodo ya fue  xq es Cabecera")
                    else:
                        if(temporalAbajo.abajo is None):
                            print("No ha mas Nodos hacia abajo de "+temporalColumnas.color+" Por uninr") 
                        else:
                            file.write(unionNodo(("Nodo"+str(temporalAbajo.abajo.x)+""+str(temporalAbajo.abajo.y)),("Nodo"+str(temporalAbajo.x)+""+str(temporalAbajo.y))))
                            file.write(unionNodo(("Nodo"+str(temporalAbajo.x)+""+str(temporalAbajo.y)),("Nodo"+str(temporalAbajo.abajo.x)+""+str(temporalAbajo.abajo.y))))
                        
                        #file.write(crearNodo(("Nodo"+str(temporalAbajo.x)+""+str(temporalAbajo.y)+""),("("+str(temporalAbajo.x)+","+str(temporalAbajo.y)+")\n"+temporalAbajo.color),"box"))
                        print("Aqui se uniran el resto de nodos")
                    temporalAbajo=temporalAbajo.abajo
            temporalColumnas=temporalColumnas.siguiente
        # --------------------------- Se procede a hacer las uniones de forma Horizontal ------------------------------------------------
        temporalFilas = self.raiz
        temporalColumnas=self.raiz

        while temporalFilas != None:
            if(temporalFilas.color=="Raiz"):
                print("Estoy en el Nodo Raiz iniciare a Moverme a Abajo")
            else:
                temporalDerecha=temporalFilas
                while temporalDerecha != None:
                    if(temporalDerecha.siguiente is None):
                        print("No ha mas Nodos hacia derecha de "+temporalDerecha.color+" Por uninr")
                    if(temporalDerecha.color == ("Y="+str(temporalDerecha.y))):
                        file.write("rank=same{ \n")
                        file.write(unionNodo(("y"+str(temporalDerecha.y)),("Nodo"+str(temporalDerecha.siguiente.x)+""+str(temporalDerecha.siguiente.y)+"")))
                        file.write(unionNodo(("Nodo"+str(temporalDerecha.siguiente.x)+""+str(temporalDerecha.siguiente.y)+""),("y"+str(temporalDerecha.y))))
                        file.write("} \n")
                        #file.write(unionNodo(("y"+str(temporalAbajo.x)),("Nodo"+str(temporalAbajo.abajo.x)+""+str(temporalAbajo.abajo.y)+""))
                        print("Este Nodo ya fue unido con Cabecera en Y")
                    else:
                        if(temporalDerecha.siguiente is None):
                            print("No ha mas Nodos hacia Derecha de "+temporalFilas.color+" Por uninr") 
                        else:
                            nodoA=("Nodo"+str(temporalDerecha.siguiente.x)+""+str(temporalDerecha.siguiente.y))
                            nodoB=("Nodo"+str(temporalDerecha.x)+""+str(temporalDerecha.y))
                            file.write("rank=same{ \n")
                            file.write(unionNodo(nodoA,nodoB))
                            file.write(unionNodo(nodoB,nodoA))
                            file.write("} \n")

                            #file.write(unionNodo(("Nodo"+str(temporalDerecha.siguiente.x)+""+str(temporalDerecha.siguiente.y)),("Nodo"+str(temporalDerecha.x)+""+str(temporalDerecha.y))))
                            #file.write(unionNodo(("Nodo"+str(temporalDerecha.x)+""+str(temporalDerecha.y)),("Nodo"+str(temporalDerecha.siguiente.x)+""+str(temporalDerecha.siguiente.y))))
                        
                        #file.write(crearNodo(("Nodo"+str(temporalAbajo.x)+""+str(temporalAbajo.y)+""),("("+str(temporalAbajo.x)+","+str(temporalAbajo.y)+")\n"+temporalAbajo.color),"box"))
                        print("Aqui se uniran el resto de nodos")
                    temporalDerecha=temporalDerecha.siguiente
            temporalFilas=temporalFilas.abajo
        """
        temporalColumnas=self.raiz
        temporalFilas=self.raiz
        if(self.raiz.abajo is None and self.raiz.siguiente is None):
                print("Solo Existe el Nodo Raiz y Ya fue Graficado")
        else:
            while temporalColumnas != None:
                temporalAbajo=temporalColumnas
                if(temporalAbajo.abajo is None and temporalAbajo.siguiente is None):
                    print("--------- Nodo Raiz -----------------")
                else: 
                    while temporalAbajo != None:
                        if(temporalAbajo.abajo is None):
                            print("No hay nodos hacia abajo en esa Columna para Unir")
                        else:
                            if(temporalAbajo.color == ("X="+str(temporalAbajo.x))):
                                #file.write("AquiEntroSupestamentePara unir Cabeza x hacia primero abajo \n")
                                file.write(unionNodo("x"+str(temporalColumnas.x),(""+str(temporalAbajo.abajo.x)+","+str(temporalAbajo.abajo.y)+"")))
                                file.write(unionNodo((""+str(temporalAbajo.abajo.x)+","+str(temporalAbajo.abajo.y)+""),"x"+str(temporalColumnas.x)))
                            else:
                                print("aqui van los otros")
                                #file.write("AquiEntroSupestamentePara unir todos los nodos hacia abajo \n")
                                #file.write(unionNodo(("("+str(temporalAbajo.x)+","+str(temporalAbajo.y)+")"),("("+str(temporalAbajo.abajo.x)+","+str(temporalAbajo.abajo.y)+")")))
                                #file.write(unionNodo(("("+str(temporalAbajo.abajo.x)+","+str(temporalAbajo.abajo.y)+")"),("("+str(temporalAbajo.x)+","+str(temporalAbajo.y)+")")))
                        temporalAbajo=temporalAbajo.abajo
                temporalColumnas = temporalColumnas.siguiente
            """
        file.write("}")
        file.close()
        os.system('dot -Tpng grafo2.dot -o grafo2.png') 











