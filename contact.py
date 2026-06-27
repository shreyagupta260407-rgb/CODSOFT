contacts = {}

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter name: ").strip()
    if name in contacts:
        print("This name already exists!")
        return
        
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    # Save inside our dictionary
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Success! {name} added.")

def view_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("Your list is empty.")
        return
        
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']}")

def search_contact():
    print("\n--- Search ---")
    query = input("Enter name to search: ").strip()
    if query in contacts:
        print(f"\nFound Details for {query}:")
        print(f"Phone: {contacts[query]['phone']}")
        print(f"Email: {contacts[query]['email']}")
        print(f"Address: {contacts[query]['address']}")
    else:
        print("Contact not found.")

def update_contact():
    print("\n--- Update ---")
    name = input("Enter the name to update: ").strip()
    if name not in contacts:
        print("Name not found.")
        return
        
    print("Press Enter to keep current values.")
    new_phone = input(f"New Phone ({contacts[name]['phone']}): ").strip()
    new_email = input(f"New Email ({contacts[name]['email']}): ").strip()
    
    if new_phone:
        contacts[name]['phone'] = new_phone
    if new_email:
        contacts[name]['email'] = new_email
    print("Contact updated!")

def delete_contact():
    print("\n--- Delete ---")
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.")
    else:
        print("Name not found.")

# Main loop to run the program
while True:
    print("\n1. Add | 2. View | 3. Search | 4. Update | 5. Delete | 6. Exit")
    choice = input("Choose an option (1-6): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
