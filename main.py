import sys
from PyQt5.QtWidgets import QApplication

from controller import LoginController, ToDoController
from view import LoginView, ToDoView

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialize LoginView and Controller
    login_view = LoginView()
    login_controller = LoginController(login_view)

    # Initialize ToDoView and Controller
    todo_view = ToDoView()
    todo_controller = ToDoController(todo_view)

    # Connect login success signal to show ToDoView
    def show_todo_view():
        login_view.close()
        todo_view.show()


    login_view.login_success.connect(show_todo_view)

    login_view.show()
    sys.exit(app.exec_())
