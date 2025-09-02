from abc import ABC, abstractmethod

class UserView(ABC):
    @abstractmethod
    def show_contacts(self, contacts: list) -> None:
        pass

    @abstractmethod
    def show_help(self, commands: dict) -> None:
        pass

    @abstractmethod
    def show_message(self, message: str) -> None:
        pass


class ConsoleView(UserView):
    def show_contacts(self, contacts: list) -> None:
        print("Контакти:")
        if not contacts:
            print("Список порожній")
        for contact in contacts:
            print(f"- {contact}")

    def show_help(self, commands: dict) -> None:
        print("Доступні команди:")
        for cmd, desc in commands.items():
            print(f"{cmd:10} - {desc}")

    def show_message(self, message: str) -> None:
        print(message)
