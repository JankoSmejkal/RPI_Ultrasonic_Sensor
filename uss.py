# Import libraries
from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import time

# Set GPIO pins
GPIO.setmode(GPIO.BCM) # BOARD does not work with gpiozero library (I did not put much effort into making it work with BOARD)
sensor = DistanceSensor(echo = 14, trigger = 15) # Sensor's echo and trigger pin
GPIO.setup(25, GPIO.OUT) # LED pin

try:
    while True:
        GPIO.output(25, True)
        time.sleep(sensor.distance) # Use distance value from sensor to control LED blinking frequency
        GPIO.output(25,False)
        time.sleep(sensor.distance) #  Use distance value from sensor to control LED blinking frequency

except KeyboardInterrupt:
    # Press CTRL + C to interrupt (quit) and cleanup pins
    GPIO.cleanup()
