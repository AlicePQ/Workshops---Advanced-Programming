"""
This module contains a class to handle a catalog including some 
search methods.

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

class Catalog:
    """Class to represent a catalog of electronic devices."""

    def __init__(self):
        """Initializes the catalog with categories, products, and their quantities."""
        # Categories and their respective products and quantities
        self.categories = {
            "Computers": {
                "products": ["Mac", "Lenovo", "Acer", "Asus"],
                "quantities": [20, 15, 20, 45]
            },
            "Laptops": {
                "products": ["Laptop A", "Laptop B", "Laptop C"],
                "quantities": [10, 20, 30]
            },
            "Smartphones": {
                "products": ["Smartphone A", "Smartphone B", "Smartphone C"],
                "quantities": [15, 25, 30]
            }
        }

    def show_categories(self):
        """Displays the available categories with enumeration."""
        print("Categories:")
        for category in self.categories:
            print(f"- {category}")

    def show_products_by_category(self, category):
        """
        Displays products and their quantities for a given category.

        Parameters:
        category (str): The name of the category to display products for.
        """
        if category in self.categories:
            print(f"Products in {category}:")
            products = self.categories[category]["products"]
            quantities = self.categories[category]["quantities"]
            for i, product in enumerate(products):
                print(f"{i+1}. {product} - {quantities[i]} units available")
        else:
            print("Category not found.")

    def show_products(self):
        """Displays all the products available in the store."""
        print("Products:")
        product_number = 1
        for category in self.categories.values():
            for product in category["products"]:
                print(f"{product_number}. {product}")
                product_number += 1
