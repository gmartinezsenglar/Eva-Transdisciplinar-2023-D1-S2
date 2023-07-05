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
#-                      Inicialización de ventana                           -
#----------------------------------------------------------------------------

ventana = tkinter.Tk()
ventana.resizable(0,0)      # --> Para que usuario no pueda redimensionar la ventana
ventana.geometry(res)       # --> Agregando las dimensiones a la ventana
ventana.configure(background="AliceBlue")

#----------------------------------------------------------------------------
#-                      Etiquetas y ventanas                                -
#----------------------------------------------------------------------------

etiqueta = tkinter.Label(ventana, text = ' Calculadora de energía cinética ', font = ('Arial', 14), bg = 'cyan')
etiqueta.pack(fill = tkinter.X)

etiquetaMasa = tkinter.Label(ventana, text = 'Masa (kg):', font = ('Arial', 12), bg = 'AliceBlue')
etiquetaMasa.pack()
ingresoMasa = tkinter.Entry(ventana, font = ('Arial', 12), bg = 'AntiqueWhite2')
ingresoMasa.pack()

etiquetaVelocidad = tkinter.Label(ventana, text = 'Velocidad (kg):', font=('Arial', 12), bg = 'AliceBlue')
etiquetaVelocidad.pack()
ingresoVelocidad = tkinter.Entry(ventana, font=('Arial', 12), bg = 'AntiqueWhite2')
ingresoVelocidad.pack()

etiquetaResultado = tkinter.Label(ventana, text = '', font = ('Arial', 12), fg = 'blue')
etiquetaResultado.pack()

#----------------------------------------------------------------------------
#-                      Operatoria y botón que la ejecuta                   -
#----------------------------------------------------------------------------

def operacion():
    try:
        masa = float(ingresoMasa.get())
        velocidad = float(ingresoVelocidad.get())
        energiaCinetica = 0.5 * masa * velocidad**2
        etiquetaResultado.config(text="La energía cinética es: {:.2f} Joules".format(energiaCinetica))
    except ValueError:
        etiquetaResultado.config(text="Error: ingresa valores numéricos")

botonCalcular = tkinter.Button(ventana, text = 'Calcular', command = operacion, font = ('Arial', 12), bg = 'lightblue')
botonCalcular.pack(pady = 10)

#----------------------------------------------------------------------------
#-                      Inicia el programa                                  -
#----------------------------------------------------------------------------

ventana.mainloop()