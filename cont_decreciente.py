import tkinter as tk

class ContCrecienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title = ("ContDecreciente")
        self.contador = 88
        self.resizable = (0,0)

        self.label = tk.Label (root, text= "Contador")
        self.label.grid (row= 0, column= 0)

        self.valor_contador = tk.StringVar ()
        self.valor_contador.set (str(self.contador))

        self.line_edit = tk.Entry(root, textvariable=self.valor_contador, state='readonly')
        self.line_edit.grid (row= 0, column= 1)

        self.boton_menos = tk.Button(root, text="-", command=self.disminuir_contador)
        self.boton_menos.grid (row=0, column=3)


    def disminuir_contador(self):
        self.contador -= 1
        self.valor_contador.set(str(self.contador))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContCrecienteApp(root)
    root.geometry ("200x50")
    root.mainloop() 
