#PRACTICA 6 | Prender y apagar un LED con interfaz de Python.
#Turn ON a LED with Python interface. 
import tkinter as tk 											#Libreria - Library
from gpiozero import LED										#libreria LED - LED library
ventana = tk.Tk() 												#sirve para los widgets
ventana.title("Prender o Apagar LED")
ventana.geometry("200x200")										#window size 
ventana.config(background = "orange")							#color del fondo. 
led = LED(25)													#pin donde esta declarado 
def encender(): 												#funcion para prender led
	led.on()	
def apagar(): 													#funcion para apagar led
	led.off()													
boton = tk.Button(ventana,text = "Encender", command = encender)#creamos boton
boton.place(x=50 , y=80) 										#donde aparecera el boton
boton1 = tk.Button(ventana,text = "Apagar", command = apagar)	#creamos boton
boton1.place(x=150 , y=80) 										#donde aparecera el boton
ventana.mainloop() 												#muestra la ventana

#Follow me on my YouTube channel: https://www.youtube.com/@adrieltrejodearcos3335