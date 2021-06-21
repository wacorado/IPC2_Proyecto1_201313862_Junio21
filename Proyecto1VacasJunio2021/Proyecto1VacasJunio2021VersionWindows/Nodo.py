class NodoMatrixDispersa():
    #Nodo para la matriz Dispersa
    def __init__(self, x,y,color):
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        self.arriba = None
        self.x = x
        self.y = y
        self.color=color
    
    def nodoString(self):
        return "("+str(self.x)+","+str(self.y)+") = "+str(self.color)
    