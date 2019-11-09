#! /usr/bin/env python3

import random


class Product:
    """
    The acme product class, holds the data for every product they sell
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """Calculates the stealability of the product based on the ratio between its price and weight"""
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif 0.5 <= ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Calculates if the product may explode based in its weight, and flammability"""
        combustible = self.flammability * self.weight
        if combustible < 10:
            return "...fizzle."
        elif 10 <= combustible < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    This class inherits from the Product class, as it is a specific product
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """NO NO NO, gloved do not explode"""
        return "...it's a glove."

    def punch(self):
        """How much pain each weight of glove can produce"""
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

