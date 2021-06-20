from tkinter import *
import random
from tkinter import messagebox as MessageBox
from matriz import MatrizDispersa
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET


matriz=MatrizDispersa()

#Variables para hacer funcional interfaz y Botones
matrizBotones=[]
infBtnlista=[]
valorY=""
valorX=""
colorJ1=""
colorJ2=""
randomPiezaJ1=0
pathImg=""
piezaJ1=0
noturno = 1
nombrePartida =""
lnturno = ""
contadorPuntosJ1=0
contadorPuntosJ2=0
rPrincipal=None
matriz=None
nombrePartidaMatriz=None
imagen = None

def randomPiezaJ1Img():
    global randomPiezaJ1,piezaJ1, lnturno
    randomPiezaJ1=random.randint(1,6)
    if(randomPiezaJ1==1):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza1.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()
    elif(randomPiezaJ1==2):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza2.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()
    elif(randomPiezaJ1==3):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza3.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()
    elif(randomPiezaJ1==4):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza4.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()
    elif(randomPiezaJ1==5):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza5.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()
    elif(randomPiezaJ1==6):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza6.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()
    lnturno.refresh()

def pruebaPieza6():
    global randomPiezaJ1,piezaJ1
    randomPiezaJ1=6
    if(randomPiezaJ1==6):
        piezaJ1=randomPiezaJ1
        pathImg=PhotoImage(file="/Users/negrocorado/Desktop/Walther Corado/IPC2 2021/Vacas Junio/Proyecto1VacasJunio2021/Pieza6.gif")
        imgPequeña=pathImg.subsample(2)
        limgPieza.config(bg="#34495E",borderwidth=1, image=imgPequeña)
        limgPieza.refresh()

#Metodos para botones y programas 
def capDimensiones():
    global valorX, valorY, noturno
    print("Tamaño Matriz: "+str(len(matrizBotones)))
    valorY=txtFilas.get()
    valorX=txtColumnas.get()
    #Creare la Matriz de Botones
    nfil = 1/int(valorY)
    ncol= 1/int(valorX)

    for y in range(int(valorX)):
        matrizBotones.append([])
        for x in range(int(valorY)):
            matrizBotones[y].append(Button(tablero))
            matrizBotones[y][x].config(bg="white", borderwidth=2, relief="solid")
            matrizBotones[y][x].place(relx=ncol*y, rely=nfil*x, relwidth=ncol, relheigh=nfil)

    for y in range(int(valorY)):
        infBtnlista.append([])
        for x in range(int(valorX)):
            infBtnlista[y].append([x,y,True,"SinColor"])
        print("------------")
        print(infBtnlista[y])
        print("-------------")
    print("Tamaño Matriz: "+str(len(matrizBotones)))
    #pruebaPieza6()
    habilitaUsr()
    randomPiezaJ1Img()

def pintarJ1():
    global valorX, valorY, colorJ1, randomPiezaJ1,noturno,contadorPuntosJ1
    colorBtnJ1=""
    tamañoMatriz = len(matrizBotones)
    posX=(int(txtColumnasJ1.get())-1)
    posY=(int(txtFilasJ1.get())-1)
    colorJ1=txtColorJ1.get()
    flagValidPieza=True
    
    if (tamañoMatriz <= 0):
        MessageBox.showinfo("Error Tablero","Tablero no ha sido creado no se puede jugar")
    else:
        if(colorJ1.upper()=="ROJO"):
            colorBtnJ1="#B90000"
        elif(colorJ1.upper()=="AZUL"):
            colorBtnJ1="#00024C"
        elif(colorJ1.upper()=="AMARILLO"):
            colorBtnJ1="#FFB900"
        elif(colorJ1.upper()=="VERDE"):
            colorBtnJ1="#005F20"
        else:
            MessageBox.showinfo("Error Color J1","Color No Disponible para el Juego") 
        
        # ------------------------------- Vamos a Validad y Crear la Pieza1 ----------------------------------
        if(randomPiezaJ1==1):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX][posY+i][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                    flagValidPieza=False
                    if(i==3):
                        if(infBtnlista[posX+1][posY+i][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                            flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ1=contadorPuntosJ1+1
                for i in range(4):
                    if(infBtnlista[posX][posY+i][2] == True):
                        infBtnlista[posX][posY+i][2] = False
                        infBtnlista[posX][posY+i][3] = colorJ1
                        print("-----------------------------------")
                        print(infBtnlista[posX][posY+i])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX][posY+i].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1),int(posY+1+i),colorJ1)
                        matriz.generarGrafo()
                        if(i==3):
                            if(infBtnlista[posX+1][posY+i][2] == True):
                                infBtnlista[posX+1][posY+i][2] = False
                                infBtnlista[posX+1][posY+i][3] = colorJ1
                                print("-----------------------------------")
                                print(infBtnlista[posX+1][posY+i])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX+1][posY+i].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1+1),int(posY+1+i),colorJ1)
                                matriz.generarGrafo()
        
        if(randomPiezaJ1==2):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX][posY+i][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                    flagValidPieza=False
                    if(i==3):
                        if(infBtnlista[posX-1][posY+i][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                            flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ1=contadorPuntosJ1+1
                for i in range(4):
                    if(infBtnlista[posX][posY+i][2] == True):
                        infBtnlista[posX][posY+i][2] = False
                        infBtnlista[posX][posY+i][3] = colorJ1
                        print("-----------------------------------")
                        print(infBtnlista[posX][posY+i])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX][posY+i].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1),int(posY+1+i),colorJ1)
                        matriz.generarGrafo()
                        if(i==3):
                            if(infBtnlista[posX-1][posY+i][2] == True):
                                infBtnlista[posX-1][posY+i][2] = False
                                infBtnlista[posX-1][posY+i][3] = colorJ1
                                print("-----------------------------------")
                                print(infBtnlista[posX-1][posY+i])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX-1][posY+i].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1-1),int(posY+1+i),colorJ1)
                                matriz.generarGrafo()       
        
        if(randomPiezaJ1==3):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX+i][posY][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                    flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ1=contadorPuntosJ1+1
                for i in range(4):
                    if(infBtnlista[posX+i][posY][2] == True):
                        infBtnlista[posX+i][posY][2] = False
                        infBtnlista[posX+i][posY][3] = colorJ1
                        print("-----------------------------------")
                        print(infBtnlista[posX+i][posY])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX+i][posY].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1+i),int(posY+1),colorJ1)
                        matriz.generarGrafo()
        
        if(randomPiezaJ1==4):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(i==0):
                    if(infBtnlista[posX][posY][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False 
                elif(i==1):
                    if(infBtnlista[posX+1][posY][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False
                elif(i==2):
                    if(infBtnlista[posX][posY+1][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False 
                elif(i==3):
                    if(infBtnlista[posX+1][posY+1][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False 
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ1=contadorPuntosJ1+1
                for i in range(4):
                    if(i==0):
                        if(infBtnlista[posX][posY][2]==True):
                            infBtnlista[posX][posY][2] = False
                            infBtnlista[posX][posY][3] = colorJ1
                            print("-----------------------------------")
                            print(infBtnlista[posX][posY])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX][posY].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1),int(posY+1),colorJ1)
                            matriz.generarGrafo() 
                    elif(i==1):
                        if(infBtnlista[posX+1][posY][2]==True):
                            infBtnlista[posX+1][posY][2] = False
                            infBtnlista[posX+1][posY][3] = colorJ1
                            print("-----------------------------------")
                            print(infBtnlista[posX+1][posY])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX+1][posY].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1+1),int(posY+1),colorJ1)
                            matriz.generarGrafo() 
                    elif(i==2):
                        if(infBtnlista[posX][posY+1][2]==True):
                            infBtnlista[posX][posY+1][2] = False
                            infBtnlista[posX][posY+1][3] = colorJ1
                            print("-----------------------------------")
                            print(infBtnlista[posX][posY+1])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX][posY+1].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1),int(posY+1+1),colorJ1)
                            matriz.generarGrafo() 
                    elif(i==3):
                        if(infBtnlista[posX+1][posY+1][2]==True):
                            infBtnlista[posX+1][posY+1][2] = False
                            infBtnlista[posX+1][posY+1][3] = colorJ1
                            print("-----------------------------------")
                            print(infBtnlista[posX+1][posY+1])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX+1][posY+1].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1+1),int(posY+1+1),colorJ1)
                            matriz.generarGrafo() 

        if(randomPiezaJ1==5):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX+i][posY][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                    flagValidPieza=False
                    if(i==1):
                        if(infBtnlista[posX+i][posY-1][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY-1)+") No Valida")
                            flagValidPieza=False
                    if(i==2):
                        if(infBtnlista[posX+i][posY-1][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY-1)+") No Valida")
                            flagValidPieza=False
                        
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ1=contadorPuntosJ1+1
                for i in range(4):
                    if(infBtnlista[posX+i][posY][2] == True):
                        infBtnlista[posX+i][posY][2] = False
                        infBtnlista[posX+i][posY][3] = colorJ1
                        print("-----------------------------------")
                        print(infBtnlista[posX+i][posY])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX+i][posY].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1+i),int(posY+1),colorJ1)
                        matriz.generarGrafo()
                        if(i==1):
                            if(infBtnlista[posX+i][posY-1][2] == True):
                                infBtnlista[posX+i][posY-1][2] = False
                                infBtnlista[posX+i][posY-1][3] = colorJ1
                                print("-----------------------------------")
                                print(infBtnlista[posX+i][posY-1])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX+i][posY-1].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1+i),int(posY+1-1),colorJ1)
                                matriz.generarGrafo()
                        if(i==2):
                            if(infBtnlista[posX+i][posY-1][2] == True):
                                infBtnlista[posX+i][posY-1][2] = False
                                infBtnlista[posX+i][posY-1][3] = colorJ1
                                print("-----------------------------------")
                                print(infBtnlista[posX+i][posY-1])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX+i][posY-1].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1+i),int(posY+1-1),colorJ1)
                                matriz.generarGrafo()
    
        if(randomPiezaJ1==6):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX][posY+i][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                    flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ1=contadorPuntosJ1+1
                for i in range(4):
                    if(infBtnlista[posX][posY+i][2] == True):
                        infBtnlista[posX][posY+i][2] = False
                        infBtnlista[posX][posY+i][3] = colorJ1
                        print("-----------------------------------")
                        print(infBtnlista[posX][posY+i])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX][posY+i].config(bg=colorBtnJ1, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1),int(posY+1+i),colorJ1)
                        matriz.generarGrafo()
    txtColorJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=DISABLED)
    noturno=2
    turnero()
    randomPiezaJ1Img()
    #pruebaPieza6()

def pintarJ2():
    global valorX, valorY, colorJ2, randomPiezaJ1, noturno, contadorPuntosJ2
    colorBtnJ2=""
    tamañoMatriz = len(matrizBotones)
    posX=(int(txtColumnasJ2.get())-1)
    posY=(int(txtFilasJ2.get())-1)
    colorJ2=txtColorJ2.get()
    flagValidPieza=True
    
    if (tamañoMatriz <= 0):
        MessageBox.showinfo("Error Tablero","Tablero no ha sido creado no se puede jugar")
    else:
        if(colorJ2.upper()=="ROJO"):
            colorBtnJ2="#B90000"
        elif(colorJ2.upper()=="AZUL"):
            colorBtnJ2="#00024C"
        elif(colorJ2.upper()=="AMARILLO"):
            colorBtnJ2="#FFB900"
        elif(colorJ2.upper()=="VERDE"):
            colorBtnJ2="#005F20"
        else:
            MessageBox.showinfo("Error Color J2","Color No Disponible para el Juego") 
        
        # ------------------------------- Vamos a Validad y Crear la Pieza1 ----------------------------------
        if(randomPiezaJ1==1):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX][posY+i][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                    flagValidPieza=False
                    if(i==3):
                        if(infBtnlista[posX+1][posY+i][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                            flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ2=contadorPuntosJ2+1
                for i in range(4):
                    if(infBtnlista[posX][posY+i][2] == True):
                        infBtnlista[posX][posY+i][2] = False
                        infBtnlista[posX][posY+i][3] = colorJ2
                        print("-----------------------------------")
                        print(infBtnlista[posX][posY+i])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX][posY+i].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1),int(posY+1+i),colorJ2)
                        matriz.generarGrafo()
                        if(i==3):
                            if(infBtnlista[posX+1][posY+i][2] == True):
                                infBtnlista[posX+1][posY+i][2] = False
                                infBtnlista[posX+1][posY+i][3] = colorJ2
                                print("-----------------------------------")
                                print(infBtnlista[posX+1][posY+i])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX+1][posY+i].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1+1),int(posY+1+i),colorJ2)
                                matriz.generarGrafo()
        
        if(randomPiezaJ1==2):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX][posY+i][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                    flagValidPieza=False
                    if(i==3):
                        if(infBtnlista[posX-1][posY+i][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                            flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ2=contadorPuntosJ2+1
                for i in range(4):
                    if(infBtnlista[posX][posY+i][2] == True):
                        infBtnlista[posX][posY+i][2] = False
                        infBtnlista[posX][posY+i][3] = colorJ2
                        print("-----------------------------------")
                        print(infBtnlista[posX][posY+i])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX][posY+i].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1),int(posY+1+i),colorJ2)
                        matriz.generarGrafo()
                        if(i==3):
                            if(infBtnlista[posX-1][posY+i][2] == True):
                                infBtnlista[posX-1][posY+i][2] = False
                                infBtnlista[posX-1][posY+i][3] = colorJ2
                                print("-----------------------------------")
                                print(infBtnlista[posX-1][posY+i])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX-1][posY+i].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1-1),int(posY+1+i),colorJ2)
                                matriz.generarGrafo()       
        
        if(randomPiezaJ1==3):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX+i][posY][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                    flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ2=contadorPuntosJ2+1
                for i in range(4):
                    if(infBtnlista[posX+i][posY][2] == True):
                        infBtnlista[posX+i][posY][2] = False
                        infBtnlista[posX+i][posY][3] = colorJ2
                        print("-----------------------------------")
                        print(infBtnlista[posX+i][posY])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX+i][posY].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1+i),int(posY+1),colorJ2)
                        matriz.generarGrafo()
        
        if(randomPiezaJ1==4):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(i==0):
                    if(infBtnlista[posX][posY][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False 
                elif(i==1):
                    if(infBtnlista[posX+1][posY][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False
                elif(i==2):
                    if(infBtnlista[posX][posY+1][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False 
                elif(i==3):
                    if(infBtnlista[posX+1][posY+1][2]==False):
                        MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                        flagValidPieza=False 
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ2=contadorPuntosJ2+1
                for i in range(4):
                    if(i==0):
                        if(infBtnlista[posX][posY][2]==True):
                            infBtnlista[posX][posY][2] = False
                            infBtnlista[posX][posY][3] = colorJ2
                            print("-----------------------------------")
                            print(infBtnlista[posX][posY])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX][posY].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1),int(posY+1),colorJ2)
                            matriz.generarGrafo() 
                    elif(i==1):
                        if(infBtnlista[posX+1][posY][2]==True):
                            infBtnlista[posX+1][posY][2] = False
                            infBtnlista[posX+1][posY][3] = colorJ2
                            print("-----------------------------------")
                            print(infBtnlista[posX+1][posY])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX+1][posY].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1+1),int(posY+1),colorJ2)
                            matriz.generarGrafo() 
                    elif(i==2):
                        if(infBtnlista[posX][posY+1][2]==True):
                            infBtnlista[posX][posY+1][2] = False
                            infBtnlista[posX][posY+1][3] = colorJ2
                            print("-----------------------------------")
                            print(infBtnlista[posX][posY+1])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX][posY+1].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1),int(posY+1+1),colorJ2)
                            matriz.generarGrafo() 
                    elif(i==3):
                        if(infBtnlista[posX+1][posY+1][2]==True):
                            infBtnlista[posX+1][posY+1][2] = False
                            infBtnlista[posX+1][posY+1][3] = colorJ2
                            print("-----------------------------------")
                            print(infBtnlista[posX+1][posY+1])
                            print("-----------------------------------")
                            print()
                            matrizBotones[posX+1][posY+1].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                            matriz.insertarElemento(int(posX+1+1),int(posY+1+1),colorJ2)
                            matriz.generarGrafo() 

        if(randomPiezaJ1==5):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX+i][posY][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY)+") No Valida")
                    flagValidPieza=False
                    if(i==1):
                        if(infBtnlista[posX+i][posY-1][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY-1)+") No Valida")
                            flagValidPieza=False
                    if(i==2):
                        if(infBtnlista[posX+i][posY-1][2] == False):
                            MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX+i)+","+str(posY-1)+") No Valida")
                            flagValidPieza=False
                        
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ2=contadorPuntosJ2+1
                for i in range(4):
                    if(infBtnlista[posX+i][posY][2] == True):
                        infBtnlista[posX+i][posY][2] = False
                        infBtnlista[posX+i][posY][3] = colorJ2
                        print("-----------------------------------")
                        print(infBtnlista[posX+i][posY])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX+i][posY].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1+i),int(posY+1),colorJ2)
                        matriz.generarGrafo()
                        if(i==1):
                            if(infBtnlista[posX+i][posY-1][2] == True):
                                infBtnlista[posX+i][posY-1][2] = False
                                infBtnlista[posX+i][posY-1][3] = colorJ2
                                print("-----------------------------------")
                                print(infBtnlista[posX+i][posY-1])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX+i][posY-1].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1+i),int(posY+1-1),colorJ2)
                                matriz.generarGrafo()
                        if(i==2):
                            if(infBtnlista[posX+i][posY-1][2] == True):
                                infBtnlista[posX+i][posY-1][2] = False
                                infBtnlista[posX+i][posY-1][3] = colorJ2
                                print("-----------------------------------")
                                print(infBtnlista[posX+i][posY-1])
                                print("-----------------------------------")
                                print()
                                matrizBotones[posX+i][posY-1].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                                matriz.insertarElemento(int(posX+1+i),int(posY+1-1),colorJ2)
                                matriz.generarGrafo()
    
        if(randomPiezaJ1==6):
            # Validare Mediante el Crecimiento en Y las piezas en Y
            for i in range(4):
                if(infBtnlista[posX][posY+i][2] == False):
                    MessageBox.showinfo("Error Pieza","Casilla: ("+str(posX)+","+str(posY+i)+") No Valida")
                    flagValidPieza=False
            #Ya validado que se puede Poner la pieza Procedemos Insertar:
            if(flagValidPieza==True):
                contadorPuntosJ2=contadorPuntosJ2+1
                for i in range(4):
                    if(infBtnlista[posX][posY+i][2] == True):
                        infBtnlista[posX][posY+i][2] = False
                        infBtnlista[posX][posY+i][3] = colorJ2
                        print("-----------------------------------")
                        print(infBtnlista[posX][posY+i])
                        print("-----------------------------------")
                        print()
                        matrizBotones[posX][posY+i].config(bg=colorBtnJ2, borderwidth=2, relief="solid")
                        matriz.insertarElemento(int(posX+1),int(posY+1+i),colorJ2)
                        matriz.generarGrafo()
    txtColorJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=DISABLED)
    noturno=1
    turnero()
    randomPiezaJ1Img()

def inicioPartidametod():
    global nombrePartida, contadorPuntosJ1, contadorPuntosJ2
    nombrePartida=txtNomPartida.get()
    #txtColorJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=NORMAL)
    #txtColorJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=NORMAL)
    txtColumnas.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=NORMAL)
    txtFilas.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=NORMAL)
    btnCrearMatriz.config(bg="#34495E", fg="white", borderwidth=1,state=NORMAL)
    txtNomPartida.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state=DISABLED)
    contadorPuntosJ1 = 0
    contadorPuntosJ2 = 0

def habilitaUsr():
        # ---------------------- Desahbilito ---------------------------------------------------------------
        txtColumnas.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=DISABLED)
        txtFilas.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=DISABLED)
        btnCrearMatriz.config(bg="#34495E", fg="white", borderwidth=1,state=DISABLED)
        # -------------------------- Habilito ----------------------------------------------------------------
        txtColorJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=NORMAL)
        txtColorJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1,state=NORMAL)
        txtColumnasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        txtFilasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        txtColumnasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        txtFilasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        btnJ2.config(bg="#34495E", fg="white", borderwidth=1, state= NORMAL)
        btnJ1.config(bg="#34495E", fg="white", borderwidth=1, state= NORMAL)

def turnero():
    global noturno
    if(noturno==1):
        txtColumnasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        txtFilasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        btnJ1.config(bg="#34495E", fg="white", borderwidth=1, state= NORMAL)
        txtColumnasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)
        txtFilasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)
        btnJ2.config(bg="#34495E", fg="white", borderwidth=1, state= DISABLED)
    elif(noturno == 2):
        txtColumnasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)
        txtFilasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)
        btnJ1.config(bg="#34495E", fg="white", borderwidth=1, state= DISABLED)
        txtColumnasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        txtFilasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= NORMAL)
        btnJ2.config(bg="#34495E", fg="white", borderwidth=1, state= NORMAL)

def defGanador():
    global contadorPuntosJ2, contadorPuntosJ1

    if(contadorPuntosJ1>contadorPuntosJ2):
        MessageBox.showinfo("Ganador","El ganador es el Jugador 1")
    elif(contadorPuntosJ2>contadorPuntosJ1):
        MessageBox.showinfo("Ganador","El ganador es el Jugador 2")
    elif(contadorPuntosJ1==contadorPuntosJ2):
        MessageBox.showinfo("Empate","El juego esta empatado")
    else:
        MessageBox.showinfo("Error Definicion","No se puede determinar ganador")

def cargarPartida():
    archivo = askopenfilename()#Abre la interfaz para escoger el archivo a cargar
    print(archivo)
    #archivoLectura = open('' + archivo + '', 'r')

def reporteWeb():
        matriz.generarGrafo()
    #--------------- se genera el HTML DEL recorrido: ----------------------------
        file = open("ReporteJuego.html","w")
        file.write("<!DOCTYPE HTML>\n")
        file.write("<htm lang = \"es\">\n")
        file.write("<head>\n")
        file.write("<TITLE>REPORTE JUEGO BLOCKS</TITLE>\n")
        file.write("<link href=\"C:/Users/wacorado/Desktop/Proyecto1VacasJunio2021/Style.css\" type=\"text/css\">\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<div id = \"titulo\">\n")
        file.write("<h1>Reporte Grafico Matriz Dispersa</h1>\n")
        file.write("</div>\n")
        file.write("<div id= \"cuerpo\">\n")
        file.write("<img src=\""+"grafo2.png"+"\">\n")
        file.write("</div>\n")
        file.write("<div>\n")
        file.write("<p><h3>  Walther Andree Corado Paiz </h3></p>\n")
        file.write("<p><h3>  Carnet: 201313861 </h3></p>\n")
        file.write("<p><h3>  IPC2 Vacaciones Junio 2021 </h3></p>\n")
        file.write("</div>\n")
        file.write("</body>\n")
        file.write("</htmlL>\n")
        #os.startfile("index.html")
        #os.open("index.html")
        print("HTML GENERADO")

#Aqui va el Codigo de la Interfaz Grafica visualmente

#Para agregar nombre a la Venta usamos lo Siguiente:
ventana1=Tk()#instanciamos nuestra interfaz
ventana1.title("Juego Practica 1")
ventana1.geometry("1200x1000")
ventana1.config(bg = "#34495E")
# Etiquetas para la Interfaz para que el usuario coloque la cantidad de filas y columnas
lcolumnas = Label(ventana1, text="Dim.X: ")
lcolumnas.grid(row = 0, column = 0)
lcolumnas.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))
lfilas = Label(ventana1, text="DimY: ")
lfilas.grid(row = 1, column = 0)
lfilas.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))
        # Tex Box para ingresar Filas y Columnas  para iniciar Juego
filas=""
columnas=""
#Aqui creo el box para obtener el valor de cantidad de filas o coordenadas X
txtColumnas = Entry(ventana1, width=4, textvariable=columnas)
txtColumnas.grid(row=0, column=1)
txtColumnas.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED) 
#Aqui creo el box para obtener el valor de cantidad de filas o coordenadas Y
txtFilas = Entry(ventana1, width=4, textvariable=filas)
txtFilas.grid(row=1, column=1) 
txtFilas.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)
#Creo Boton Para Capturar Filas y Columnas para el Tablero
btnCrearMatriz = Button(ventana1, text="Crear Tablero", command = capDimensiones)
btnCrearMatriz.grid(row=0 , column=2)
btnCrearMatriz.config(bg="#34495E", fg="white", borderwidth=1, state= DISABLED)

# Frame para colocar el tablero dinamico de Botones:
tablero = Frame(ventana1)
tablero.config(bg = "#900C3F")
tablero.place(relx=0.003, rely=0.13, relwidth= 0.75, relheight= 0.75)
#---------------------------------------------------------- Controles de Jugadores --------------------------------------------------
#Creare Label y TextBox para CoordenadasX del J1
columnaJ1=""
lcolumnasJ1 = Label(ventana1, text="PosX: ")
lcolumnasJ1.grid(row = 0, column = 4)
lcolumnasJ1.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtColumnasJ1 = Entry(ventana1, width=4, textvariable=columnaJ1)
txtColumnasJ1.grid(row=0, column=5)
txtColumnasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED) 

#Create Label y TextBox para CoordenadasY del J1
filaJ1 = ""
lfilasJ1 = Label(ventana1, text="PosY: ")
lfilasJ1.grid(row = 1, column = 4)
lfilasJ1.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtFilasJ1 = Entry(ventana1, width=4, textvariable=filaJ1)
txtFilasJ1.grid(row=1, column=5)
txtFilasJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)

#Create Label y TextBox para Color del J1
colorJ1 = ""
lcolorJ1 = Label(ventana1, text="ColorJ1: ")
lcolorJ1.grid(row = 2, column = 4)
lcolorJ1.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtColorJ1 = Entry(ventana1, width=10, textvariable=colorJ1)
txtColorJ1.grid(row=2, column=5)
txtColorJ1.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)

#Se Crea el Boton para que el J1 pueda Jugar
btnJ1 = Button(ventana1, text="Jugar J1", command=pintarJ1)
btnJ1.grid(row=0 , column=6)
btnJ1.config(bg="#34495E", fg="white", borderwidth=1, state= DISABLED)

#Creare Label y TextBox para CoordenadasX del J2
columnaJ2=""
lcolumnasJ2 = Label(ventana1, text="PosX: ")
lcolumnasJ2.grid(row = 0, column = 7)
lcolumnasJ2.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtColumnasJ2 = Entry(ventana1, width=4, textvariable=columnaJ2)
txtColumnasJ2.grid(row=0, column=8)
txtColumnasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED) 

#Create Label y TextBox para CoordenadasY del J2
filaJ2 = ""
lfilasJ2 = Label(ventana1, text="PosY: ")
lfilasJ2.grid(row = 1, column = 7)
lfilasJ2.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtFilasJ2 = Entry(ventana1, width=4, textvariable=filaJ2)
txtFilasJ2.grid(row=1, column=8)
txtFilasJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)

#Create Label y TextBox para Color del J2
colorJ2 = ""
lcolorJ2 = Label(ventana1, text="ColorJ2: ")
lcolorJ2.grid(row = 2, column = 7)
lcolorJ2.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtColorJ2 = Entry(ventana1, width=10, textvariable=colorJ1)
txtColorJ2.grid(row=2, column=8)
txtColorJ2.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1, state= DISABLED)

#Se Crea el Boton para que el J2 pueda Jugar
btnJ2 = Button(ventana1, text="Jugar J2", command=pintarJ2)
btnJ2.grid(row=0 , column=9)
btnJ2.config(bg="#34495E", fg="white", borderwidth=1, state= DISABLED) 

#------------------------ piezas Aleatoreas como se Mostraran -----------------------------------------------------
#Aqui creare un Frame para Mostrar una Imagen Aleatoria de las piezas
pieza = Frame(ventana1)
pieza.config(bg = "#ADB3BD")
pieza.place(relx=0.778, rely=0.13, relwidth= 0.2, relheight= 0.2)

limgPieza = Label(pieza)
limgPieza.config(bg="#34495E",borderwidth=1, image=pathImg)
limgPieza.place(relx=0.003, rely=0.003, relwidth=0.99, relheight=0.99)

#---------------------- Label para Nombre de Partida, Boton Iniciar Juego, Boton Cargar Juego ------------------------
#Create Label y TextBox para Nombre Partida
nombrePartida= ""
lnombrePartida = Label(ventana1, text="NombrePartida: ")
lnombrePartida.grid(row = 0, column = 10)
lnombrePartida.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

txtNomPartida = Entry(ventana1, width=12, textvariable=nombrePartida)
txtNomPartida.grid(row=0, column=11)
txtNomPartida.config(bg="white", fg="#34495E", font=("Comic Sans MS", 16), borderwidth=1)

#Se Crea el Boton para que el Iniciar Partida y se  pueda Jugar
inicioPartida = Button(ventana1, text="Jugar", command=inicioPartidametod)
inicioPartida.place(relx=0.825, rely=0.365, relwidth= 0.1, relheight= 0.1)
inicioPartida.config(bg="#34495E", fg="white", borderwidth=1) 

#Se Crea el Boton para que el Cargar Partida y se  pueda Jugar
cargarPartida = Button(ventana1, text="Cargar\n" "Partida", command=cargarPartida)
cargarPartida.place(relx=0.825, rely=0.485, relwidth= 0.1, relheight= 0.1)
cargarPartida.config(bg="#34495E", fg="white", borderwidth=1) 

#Se Crea el Boton para que el Calificar Partida y se  pueda Jugar
calificarPartida = Button(ventana1, text="Calificar\n" "Partida", command=defGanador)
calificarPartida.place(relx=0.825, rely=0.610, relwidth= 0.1, relheight= 0.1)
calificarPartida.config(bg="#34495E", fg="white", borderwidth=1) 

#Se Crea el Boton para que el Calificar Partida y se  pueda Jugar
reporteJuego = Button(ventana1, text="Reporte\n" "Juego", command=reporteWeb)
reporteJuego.place(relx=0.825, rely=0.738, relwidth= 0.1, relheight= 0.1)
reporteJuego.config(bg="#34495E", fg="white", borderwidth=1)

#Se Crea el Boton para que el Reporte Grafico de  Partida
guardarJuego = Button(ventana1, text="Guardar\n" "Juego", command=pintarJ2)
guardarJuego.place(relx=0.825, rely=0.858, relwidth= 0.1, relheight= 0.1)
guardarJuego.config(bg="#34495E", fg="white", borderwidth=1) 


#---------------------- Label para Nombre de Partida, Boton Iniciar Juego, Boton Cargar Juego ------------------------
#Create Label y TextBox para CoordenadasY del J2
lturno = Label(ventana1, text="Turno: ")
lturno.grid(row = 2, column = 10)
lturno.config(bg="#34495E", fg="white", font=("Comic Sans MS", 24))


lnturno = Label(ventana1, text=noturno)
lnturno.grid(row = 2, column = 11)
lnturno.config(bg="#34495E", fg="white", font=("Comic Sans MS", 16))

ventana1.mainloop()

