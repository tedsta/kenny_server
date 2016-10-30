#!/usr/bin/env python

import math
import RPIO as rpio
import time
import struct

from motor.motor import *
from motor.pwm import Pwm
from net import *

for pin in [4, 5, 6, 17, 23, 27]:
    rpio.setup(pin, rpio.OUT)

motor = MotorDriver()
motor.rotate(CLOCKWISE, 0.0, MOTOR_A)
motor.rotate(CLOCKWISE, 0.0, MOTOR_B)

"""leds = [Pwm(pin) for pin in [5, 6, 23]]
for led in leds:
    led.set(0)"""

socket = Socket('0.0.0.0', 20001)

start = time.time()
try:
    while True:
        for packet in socket.listen():
            if packet is not None:
                if len(packet) == 0:
                    continue

                # Extract packet ID from packet
                id = struct.unpack('B', packet[0])[0]
                
                if id == 0:
                    # Stop
                    motor.rotate(CLOCKWISE, 0.0, MOTOR_A)
                    motor.rotate(CLOCKWISE, 0.0, MOTOR_B)
                elif id == 1:
                    # Up
                    motor.rotate(COUNTER_CLOCKWISE, 1.0, MOTOR_A)
                    motor.rotate(COUNTER_CLOCKWISE, 1.0, MOTOR_B)
                elif id == 2:
                    # Down
                    motor.rotate(CLOCKWISE, 1.0, MOTOR_A)
                    motor.rotate(CLOCKWISE, 1.0, MOTOR_B)
                elif id == 3:
                    # Left
                    motor.rotate(COUNTER_CLOCKWISE, 1.0, MOTOR_A)
                    motor.rotate(CLOCKWISE, 1.0, MOTOR_B)
                elif id == 4:
                    # Right
                    motor.rotate(CLOCKWISE, 1.0, MOTOR_A)
                    motor.rotate(COUNTER_CLOCKWISE, 1.0, MOTOR_B)
                else:
                    print("Received unrecognized packet ID: %s" % id)
        t = time.time()
        """for i, led in enumerate(leds):
            led.set((math.sin((t - start) * 8.0 + i*3.0) + 1.0) / 2.0)
            led.update(t)"""
        motor.update(t)
except KeyboardInterrupt:
    pass

socket.close()
rpio.cleanup()
