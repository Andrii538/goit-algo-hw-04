from com_parser import *

def main():
    """
    Консольний бот-помічник, який розпізнає команди, що вводяться з клавіатури, та відповідає згідно із введеною командою.
    Він вміє зберігати, змінювати і показувати збережені контакти і відповідні номери телефонів.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    commands = '''
    hello - для вітального повідомлення,
    help - для виклику цього повідомлення,
    close or exit - для припинення виконня бота,
    add - для додавання нового контакта, передається з імʼям і номером розділеними пробілом,
    phone - для показу номера телефона для конкретного контакта, передається з імʼям розділеними пробілом,
    change - для зміни записаного номера для конкретного контакта, передається з імʼям і номером розділеними пробілом,
    all - для показу всіх збережених контактів з їх номерами.
    '''
    print(commands)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'help':
            print(commands)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
