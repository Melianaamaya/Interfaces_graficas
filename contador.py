from tkinter import * 

class contador:
    def __init__(self, root):
        self.root= root
        self.root.title ("Contador")
        self.root.resizable (0,0)
        
        self.contador = IntVar (value= 0)

        self.label = Label (root, text= "Contador")
        self.label.grid (row=0, column=0)

        self.valor_contador = StringVar ()
        self.valor_contador.set (str(self.contador.get()))

        self.edit = Entry (root, textvariable= self.contador, state= "readonly")
        self.edit.grid (row=0, column=1)

        self.boton1 = Button (root, text= "Count up", command= self.count_up)
        self.boton1.grid (row=0, column=2)

        self.boton2 = Button (root, text= "count down", command= self.count_down)
        self.boton2.grid (row=0, column= 3)

        self.boton3 = Button (root, text= "Reset", command= self.reset)
        self.boton3.grid (row=0, column= 4)

    def count_up(self):
        self.contador.set(self.contador.get() + 1)
        self.valor_contador.set(str(self.contador.get()))

    def count_down(self):
        self.contador.set(self.contador.get() - 1)
        self.valor_contador.set(str(self.contador.get()))
    
    def reset (self):
        self.contador.set (0)
        self.valor_contador.set(str(self.contador.get()))


if __name__ == "__main__":
    root = Tk()
    app = contador(root)
    root.geometry ("500x50")
    root.mainloop() 

