import time
from rpi_ws281x import *
import pygame
import RPi.GPIO as GPIO
import random

pygame.init()

#pour la musique
buble_sound = pygame.mixer.Sound("Buble.mp3")
sensorPin = 11

# LED strip configuration:
LED_COUNT      = 300    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

#musique
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN)




while True:
    time.sleep(1)
    if GPIO.input(sensorPin)==GPIO.HIGH and pygame.mixer.get_busy()== False:
        pygame.mixer.Sound.play(buble_sound)
        print("Mouvement detecte")
        while True:
            previous = -1
            for led_number in range(LED_COUNT):
                randColor=random.randint(0,3)
                while previous == randColor:
                    randColor = random.randint(0, 3)
                previous = randColor
                color = Color(255,255,0)
                if randColor == 0:
                    color = Color(255, 0, 0)
                elif randColor == 1:
                    color = Color(0, 255, 0)
                elif randColor == 2:
                    color = Color(0,0,255)
                strip.setPixelColor(led_number, color)
            strip.show()
            time.sleep(1/2)


"""
            for x in range(25):
                print("XXX")
                print(x)
                value = x*10
                for led_number in range(LED_COUNT):
                    if led_number%2 == 0:
                        strip.setPixelColor(led_number, Color(0, 0, value))

            time.sleep(100 / 1000.0)
            strip.show()

            for led_number in range(LED_COUNT):
                strip.setPixelColor(led_number, Color(0, 0, 0))
                strip.show()
            for x in range(25):
                print("XXX")
                print(x)
                value = x * 10
                for led_number in range(LED_COUNT):
                    if led_number % 2 == 1:
                        strip.setPixelColor(led_number, Color(value, 0, 0))
                strip.show()
                time.sleep(100 / 1000.0)
            for led_number in range(LED_COUNT):
                strip.setPixelColor(led_number, Color(0, 0, 0))
                strip.show()


"""