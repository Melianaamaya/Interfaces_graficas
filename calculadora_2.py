from tkinter import *
from tkinter import Radiobutton

class calculadora_2 ():
    def __init__ (self, root):
        self.root = root
        self.root.title ("Calculadora 2")

        self.v1 = IntVar ()
        self.v2 = IntVar ()
        self.resul = IntVar (value= 0)

        self.label_v1 = Label (root, text= "Valor 1")
        self.label_v1.grid (row= 1, column= 0, padx= 20, pady= 20)

        self.label_v2 = Label (root, text= "Valor 2")
        self.label_v2.grid (row= 2, column= 0, padx= 20, pady= 20) 

        self.label_result = Label (root, text= "Resultado")
        self.label_result.grid (row= 3, column= 0, padx= 20, pady= 20)

        self.label_opera = Label (root, text= "Operaciones")
        self.label_opera.grid (row= 0, column= 2, padx= 60, pady= 20)

        self.selected_operation = StringVar()

        operations = ['Suma', 'Resta', 'Multiplicación', 'División']
        row_counter = 1
        for operation in operations:
            rb = Radiobutton(root, text=operation, variable=self.selected_operation, value=operation)
            rb.grid(row=row_counter, column=2)
            row_counter += 1

        self.entry_v1 = Entry (root, textvariable= self.v1)
        self.entry_v1.grid(row=1, column=1, padx=20, pady=20)

        self.entry_v2 = Entry(root, textvariable= self.v2)
        self.entry_v2.grid(row=2, column=1, padx=20, pady=20)

        self.entry_result = Entry(root, textvariable= self.resul, state= "readonly")
        self.entry_result.grid(row=3, column= 1, padx=20, pady=20)

        self.boton_calc = Button (root, text= "Calcular", command= self.calcular)
        self.boton_calc.grid (row= 4, column= 1, padx= 20, pady= 20)

    def calcular (self):
        operation = self.selected_operation.get()
        valor1 = self.v1.get()
        valor2 = self.v2.get()

        if operation == 'Suma':
            result = valor1 + valor2
        elif operation == 'Resta':
            result = valor1 - valor2
        elif operation == 'Multiplicación':
            result = valor1 * valor2
        elif operation == 'División':
            result = valor1 / valor2 if valor2 != 0 else "Error"

        self.resul.set(result)

if __name__ == "__main__":
    root = Tk()
    app = calculadora_2(root)
    root.geometry ("450x350")
    root.mainloop() 