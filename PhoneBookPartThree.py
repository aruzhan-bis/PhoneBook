# Lab Assignment 30 Phone Book Part Three
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program manages a list of contacts, adds, removes, edits and displays them,
# As well as saves and loads them to/from a file.

# The Contact class represents a person's contact information,
# Including their name, phone number, email, and address.
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

# The PhoneBook class manages a list of contacts and
# Provides basic methods for interacting with them.
class PhoneBook:
    def __init__(self):
        # Initialize the phone book with an empty list
        self.contacts = []

    def add_contact(self, contact):
        # Add a contact object to the phone book
        self.contacts.append(contact)

    def get_contact(self, name):
        # Get a contact object by name from the phone book
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        # Give an error if the contact is not found
        raise ValueError(f"No contact found with name '{name}'")

    def remove_contact(self, name):
        # Remove a contact object by name from the phone book
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                return self.contacts.pop(i)
        # Give an error if the contact is not found
        raise ValueError(f"No contact found with name '{name}'")

    def add_new_entry(self):
        # Prompt the user for information to create a new contact object
        name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        address = input("Enter the contact's address: ")
        # Create a new contact object with the given information
        contact = Contact(name, phone_number, email, address)
        # Add the new contact to the phone book
        self.add_contact(contact)

    def print_formatted_phonebook(self):
        for contact in self.contacts:
            print(contact.formatted_contact())

    def save_phonebook(self, filename):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                file.write(str(contact) + '\n')
        print("Phonebook saved successfully!")

    def load_phonebook(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    name = data[0].split(':')[1]
                    phone = data[1].split(':')[1]
                    email = data[2].split(':')[1]
                    address = data[3].split(':')[1]
                    contact = Contact(name, phone, email, address)
                    self.add_contact(contact)
            print("Phonebook loaded successfully!")
        except FileNotFoundError:
            print("Error: File not found.")

# Create an interactive session to test the PhoneBook class
phone_book = PhoneBook()

print("Welcome to the Phonebook!")

while True:
    print("\nChoose your option:")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Edit a contact")
    print("4. Get a contact")
    print("5. Display all Contacts in a readable list")
    print("6. Save all contacts to a plain text file")
    print("7. Load all Contacts from a file you saved earlier")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add a contact
        phone_book.add_new_entry()
        print("Contact added successfully!")
    elif choice == "2":
        # Remove a contact
        name = input("Enter the contact's name: ")
        try:
            contact = phone_book.remove_contact(name)
            print(f"Contact '{contact.name}' removed successfully!")
        except ValueError as e:
            print(str(e))
    elif choice == "3":
        # Edit a contact
        name = input("Enter the contact's name: ")
        try:
            contact = phone_book.get_contact(name)
            print("Enter new information for the contact:")
            contact.name = input(f"Name ({contact.name}): ") or contact.name
            contact.phone_number = input(f"Phone ({contact.phone_number}): ") or contact.phone_number
            contact.email = input(f"Email ({contact.email}): ") or contact.email
            contact.address = input(f"Address ({contact.address}): ") or contact.address
            print("Contact updated successfully!")
        except ValueError as e:
            print(str(e))
    elif choice == "4":
        # Get and print a contact by name
        name = input("Enter the contact's name: ")
        try:
            contact = phone_book.get_contact(name)
            print(contact.formatted_contact())
        except ValueError as e:
            print(str(e))
    elif choice == "5":
        print("Contacts:")
        phone_book.print_formatted_phonebook()
    elif choice == "6":
        filename = input("Enter filename to save to: ")
        phone_book.save_phonebook(filename)
    elif choice == "7":
        filename = input("Enter filename to load from: ")
        phone_book.load_phonebook(filename)
    elif choice == "8":
        # Exit the program
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")