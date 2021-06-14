from matriz import MatrizDispersa

matriz=MatrizDispersa()

def menu():
    print("1. Crear Nodo en Matriz")
    print("2. Graficar")
    print("3. Salir")
    opcion = input("Ingrese una opccion: \n")
    return opcion

def agregarNodo():
    posX=input("Ingrese la Coordenada X: \n")
    posY=input("Ingrese la Coordenada Y: \n")
    color=input("Ingrse el Color para Celda: \n")
    matriz.insertarElemento(int(posX),int(posY),color)

def generarGrafica():
    matriz.generarGrafo()

ciclo=True
while(ciclo):
    numero = menu()
    if numero == "1":
        print("Opcion1")
        agregarNodo()
        input("")
    elif numero == "2":
        print("Opcion2")
        generarGrafica()
        input("")
    elif numero == "3":
        #salir()
        input("")
        ciclo=False
    elif numero >= str(5):
        print("Opcion no Valida debe ingresar una opcion entre 1 y 3")
        input("")