# С – конвенция (convention)
# R – рефакторинг (refactor)
# W – предупреждение (warning)
# E – ошибка (error)

import sys


class CarClass:
    """"""

    def __init__(self, color, make, model, year):
        """Constructor"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year

        if "Windows" in platform.platform():
            print("You're using Windows!")

        self.weight = self.get_weight(1, 2, 3)

    def get_weight(this):
        """"""
        return "2000 lbs"