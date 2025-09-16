from views import UserView

class BotApp:
    def __init__(self, view: UserView):
        self.contacts = []
        self.commands = {
            "add": "Додати новий контакт",
            "list": "Показати всі контакти",
            "help": "Показати список команд",
            "exit": "Вихід з програми"
        }
        self.view = view

    def run(self):
        self.view.show_message("Ласкаво просимо до Персонального помічника!")
        while True:
            cmd = input("Введіть команду: ")
            if cmd == "add":
                name = input("Введіть ім'я: ")
                self.contacts.append(name)
                self.view.show_message(f"Контакт {name} додано!")
            elif cmd == "list":
                self.view.show_contacts(self.contacts)
            elif cmd == "help":
                self.view.show_help(self.commands)
            elif cmd == "exit":
                self.view.show_message("До побачення!")
                break
            else:
                self.view.show_message("Невідома команда. Введіть 'help'.")
