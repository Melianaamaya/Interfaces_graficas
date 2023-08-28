from tkinter import *
from tkinter import Listbox

class peliculas():
    def __init__(self, root):
        self.root = root
        self.root.title ("Peliculas")
        self.root.resizable (0,0)


        self.text = StringVar()

        self.label_agregar = Label (root, text= "Añadir el titulo de la pelicula")
        self.label_agregar.grid (row= 0, column= 0, padx= 20, pady= 20)

        self.label_pelic = Label (root, text= "Peliculas")
        self.label_pelic.grid (row= 0, column= 1, padx= 20, pady= 20)


        self.entry_pelicula = Entry(root, textvariable=self.text)
        self.entry_pelicula.grid(row= 1, column= 0, padx= 20, pady= 5)

        
        self.listbox_pelis = Listbox(root)
        self.listbox_pelis.grid(row= 1, column= 1, padx= 20, pady= 5, rowspan= 2)


        self.boton_anadir = Button(root, text="Añadir", command=self.añadir_peliculas)
        self.boton_anadir.grid(row=2, column= 0, padx=20, pady=20)


    def añadir_peliculas(self):
        pelicula = self.entry_pelicula.get()
        if pelicula:
            self.listbox_pelis.insert(END, pelicula)
            self.entry_pelicula.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = peliculas(root)
    root.geometry ("500x500")
    root.mainloop() 