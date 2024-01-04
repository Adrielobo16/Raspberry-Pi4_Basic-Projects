#PRACTICA 4 / PRENDER LED CON PUSH BUTTON 
#Turn ON a LED with push button.
from gpiozero import LED 		#libreria para LED 
from gpiozero import Button 	#libreria para push button.
from time import sleep			#libreria tiempo/sleep.
button = Button(25) 			#pin donde esta declarado el boton. 
led = LED(24) 					#pin donde esta declarado el led. 
while True:
	button.wait_for_press() 	#funcion que lee estado del boton.
	led.on()					#enciende el led.
	sleep(1)					#prende por 3 segundos.
	led.off()					#apaga el led.

#Follow me on YouTube: https://www.youtube.com/@adrieltrejodearcos3335