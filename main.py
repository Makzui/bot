def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
    return wrapper

class ContactBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def hello(self):
        return "How can I help you?"

    @input_error
    def add(self, data):
        try:
            name, phone = data.split()
            if name not in self.contacts:
                self.contacts[name] = phone
                return f"Contact {name} added with phone {phone}"
            else:
                return f"Contact with name {name} already exists. Use 'change' command to update the phone number."
        except ValueError:
            raise ValueError("Invalid data format. Please provide both name and phone.")

    @input_error
    def change(self, data):
        try:
            name, phone = data.split()
            if name in self.contacts:
                self.contacts[name] = phone
                return f"Phone number updated for {name}"
            else:
                raise IndexError("Contact not found")
        except ValueError:
            raise ValueError("Invalid data format. Please provide both name and phone.")

    @input_error
    def phone(self, name):
        return self.contacts.get(name, "Contact not found")

    @input_error
    def show_all(self):
        if not self.contacts:
            return "No contacts available"
        else:
            result = "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())
            return result

    def main(self):
        while True:
            user_input = input("Enter command: ").lower()
            if user_input in ["good bye", "close", "exit", "."]:
                print("Good bye!")
                break
            elif user_input == "hello":
                print(self.hello())
            elif user_input.startswith("add"):
                data = user_input[4:]
                print(self.add(data))
            elif user_input.startswith("change"):
                data = user_input[7:]
                print(self.change(data))
            elif user_input.startswith("phone"):
                name = user_input[6:]
                print(self.phone(name))
            elif user_input == "show all":
                print(self.show_all())
            else:
                print("Invalid command. Try again.")

if __name__ == "__main__":
    bot = ContactBot()
    bot.main()
