#SEMAFORO- PRACTICA 3
#Traffic Light 
from gpiozero import LED 			#libreria para LED 
from time import sleep				#libreria tiempo/sleep.
ledRojo = LED(23) 					#pin donde esta declarado el LED rojo. 
ledAmarillo = LED(24) 				#pin donde esta declarado el LED amarillo. 
ledVerde = LED(25) 					#pin donde esta declarado el LED verde. 
while True:
	#Green LED
	ledVerde.on()					#prende el led - Turn ON the LED.
	sleep(4)						#prende por 5 segundo.
	ledVerde.off() 					#apaga el led - Turn OFF the LED.
	sleep(1)						#apaga por 5 segundo.
	ledVerde.on()					#prende el led - Turn ON the LED.
	sleep(1)						#prende por 5 segundo.
	ledVerde.off() 					#apaga el led - Turn OFF the LED.
	sleep(1)						#apaga por 5 segundo.
	ledVerde.on()					#prende el led - Turn ON the LED.
	sleep(1)						#prende por 5 segundo.
	ledVerde.off() 					#apaga el led - Turn OFF the LED.
	#Yellow LED
	ledAmarillo.on()				#prende el led - Turn ON the LED.
	sleep(2)						#prende por 2 segundo.
	ledAmarillo.off() 				#apaga el led - Turn OFF the LED.
	#Red LED
	ledRojo.on()					#prende el led - Turn ON the LED.
	sleep(3)						#prende por 3 segundo.
	ledRojo.off() 					#apaga el led - Turn OFF the LED.

#Follow me on my YouTube channel: https://www.youtube.com/@adrieltrejodearcos3335