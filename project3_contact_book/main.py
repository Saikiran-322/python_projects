contacts = []

def add_contact():
    name  = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter Email: ")

    contact={
        "name":name,
        "phone":phone,
        "email":email
    }

    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    print("\n--- Contact List ---")

    for index,c in enumerate(contacts,start=1):
        print(f"{index}.{c['name']} - {c['phone']} - {c['email']}")



def search_contact():
    name = input("Enter name to search: ").lower()
    found = [c for c in contacts if c['name'].lower() == name]

    if not found:
        print("Contact not found.")

    else:
        print("\n--- Search result ---")
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']}")


def delete_contact():
    name  = input("Enter name of contact to delete: ").lower()
    
    global contacts
    new_list = [c for c in contacts if c['name'].lower() != name]

    if len(new_list) == len(contacts):
        print("Contact not found")

    else:
        contacts = new_list
        print("Contact deleted successfully!")


def menu():
    print("\n📒 CONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
    

