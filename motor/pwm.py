import RPIO as rpio

class Pwm:
	def __init__(self, pin, frequency=50):
		self.pin = pin
		self.period = 1.0 / frequency
		self.last_cycle = 0.0
		self.duty_cycle = 0.0
		self.on = True
		rpio.output(self.pin, True)

	def update(self, t):
		delta = t - self.last_cycle
		if self.on and delta > self.duty_cycle*self.period:
			rpio.output(self.pin, False)
			self.on = False
		elif delta > self.period:
			rpio.output(self.pin, True)
			self.on = True
			self.last_cycle = t

	def set(self, duty_cycle):
		self.duty_cycle = duty_cycle

	def get(self):
		return self.duty_cycle
