import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.IN) # Left
GPIO.setup(26, GPIO.IN) # Right


while True:
        if GPIO.input(21) == GPIO.input(26):
                print("forward")
        if GPIO.input(21) != 0:
                print("left")
        if GPIO.input(26) !=  0:
                print("right")
