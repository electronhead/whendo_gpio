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
    """
    Detects a change to pin in one direction or both directions.
    """
    pin: int  # synonymous with 'channel'
    event: int  # GPIO.FALLING, GPIO.RISING, GPIO.BOTH

    def description(self):
        return f"Executes a callback based on a supplied scheduler_name if a selected event has been detected in pin ({self.pin}). [GPIO.RISING ({GPIO.RISING}), GPIO.FALLING ({GPIO.FALLING}), GPIO.BOTH({GPIO.BOTH})] {super().description()}"

    def schedule(self, scheduler_name: str, executor: Executor):
        callable = self.during_period(scheduler_name=scheduler_name, executor=executor)
        GPIO.setmode(GPIO.BCM)
        # GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN) 
        GPIO.add_event_detect(self.pin, self.event, callback=lambda pin: callable(), bouncetime=150)

    def unschedule(self, schedule_name: str):
        GPIO.setmode(GPIO.BCM)
        # GPIO.setwarnings(False)
        GPIO.remove_event_detect(self.pin)
