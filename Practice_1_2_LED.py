#Turn ON and OFF a LED.
#PRENDER Y APAGAR UN LED - PRACTICA 1 / 2
from gpiozero import LED 		#libreria para LED - LED library
from time import sleep			#libreria tiempo/sleep 
led = LED(25) 					#pin donde esta declarado el LED - Raspberry Pi 4 Pin for LED.
while True:
	led.on()					#prende el led - Turn On the LED.
	sleep(1)					#prende por 1 segundo - for 1 second.
	led.off() 					#apaga el led - Turn Off the LED.
	sleep(1)					#se apaga por un segundo - for 1 second. 

#Follow me on my YouTube channel: https://www.youtube.com/@adrieltrejodearcos3335