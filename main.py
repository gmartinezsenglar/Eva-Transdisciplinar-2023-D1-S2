import tkinter

ventana = tkinter.Tk()
ventana.geometry('400x300')

etiqueta = tkinter.Label(ventana, text = ' Programa - ', bg = 'blue')
etiqueta.pack(fill = tkinter.X)

ventana.title(' Eva-Transdisciplinar-2023-D1-S2 ')
ventana.mainloop()