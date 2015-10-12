import RPi.GPIO as GPIO                    
import time                              
GPIO.setmode(GPIO.BCM)

TRIG = 24 #Change to match GPIO pins used
ECHO = 25
GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)

print("Measuring the distance!")
while True:
    GPIO.output(TRIG, 0)
    time.sleep(2) # Wait for sensor to settle

    GPIO.output(TRIG, 1) # Sending out a signal
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_length = pulse_end - pulse_start
    distance = pulse_length * 17150

    print(distance)
