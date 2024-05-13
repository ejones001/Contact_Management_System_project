import re
import json
import os

# Global variable to store contacts
contacts = {}

# Function to display menu and get user choice
def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

    choice = input("Enter your choice (1-8): ")
    return choice.strip()

# Function to add a new contact
def add_contact():
    print("Adding a new contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
    }
    print("Contact added successfully!")

# Function to edit an existing contact
def edit_contact():
    print("Editing an existing contact:")
    name = input("Enter name of the contact to edit: ")
    if name not in contacts:
        print("Contact not found!")
        return

    print("Enter new details (leave blank to keep existing):")
    phone = input(f"Enter phone number ({contacts[name]['phone']}): ").strip() or contacts[name]["phone"]
    email = input(f"Enter email address ({contacts[name]['email']}): ").strip() or contacts[name]["email"]

    contacts[name] = {
        "phone": phone,
        "email": email,
    }
    print("Contact updated successfully!")

# Function to delete a contact
def delete_contact():
    print("Deleting a contact:")
    name = input("Enter name of the contact to delete: ")
    if name not in contacts:
        print("Contact not found!")
        return

    del contacts[name]
    print("Contact deleted successfully!")

# Function to search for a contact
def search_contact():
    print("Searching for a contact:")
    name = input("Enter name of the contact to search: ")
    if name not in contacts:
        print("Contact not found!")
        return

    print("Contact details:")
    print(json.dumps(contacts[name], indent=4))

# Function to display all contacts
def display_contacts():
    print("All contacts:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(json.dumps(details, indent=4))
        print()

# Function to export contacts to a text file
def export_contacts():
    filename = input("Enter filename to export contacts to (e.g., contacts.txt): ")
    with open(filename, "w") as file:
        json.dump(contacts, file)
    print("Contacts exported successfully!")

# Function to import contacts from a text file
def import_contacts():
    filename = input("Enter filename to import contacts from (e.g., contacts.txt): ")
    try:
        with open(filename, "r") as file:
            global contacts
            contacts = json.load(file)
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("File not found!")

# Main function
def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
