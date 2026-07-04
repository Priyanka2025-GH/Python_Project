# 2.Contact Book Using Python

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts[name] = phone 
    print("Contact Added Successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No Contacts Found!")
    else:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(name, "-", phone)

def search_contact():
    name = input("Enter Name to Search: ").strip()

    if name in contacts:
        print("Found:", name, "-", contacts[name])
    else:
        print("Contact Not Found!")

def update_contact():
    name = input("Enter Name to Update: ").strip()

    if name in contacts:
        new_phone = input("Enter New Phone Number: ")
        contacts[name] = new_phone
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")

def delete_contact():
    name = input("Enter Name to Delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

while True:
     
    print("\n--- Contact Book Menu ---")
    print("\nTotal Contacts")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice! Please Try Again.")

