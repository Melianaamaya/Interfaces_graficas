from tkinter import *   
from tkinter import Spinbox
import random

class generador_de_numeros():
    def __init__ (self, root):
        self.root= root
        self.root.title ("Generador de números")
        self.root.resizable (0,0)
        self.root.configure (bg= "pink")

        self.label_n1 = Label (root, text= "Numero 1")
        self.label_n1.grid (row= 0, column= 0, padx= 20, pady= 20)

        self.label_n2 = Label (root, text= "Número 2")
        self.label_n2.grid (row= 1, column= 0, padx= 20, pady= 20)

        self.spin_n1 = Spinbox(root, from_=0, to=100)
        self.spin_n1.grid(row=0, column=1, padx=20, pady=20)

        self.spin_n2 = Spinbox(root, from_=0, to=100)
        self.spin_n2.grid(row=1, column=1, padx=20, pady=20)

        self.label_generado = Label(root, text="Número Generado")
        self.label_generado.grid(row=2, column=0, padx=20, pady=20)

        self.resultado = Entry(root, state="readonly")
        self.resultado.grid(row=2, column=1, padx=20, pady=20)

        self.boton_generar = Button(root, text="Generar", command=self.generar_numero)
        self.boton_generar.grid(row=3, columnspan=2, padx=20, pady=20)

    def generar_numero(self):
        min_valor = int(self.spin_n1.get())
        max_valor = int(self.spin_n2.get())
        numero_generado = random.randint(min_valor, max_valor)
        self.resultado.config(state="normal")
        self.resultado.delete(0, END)
        self.resultado.insert(0, str(numero_generado))
        self.resultado.config(state="readonly")

if __name__ == "__main__":
    root = Tk()
    app = generador_de_numeros(root)
    root.geometry ("500x500")
    root.mainloop() 