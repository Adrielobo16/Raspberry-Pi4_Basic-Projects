#PRACTICA 5 / PRENDER LED CON TECLADO 
#Turn a LED with keyboard.
from gpiozero import LED 		#libreria para LED - LED library. 
from time import sleep			#libreria tiempo/sleep.
led = LED(25) 					#pin donde esta declarado el LED - Raspberry pin GPIO for LED
while True:
	print("Do you want turn ON the LED?")
	cmd = input()
	if(cmd == "yes"):
		led.on()				#prende el led - Turn ON the LED:
		sleep(4) 				#prende por 4 segundos - for 4 seconds.
		led.off()				#apaga el led - Turn OFF the LED.
	if(cmd == "no"):
		led.off()				#apaga el led - Turn OFF the LED.
#Follow me on my YouTube channel: https://www.youtube.com/@adrieltrejodearcos3335