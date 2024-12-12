from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from login_ui import Ui_LoginWindow
from main_ui import Ui_TodoListWindow


class LoginView(QWidget, Ui_LoginWindow):
    login_success = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ToDoView(QWidget, Ui_TodoListWindow):
    def __init__(self):
        super(ToDoView, self).__init__()
        self.setupUi(self)
