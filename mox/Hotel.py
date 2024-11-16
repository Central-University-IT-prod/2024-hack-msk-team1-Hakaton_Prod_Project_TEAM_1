from config import *
from random import choice

class Hotel:

    def __init__(self, price=None, name=None):
        self.price = price
        self.name = name

    def fill(self):  # FILL RICHARDS
        return Hotel(
            choice(HOTEL_PRICES),
            choice(HOTEL_NAMES)
        )
