# ME 4550 Mechatronics Lab 
# LAB 1: BASIC PICO AND PROGRAMMING
# EXERCISE 3: LED Control with Potentiometer and Pico
# Created by Jack Starke and April Trimmer (9/06/2024)

from machine import Pin
import machine as mach
from machine import PWM
from machine import ADC

while 1:
    pot = ADC(26)                       # potentiometer signal converted from analog to digital on pin 26
    pot_value = pot.read_u16()          # read potentiometer 
    pwmPin27 = PWM(Pin(27), freq= 1000) # use pwm output w/ set freq. to LED w/ Pin 27
    P27 = pwmPin27.duty_u16(pot_value)  # duty cycle is based off of potentiometer value
    print(pot_value)                    # prints potetiometer value just for good measure
