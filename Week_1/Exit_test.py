import json

contacts= []

class Contacts:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print("Name: ", self.name)
        print("Phone: ", self.phone)
        print("Email: ", self.email)

def save_contacts():
        data = []
        for contact in contacts:
            data.append({
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email
            })

        with open("contacts.json", "w")as file:
            json.dump(data, file, indent=4)

def load_contact():
        try:
            with open("contacts.json", "r")as file:
                data = json.load(file)

                for item in data:
                    contact = Contacts(
                            item["name"],
                            item["phone"],
                            item["email"]
                    )
                    contacts.append(contact)
        except FileNotFoundError:
            print("File not found.")
load_contact()
while True:
    print("\n====Contact Book====")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = Contacts(name, phone, email)

        contacts.append(contact)
        save_contacts()

        print("Contact added successfully")

    elif choice == "2":
        for contact in contacts:
            contact.display()

    elif choice == "3":
        found = False

        search_name = input("Enter name: ")

        for contact in contacts:
            if contact.name.lower() == search_name.lower():

                contact.display()
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        found = False

        search_name = input("Enter name: ")

        for contact in contacts:
            if contact.name.lower() == search_name.lower():

                new_phone = input("Enter phone: ")
                contact.phone = new_phone
                save_contacts()
                found = True

                print("Contact updated successfully.")
                break
            
        if not found: 
            print("Contact not found.")

    elif choice == "5":
        found = False 

        search_name = input("Enter name: ")

        for contact in contacts:
            if contact.name.lower() == search_name.lower():

                contacts.remove(contact)
                save_contacts()
                found = True

                print("Contact deleted successfully")
                break
        if not found: 
            print("Contact not found.")
    elif choice == "6":
        print("Thank you")
        break

            
            
