import tkinter as tk

class ContCrecienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ContCreciente")

        self.root.configure (bg= "lavender")
        
        self.contador = 0

        self.label = tk.Label(root, text="Contador")
        self.label.pack()

        self.valor_contador = tk.StringVar()
        self.valor_contador.set(str(self.contador))
        
        self.line_edit = tk.Entry(root, textvariable=self.valor_contador, state='readonly')
        self.line_edit.pack()

        self.boton_mas = tk.Button(root, text="+", bg= "cyan4", command=self.incrementar_contador)
        self.boton_mas.pack()

    def incrementar_contador(self):
        self.contador += 1
        self.valor_contador.set(str(self.contador))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContCrecienteApp(root)
    root.geometry ("350x100")
    root.mainloop() 