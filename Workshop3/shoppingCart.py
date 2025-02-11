"""
This module has a simple definition of a shopping cart and also a web server with Flask
to manage the shopping cart, allowing to add and remove items from it, you must 
have flask installed in your system.

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

from flask import Flask, jsonify, request
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

# Flask app setup
app = Flask(__name__)
shopping_cart = ShoppingCart()

@app.route('/cart', methods=['GET'])
def view_cart():
    """
    Web service to view the shopping cart.
    Name: view_cart
    Endpoint: /cart
    HTTP Method: GET
    Inputs: None
    Outputs: List of products in the cart with quantities and total
    """
    cart_content = shopping_cart.show_cart()
    total_items = sum(cart_content.values())
    response = {
        "products": [{"category": category, "product": product, "quantity": quantity} 
                     for (category, product), quantity in cart_content.items()],
        "total_items": total_items
    }
    return jsonify(response)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """
    Web service to add a product to the shopping cart.
    Name: add_to_cart
    Endpoint: /cart/add
    HTTP Method: POST
    Inputs: product_id, quantity
    Outputs: Confirmation that the product was added to the cart
    """
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({"error": "Missing required fields"}), 400

    # Assuming you have a way to get the product details from the product_id
    # For example, using a Catalog instance
    catalog = Catalog()
    product = None
    category = None
    for cat_name, cat_data in catalog.categories.items():
        if product_id in cat_data["products"]:
            product = product_id
            category = cat_name
            break

    if not product or not category:
        return jsonify({"error": "Product not found"}), 404

    shopping_cart.add_to_cart(category, product, quantity)
    return jsonify({"message": "Product added to cart"}), 200

if __name__ == '__main__':
    app.run(debug=True)