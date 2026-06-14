
import json


def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)
    print("Contacts saved!")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
        print("Contacts loaded!")
    except FileNotFoundError:
        contacts = {}

contacts = {}

def add_contact():
    while True:                      # loop starts here
        name = input("Enter contact name: ")
        try:                         # ← inside while ✅
            phone_number = int(input("Enter phone number: "))
            contacts[name] = phone_number  # ← contacts not contact ✅
            print(f"{name} added successfully!")
            save_contacts()
            break                    # ← inside while ✅
        except ValueError:
            print("Please enter integers only. Try again!")
print(contacts)

#function to view contacts
def view_contact():
    if contacts:
     for name, phone in contacts.items():
      print(f"{name}: {phone}")
    else:
      print("contact not found")

def search_contact():
 name = input("Enter name to search: ")
 if name in contacts:
      print(f"{name}: {contacts[name]}")
 else:
      print(f"{name} not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully")
        save_contacts()
    else:
        print(f"{name} not found")


def menu():
    while True: 
        option_selected = int(input("Select: 1 for add contact, 2 for view contact, 3 for search contact ,4 for delete contact and 5 to end process"))
        try:
            if option_selected == 1:
             add_contact()
            elif option_selected == 2:
                view_contact()
            elif option_selected == 3:
                search_contact()
            elif option_selected == 4:
                delete_contact()
            elif option_selected == 5:
                print("Good bye")
                break

            else:
                print("Invalid choice please try again")

        except ValueError:
            print("Please enter intergers only.Try again")

load_contacts()   # ← load saved contacts first
menu()
