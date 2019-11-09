#! /usr/bin/env python3

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Randomly generate a given number of product objects, default of 30
    :param num_products: Number of product objects to randomly generate
    :returns: Random list of Person Objects
    """
    products = []
    for __ in range(num_products):
        name = f"{sample(ADJECTIVES, 1)[0]} {sample(NOUNS, 1)[0]}"
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        product = Product(name=name, price=price, weight=weight, flammability=flammability)
        products.append(product)
    return products


def inventory_report(products):
    """
    Prints a report of each person object from a list
    :param products: List of randomly generated product objects
    """
    num_prods = len(products)
    all_names = []
    prices = 0
    weights = 0
    flammable = 0.0
    for prod in products:
        all_names.append(prod.name)
        prices = prices + prod.price
        weights = weights + prod.weight
        flammable = flammable + prod.flammability
    unique_names = set(all_names)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {len(unique_names)}")
    print(f"Average price: {prices / num_prods}")
    print(f"Average weight: {weights / num_prods}")
    print(f"Average flammability: {flammable / num_prods}")

if __name__ == '__main__':
    inventory_report(generate_products())

