from machine import Pin, PWM
import time

servo = PWM(Pin(12), freq=50)

def set_angle(angle):
    duty = int((angle / 180) * 75 + 40)
    servo.duty(duty)

LOW = 30
HIGH = 130   # bigger angle

while True:
    set_angle(HIGH)
    time.sleep(0.04)

    set_angle(LOW)
    time.sleep(0.04)