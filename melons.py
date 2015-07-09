"""This file should have our melon-type classes in it."""

class Melon(object):
    species = None
    color = None
    imported = None
    shape = None
    seasons = []

    def get_base_price(self, melon_price = 5.00):
        melon_base_price = float(melon_price)
        return melon_base_price 

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def __init__(self, color = "green", imported = False):
        self.color = color
        self.imported = imported

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        watermelon_base_price = self.get_base_price()
        total = watermelon_base_price * qty
        if qty >= 3:
            total = total * 0.75
        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        total = 5.00 * qty
        if qty >= 5:
            total = total / 2.00
        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Winter", "Fall"]

    def get_price(self, qty):
        total = (6.00 * qty) * 1.50
        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True 
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        total = 5.00 * qty * 1.50
        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        total = 5.00 * qty * 1.50
        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
        total = 5.00 * qty
        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        total = 5.00 * qty * 1.50
        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        total = 5.00 * qty * 2.00
        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    season = ["Spring", "Summer"]

    def get_price(self, qty):
        total = 6.00 * qty
        return total

