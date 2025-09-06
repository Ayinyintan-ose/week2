class Phonebook:
    def __init__(self):
        # Create a dictionary to store both name and number
        self.contacts = {}

    def add_number(self):
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        if name in self.contacts:
            print(f"The name {name} already exists in your phone book")
        self.contacts[name] = number
        print(f"This is your new contact: {name} -> {number}")

    def remove_number(self):
        print("These are the available contacts you have stored")
        for index, (name, number) in enumerate(self.contacts.items()):
            print(f"{index + 1}. {name} -> {number}")
        name = input("Enter the contact name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"The contact {name} has been removed from your contact.")
        else:
            print(f"The name {name} is not in your contact.")

    def view_contact(self):
        if not self.contacts:
            print("There is no contact in your phonebook.")
        else:
            for index, (name, number) in enumerate(self.contacts.items()):
                print(f"{index + 1}. {name} -> {number}")

my_phonebook = Phonebook()

while True:
    print("These are the available options")
    options = ["add contact", "view contact","remove contact", "Exit"]
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    user_choice = input("What would you like to do? Enter from (1-4): ")

    if user_choice == "1":
        my_phonebook.add_number()
    elif user_choice == "2":
        my_phonebook.view_contact()
    elif user_choice == "3":
        my_phonebook.remove_number()
    elif user_choice == "4":
        print("Bye!")
        break
    else:
        print("That is not an available option.")