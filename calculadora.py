from tkinter import *
from math import *


class calculadora ():
    def __init__(self, root):
        self.root = root
        self.root.title ("Calculadora")
        self.root.resizable (0,0)
        self.root.configure (bg= "bisque")

        self.n1 = IntVar ()
        self.n2 = IntVar ()
        self.resul = IntVar (value= 0)

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(2):
            self.root.columnconfigure(i, weight=1)
        

#Creamos las etiquetas

        self.label = Label (root, text= "Primer número")
        self.label.grid (row= 0, column= 0, sticky= "e")

        self.label = Label (root, text= "Segundo número")
        self.label.grid (row= 1, column= 0, sticky= "e")

        self.label = Label (root, text= "Resultado")
        self.label.grid (row= 2, column= 0, sticky= "e")

#Creamos 3 lineEdit

        self.edit1 = Entry (self.root, textvariable= self.n1)
        self.edit1.grid (row=0, column=1, sticky= "w")

        self.edit2 = Entry (self.root, textvariable= self.n2)
        self.edit2.grid (row= 1, column= 1, sticky= "w")

        self.edit3 = Entry (self.root, textvariable= self.resul, state= "readonly")
        self.edit3.grid (row= 2, column= 1, sticky= "w")

        #Creamos los botones

        self.boton1 = Button (root, text= "+", command= self.sumar)
        self.boton1.grid (row= 3, column=0, columnspan= 1, sticky= "we")

        self.boton2 = Button (root, text= "-", command= self.restar)
        self.boton2.grid (row= 3, column=1, columnspan= 2, sticky= "we")

        self.boton3 = Button (root, text= "*", command= self.multiplicar)
        self.boton3.grid (row= 4, column=0, columnspan= 1, sticky= "we")

        self.boton4 = Button (root, text= "/", command= self.dividir)
        self.boton4.grid (row= 4, column= 1, columnspan= 2, sticky= "we")

        self.boton5= Button (root, text= "%", command= self.calcular_porcentaje)
        self.boton5.grid (row= 5, column= 0, columnspan= 1, sticky= "we")

        self.boton6 = Button (root, text= "Clear", command= self.borrar)
        self.boton6.grid (row= 5, column= 1, columnspan= 2, sticky= "we")

        #- 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
        #3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica
        #es Resultado.
        self.input_text= StringVar()
        self.operador=""

    def sumar(self):
        resultado = self.n1.get() + self.n2.get()
        self.resul.set(resultado)

    def restar (self):
        resultado = self.n1.get() - self.n2.get ()
        self.resul.set(resultado)

    def multiplicar (self):
        resultado = self.n1.get() * self.n2.get()
        self.resul.set (resultado)

    def dividir (self):
        if self.n2.get() != 0:
            resultado = self.n1.get() / self.n2.get()
            self.resul.set (resultado)
        else:
            self.resul.set("ERROR")

    def calcular_porcentaje(self):
        if self.n2.get() != 0:
            resultado = (self.n1.get() * self.n2.get()) / 100
            self.resul.set(resultado)
        else:
            self.resul.set("ERROR")

    def borrar (self):
        self.n1.set(0)
        self.n2.set(0)
        self.resul.set(0)

if __name__ == "__main__":
    root = Tk()
    app = calculadora(root)
    root.geometry ("350x300")
    root.mainloop() 






