from views import ConsoleView
from app import BotApp

if __name__ == "__main__":
    view = ConsoleView()
    app = BotApp(view)
    app.run()
