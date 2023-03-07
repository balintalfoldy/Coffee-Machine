from typing import Dict
import numpy as np
import time

test_arr = np.array([1,2,3])

class CoffeeMachine():
    """Coffee machine class for making coffee.
    """
    RECIPE = {
        'espresso': {'coffee': 10,
                     'water': 60},
        'americano': {'coffee': 10,
                      'water': 240},
        'lungo': {'coffee': 20,
                  'water': 150},
        'ristretto': {'coffee': 10,
                  'water': 40}
                  }

    def __init__(self):
        self.coffee_tank = 100
        self.water_tank = 1000
        self.counter = 0

    def print_help(self):
        print("To brew coffee use the brew command and "
              "set the recipe you want to drink.")

    def brew(self, recipe: str):
        """Brew coffee.

        Args:
            recipe (str): type of coffee
        """
        coffee = self.RECIPE.get(recipe)

        self._check_before(coffee)

        print(f'Brewing my {recipe}')
        self.counter += 1
        self.coffee_tank -= coffee.get('coffee')
        self.water_tank -= coffee.get('water')

        if self.counter >= 10:
            self.maintanence()

    def maintanence(self):
        """Run maintenence program.
        """
        print('Executing maintanence...')
        self.counter = 0

    def restart(self):
        """
        Restart machine.
        """
        print('Restarting...')
        time.sleep(5)

    def _check_before(self, coffee: Dict):
        """Check machine status.

        Args:
            coffee (Dict): type of coffee.
        """
        if self.coffee_tank < coffee.get('coffee'):
            print('refilling coffee ...')
            self.coffee_tank = 100

        if self.water_tank < coffee.get('water'):
            print('refilling water ...')
            self.water_tank = 1000
    
    @property
    def recipies(self):
        return self.RECIPE
