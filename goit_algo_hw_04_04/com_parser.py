
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return f'{name} is already in your contacts list.\nIf you want to change the phone number for {name}, use the command "change".'

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found."

def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return contacts[name]
    else:
        return "Name not found."
    
def show_all(contacts):
    result = '\n'.join(f'{item:^10} {contacts[item]}' for item in contacts)
    return result

