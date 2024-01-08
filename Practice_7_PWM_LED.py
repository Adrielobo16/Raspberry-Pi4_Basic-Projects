#PRACTICA 7 / PWM LED
from gpiozero import PWMLED #libreria PWM con LED
from time import sleep		  #libreria tiempo/sleep.

led = PWMLED(4) 				    #pin donde esta declarado el LED - Raspberry Pin GPIO for LED.

while True:
    #encender led
    for duty_cycle in range(0, 100, 1):
      led.value = duty_cycle/100.0
      sleep(0.05)
    #apagar led
    for duty_cycle in range(100, 0, -1):
      led.value = duty_cycle/100.0
      sleep(0.05)
#Follow me on my YouTube channel: https://www.youtube.com/@adrieltrejodearcos3335/videos