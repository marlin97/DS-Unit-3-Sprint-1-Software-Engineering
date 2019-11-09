#! /usr/bin/env python3

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_flammability(self):
        prod = Product("Some Item")
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability_explode_methods(self):
        prod = Product('Pen', 5, 2, 1.1)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...fizzle.")


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        name_strs = [prod.name.split() for prod in products]
        for name in name_strs:
            self.assertIn(name[0], ADJECTIVES)
            self.assertIn(name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()

