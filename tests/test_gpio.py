"""
These tests do nothing useful. They exist for the day
when a better mock gpio library turns up.
"""

from pydantic import BaseModel
import Mock.GPIO as GPIO
import whendo_gpio.action as act


def test_set_pin():
    pin = 25
    action = act.SetPin(pin=pin, on=True)
    assert action.execute()


def test_toggle_pin():
    pin = 25
    action = act.TogglePin(pin=pin)
    assert action.execute()


def test_pin_state():
    pin = 25
    action = act.PinState(pin=pin)
    assert not action.execute()

def test_cleanup_pins():
    pin = 25
    action = act.CleanupPins()
    assert not action.execute()