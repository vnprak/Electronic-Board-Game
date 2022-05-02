import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

def info():
    '''Prints a basic library description'''
    print("Software library for the Electronic Board Game project.")
    
def all_LED_on():
    print("All LEDs ON")
    
def all_LED_off():
    print("All LEDs OFF")
    
def LED_on(num):
    print("LED " + str(num) + " ON")
    
def LED_off(num):
    print("LED " + str(num) + " OFF")
    
def gpio_button_setup(pin):
    GPIO.setup(pin, GPIO.IN)

def gpio_button_read(pin):
    return GPIO.input(pin)
    
def gpio_button_wait(pin):
    GPIO.wait_for_edge(pin, GPIO.RISING)