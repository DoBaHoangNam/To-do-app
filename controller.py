from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QInputDialog


from model import Task, TaskManager


class LoginController:
    def __init__(self, view):
        self.view = view
        self.view.loginButton.clicked.connect(self.login)
        self.view.cancelButton.clicked.connect(self.cancel)

    def login(self):
        username = self.view.usernameLineEdit.text()
        password = self.view.passwordLineEdit.text()

        if username == "" and password == "":
            QMessageBox.information(self.view, "Login Successful", "Welcome, admin!")
            self.view.login_success.emit()
        else:
            QMessageBox.warning(self.view, "Login Failed", "Invalid username or password!")

    def cancel(self):
        self.view.close()


class ToDoController:
    def __init__(self, view):
        self.view = view
        self.task_manager = TaskManager()

        self.view.addTaskButton.clicked.connect(self.add_task)
        self.view.deleteTaskButton.clicked.connect(self.delete_task)
        self.view.clearAllButton.clicked.connect(self.clear_all_tasks)
        self.view.taskListWidget.itemDoubleClicked.connect(self.mark_task_as_completed)

        self.load_tasks()

    def add_task(self):
        """add a new task"""
        title, ok = QInputDialog.getText(self.view, "New Task", "Enter task title:")
        if ok and title:
            description, ok = QInputDialog.getText(self.view, "New Task", "Enter task description:")
            if ok:
                due_date = None
                due_date_str, ok = QInputDialog.getText(self.view, "New Task", "Enter due date (YYYY-MM-DD, optional):")
                if ok and due_date_str:
                    try:
                        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                    except ValueError:
                        QMessageBox.warning(self.view, "Invalid Date",
                                            "Please enter a valid date in YYYY-MM-DD format.")
                        return

                # Create a new task object
                task = Task(title=title, description=description, due_date=due_date)

                # Add task to the manager and update the view
                self.task_manager.add_task(task)
                self.view.taskListWidget.addItem(self.task_manager.get_display_text(task))

    def delete_task(self):
        """remove selected tasks"""
        selected_items = self.view.taskListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self.view, "No Selection", "Please select a task to delete.")
            return

        for item in selected_items:
            task_title = item.text().split(" (")[0]
            task = self.task_manager.find_task_by_title(task_title)
            if task:
                self.task_manager.remove_task(task.id)
                self.view.taskListWidget.takeItem(self.view.taskListWidget.row(item))

    def clear_all_tasks(self):
        """delete all tasks"""
        reply = QMessageBox.question(
            self.view, "Clear All Tasks",
            "Are you sure you want to delete all tasks?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.task_manager.tasks = []
            self.task_manager.save_tasks()
            self.view.taskListWidget.clear()

    def mark_task_as_completed(self, item):
        """mark task as completed"""
        task_title = item.text().split(" (")[0]
        task = self.task_manager.find_task_by_title(task_title)
        if task:
            self.task_manager.mark_task_as_completed(task.id)
            item.setText(self.task_manager.get_display_text(task))

    def load_tasks(self):
        """load and display all tasks"""
        self.view.taskListWidget.clear()
        for task in self.task_manager.get_all_tasks():
            self.view.taskListWidget.addItem(self.task_manager.get_display_text(task))
