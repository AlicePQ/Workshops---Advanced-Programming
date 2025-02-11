"""
This module has a simple definition of a shopping cart.

Author: Alicia Pineda Quiroga <apinedaq@udistrital.edu.co>

This file is part of Workshop_3_AP-UD.

Workshop_3_AP-UD is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop_3_AP-UD is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop_3_AP-UD. If not, see <https://www.gnu.org/licenses/>. 
"""

from catalog import Catalog

class ShoppingCart:
    """Class to represent a shopping cart."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        # A dictionary to store items and their quantities
        self.cart = {}

    def add_to_cart(self, category, product, quantity):
        """
        Adds a product to the shopping cart.

        Parameters:
        category (str): The category of the product.
        product (str): The name of the product.
        quantity (int): The quantity of the product to add.
        """
        if (category, product) in self.cart:
            self.cart[(category, product)] += quantity
        else:
            self.cart[(category, product)] = quantity

    def show_cart(self):
        """Displays the content of the shopping cart."""
        print("Shopping Cart:")
        if not self.cart:
            print("Your cart is empty.")
        else:
            for (category, product), quantity in self.cart.items():
                print(f"{product} ({category}) - {quantity} units")