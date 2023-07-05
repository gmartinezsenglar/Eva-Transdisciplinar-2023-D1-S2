#----------------------------------------------------------------------------
#-                      Calculadora energía cinética                        -
#----------------------------------------------------------------------------

import tkinter

#----------------------------------------------------------------------------
#-                      Constantes                                          -
#----------------------------------------------------------------------------

gravedad = 9.8
res = '300x270'

#----------------------------------------------------------------------------
#-                      Creación de la ventana                              -
#----------------------------------------------------------------------------

ventana = tkinter.Tk()
ventana.resizable(0,0)      # --> Para que usuario no pueda redimensionar la ventana
ventana.geometry(res)       # --> Agregando las dimensiones a la ventana
ventana.configure(background="AliceBlue")

etiqueta = tkinter.Label(ventana, text = ' Calculadora de energía cinética ', font = ('Arial', 14), bg = 'cyan')
etiqueta.pack(fill = tkinter.X)

# Etiqueta y entrada para la masa
etiquetaMasa = tkinter.Label(ventana, text = 'Masa (kg):', font = ('Arial', 12), bg = 'AliceBlue')
etiquetaMasa.pack()
ingresoMasa = tkinter.Entry(ventana, font = ('Arial', 12), bg = 'AntiqueWhite2')
ingresoMasa.pack()

etiquetaVelocidad = tkinter.Label(ventana, text = 'Velocidad (kg):', font=('Arial', 12), bg = 'AliceBlue')
etiquetaVelocidad.pack()
ingresoVelocidad = tkinter.Entry(ventana, font=('Arial', 12), bg = 'AntiqueWhite2')
ingresoVelocidad.pack()

ventana.mainloop()