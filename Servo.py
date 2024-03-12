import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 50)
pwm.start(0)

pwm.ChangeDutyCycle(5)
sleep(1)
pwm.ChangeDutyCycle(7.1)
sleep(1)
pwm.ChangeDutyCycle(10)
sleep(1)

pwm.stop()
GPIO.cleanup()