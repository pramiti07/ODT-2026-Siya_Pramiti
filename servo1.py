from machine import Pin, PWM
import time
servo=PWM(12,Pin.OUT)
servo.freq(50)  
def set_angle(angle):
    
    duty = int(angle)
    servo.duty(duty)

while(1):
    
    set_angle(45)
    print("0 degree")
    time.sleep(2)
    
    set_angle(90)
    print("90 degree")
    time.sleep(2)
    
