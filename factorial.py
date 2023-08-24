import tkinter as tk

class factorialApp: 
    def __init__ (self, root):
        self.root = root
        self.root.title ("Factorial")
        self.root.resizable (0,0)

        self.n1 = tk.IntVar (value=0)
        self.n2 = tk.StringVar ()

        self.label = tk.Label (self.root, text= "n")
        self.label.grid (row=0, column=0)

        self.label = tk.Label (self.root, text= "Factorial (n)")
        self.label.grid (row=0, column=2)


        self.edit1 = tk.Entry (self.root, textvariable= self.n1, state= "readonly")
        self.edit1.grid (row=0, column=1)
        self.edit2 = tk.Entry (self.root, textvariable= self.n2, state= "readonly")
        self.edit2.grid (row=0, column=3)

        self.boton = tk.Button (self.root, text= "Siguiente", command= self.factoreo)
        self.boton.grid (row=0, column=4)

    def factoreo (self):
        self.n1.set (self.n1.get () +1)

        factorial =1 
        for i in range (1, (self.n1.get()) +1):
            factorial = factorial * i
            self.n2.set(factorial)

if __name__ == "__main__":
    root = tk.Tk()
    app = factorialApp(root)
    root.geometry ("500x50")
    root.mainloop() 
