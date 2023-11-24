# Lab Assignment 30 Phone Book Part One
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program stores and displays contact information for a person using a Contact class

class Contact:
    def __init__(self, name, phone_number, email, address):
        # Initialize the variables for the Contact class
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        # Create a string representation of the Contact
        return f"Name:{self.name},Phone:{self.phone_number},Email:{self.email},Address:{self.address}"

    def formatted_contact(self):
        # Format the contact information
        name_line = f"{'-' * 20} {self.name.upper()} {'-' * 20}"
        phone_line = f"Phone: {self.phone_number}"
        email_line = f"Email: {self.email.lower()}"
        address_line = f"Address: {self.address}"

        # Return the formatted contact information as a string
        return f"{name_line}\n{phone_line}\n{email_line}\n{address_line}\n"

contact = Contact("Aruzhan", "5163697765", "abissenbay@adelphi.edu", "1 South Avenue Garden City NY")

print(contact)

print(contact.formatted_contact())
