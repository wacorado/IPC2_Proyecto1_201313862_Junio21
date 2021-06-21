from tkinter import Tk, StringVar
from tkinter.ttk import Label
import threading
import time

window = Tk()
window.geometry('200x100')

# Variable que almacena el string con el contenido del reloj
timer = StringVar()

timer.set(0)  # Lo fija en 0


def timer_thread(seconds: int):
    i = 0
    while i < seconds:
        time.sleep(1)  # Pausa la ejecución por 1 segundo
        i += 1
        timer.set(i)  # actualiza el valor del reloj


if __name__ == '__main__':

    lbl1 = Label(window, textvariable=timer)
    lbl1.pack()

    # Pasar como arg la cantidad de segundos que se debe ejecutar
    t1 = threading.Thread(target=timer_thread, args=(60, ))

    t1.start()  # Inicia el hilo
    window.mainloop()  # Inicia la ventana

    # (Opcional) Todo lo que este debajo de esta la linea sera ejecutado cuando termine de ejecutarse el hilo
    t1.join()