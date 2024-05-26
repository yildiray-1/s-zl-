from machine import Pin
from time import sleep

IN1 = Pin(19,Pin.OUT)
IN2 = Pin(18,Pin.OUT)
IN3 = Pin(5,Pin.OUT)
IN4 = Pin(17,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for step in sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.001)
