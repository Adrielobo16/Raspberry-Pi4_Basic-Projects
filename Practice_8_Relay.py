#PRACTICA 8 | Control de un relay
#Code for using a Relay.

from gpiozero import LED 		#libreria para LED|Relay
from time import sleep			#libreria tiempo/sleep.
led = LED(25) 					#pin donde esta declarado el LED - Raspberry pin GPIO for LED.
while True:
	led.on()					#prende el led - Turn ON a LED.
	sleep(1)					#prende por 1 segundo.
	led.off() 					#apaga el led - Turn OFF a LED.
	sleep(1)					#se apaga por un segundo.
#Follow me on my YouTube channel: https://www.youtube.com/@adrieltrejodearcos3335/featured