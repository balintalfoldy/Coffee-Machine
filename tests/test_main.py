from coffee import main
import pytest


def test_init():
    cm = main.CoffeeMachine()
    assert cm.coffee_tank == 100
    assert cm.water_tank == 1000
    assert cm.counter == 0


def test_brew():
    cm = main.CoffeeMachine()
    cm.brew('americano')
    assert cm.coffee_tank == 90
    assert cm.water_tank == 760
    assert cm.counter == 1
