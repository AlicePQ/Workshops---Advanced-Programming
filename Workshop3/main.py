"""
This module contains a set of classes to handle
electronic devices using categories, searchs, 
among others functionalities.

Author:Alicia Pineda Quiroga <apinedaq@udistrital.edu.co>

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
from shoppingCart import ShoppingCart
from checkout import Checkout

def display_menu():
    """Displays the main menu and gets user choice"""
    print("\nWelcome to the Electronics Store")
    print("In our store you can find a variety of electronic devices, select the best option from the menu below to find what you're looking for.")
    print("1. Show categories List")
    print("2. Show products list")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Choose an option: ")
    return choice

def main():
    """Main loop to display menu and handle user choices"""

    # Initialize the catalog, shopping cart, and checkout instances
    catalog = Catalog()
    cart = ShoppingCart()
    checkout = Checkout()

    while True:
        choice = display_menu()  # Display the main menu and get user choice

        # Main menu options
        if choice == "1":
            catalog.show_categories()
            while True:
                print("1. Check products by category")
                print("2. Back to main menu")
                answer = input("Choose an option: ")
                if answer == "1":
                    category = input("Enter the name of the category: ")
                    if category in catalog.categories:
                        catalog.show_products_by_category(category)
                        while True:
                            print("1. Add product to cart")
                            print("2. Back to category menu")
                            answer = input("Choose an option: ")

                            if answer == "1":
                                try:
                                    product_index = int(input("Enter product number: ")) - 1
                                    quantity = int(input("Enter quantity of the product you want to add to the cart: "))
                                    if product_index < 0 or product_index >= len(catalog.categories[category]["products"]):
                                        print("Invalid product number.")
                                    elif quantity <= 0:
                                        print("Quantity must be positive.")
                                    else:
                                        product = catalog.categories[category]["products"][product_index]
                                        cart.add_to_cart(category, product, quantity)
                                        print(f"{quantity} units of {product} added to the cart successfully.")
                                except ValueError:
                                    print("Invalid input. Please enter valid numbers.")

                            elif answer == "2":
                                break
                    else:
                        print("Category not found.")
                elif answer == "2":
                    break
                else:
                    print("Invalid option. Please try again.")
        
        elif choice == "2":
            catalog.show_products()
            while True:
                print("1. Back to main menu")
                answer = input("Choose an option: ")
                if answer == "1":
                    break
            
        elif choice == "3":
            cart.show_cart()
            while True:
                print("1. Complete Checkout")
                print("2. Back to main menu")
                answer = input("Choose an option: ")
                if answer == "1":
                    checkout.get_customer_info()
                    print("Delivery confirmation:\n")
                    checkout.show_customer_info()
                    print("Electronic devices selected: \n")
                    cart.show_cart()
                    print("Thank you for shopping with us!\n")
                    break

                elif answer == "2":
                    break

        elif choice == "4":
            while True:
                print("1. Complete Checkout")
                print("2. Back to main menu")
                answer = input("Choose an option: ")

                if answer == "1":
                    checkout.get_customer_info()
                    print("Delivery confirmation:\n")
                    checkout.show_customer_info()
                    print("Electronic devices selected: \n")
                    cart.show_cart()
                    print("Thank you for shopping with us!\n")
                    break  

                elif answer == "2":
                    break
            
        elif choice == "5":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()