import RPIO as rpio
from pwm import Pwm

# GLOBAL CONSTANTS
MOTOR_A_PIN1 = 4
MOTOR_A_PIN2 = 17
MOTOR_B_PIN1 = 6
MOTOR_B_PIN2 = 23

MOTOR_A = 0
MOTOR_B = 1

CLOCKWISE = 0
COUNTER_CLOCKWISE = 1

class Motor:
    def __init__(self, pwm_pin):
        self.pwm = Pwm(pwm_pin, 50)
        self.direction = 0
        self.position = 0 # for stepper motor

class MotorDriver:
    def __init__(self):
        self.motor_a = Motor(27)
        self.motor_b = Motor(5)

    def update(self, t):
        self.motor_a.pwm.update(t)
        self.motor_b.pwm.update(t)

    def rotate(self, direction, speed, motorID):
        pin1_level = 0
        pin2_level = 0
        if direction == CLOCKWISE:
            pin1_level = False
            pin2_level = True
        else:
            pin1_level = True
            pin2_level = False

        if motorID == MOTOR_A:
            self.motor_a.pwm.set(speed)
            rpio.output(MOTOR_A_PIN1, pin1_level)
            rpio.output(MOTOR_A_PIN2, pin2_level)
        elif motorID == MOTOR_B:
            self.motor_b.pwm.set(speed)
            rpio.output(MOTOR_B_PIN1, pin1_level)
            rpio.output(MOTOR_B_PIN2, pin2_level)
        else:
            raise Exception('ERROR: Invalid motor ID %s' % motorID)
