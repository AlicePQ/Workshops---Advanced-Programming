"""
This module contains a class to define the delivery user information in the application.

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

import re 

class Checkout:
    """Class to handle the checkout process."""

    def __init__(self):
        """Initializes the Checkout class with an empty customer_info dictionary."""
        self.customer_info = {}

    def get_customer_info(self):
        """Collects customer information for delivery."""
        print("Please enter your delivery information:")
        self.customer_info["name"] = self._get_valid_input("Name: ", self._validate_non_empty)
        self.customer_info["address"] = self._get_valid_input("Address: ", self._validate_non_empty)
        self.customer_info["phone"] = self._get_valid_input("Phone: ", self._validate_phone)

    def show_customer_info(self):
        """Displays the collected customer information."""      
        print("Customer Information:")
        for key, value in self.customer_info.items():
            print(f"{key.capitalize()}: {value}")

    def _get_valid_input(self, prompt, validation_func):
        """
        Helper method to get valid input from the user.

        Parameters:
        prompt (str): The input prompt to display to the user.
        validation_func (function): The validation function to validate the input.

        Returns:
        str: The validated input from the user.
        """
        while True:
            value = input(prompt)
            if validation_func(value):
                return value
            else:
                print("Invalid input. Please try again.")

    def _validate_non_empty(self, value):
        """
        Validation function to check if the input is not empty.

        Parameters:
        value (str): The input value to validate.

        Returns:
        bool: True if the input is not empty, False otherwise.
        """
        return bool(value.strip())

    def _validate_phone(self, value):
        """
        Validation function to check if the phone number is valid.

        Parameters:
        value (str): The input value to validate.

        Returns:
        bool: True if the phone number is valid, False otherwise.
        """
        return re.match(r'^\+?1?\d{9,15}$', value) is not None