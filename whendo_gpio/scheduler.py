"""
These classes initiate action execution from asynchronous
events generated by the GPIO library.
"""
try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO

from whendo.core.scheduler import ThresholdScheduler
from whendo.core.executor import Executor


class PinScheduler(ThresholdScheduler):
    pin: int  # synonymous with 'channel'
    event: int  # GPIO.FALLING, GPIO.RISING, GPIO.BOTH

    def schedule(self, scheduler_name: str, executor: Executor):
        callable = self.during_period(scheduler_name=scheduler_name, executor=executor)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN) 
        GPIO.add_event_detect(self.pin, self.event, callback=lambda pin: callable(), bouncetime=150)

    def unschedule(self, schedule_name: str):
        GPIO.setmode(GPIO.BCM)
        GPIO.remove_event_detect(self.pin)