import json
from datetime import datetime
from uuid import uuid4


class Task:
    def __init__(self, title, description="", completed=False, due_date=None):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.due_date = due_date

    def to_dict(self):
        """Chuyển đổi công việc thành dictionary để lưu trữ."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "due_date": self.due_date.isoformat() if self.due_date else None,
        }

    @staticmethod
    def from_dict(data):
        """Khôi phục công việc từ dictionary."""
        task = Task(
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            due_date=datetime.fromisoformat(data["due_date"]) if data["due_date"] else None,
        )
        task.id = data["id"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        return task


class TaskManager:
    def __init__(self, storage_file="tasks.json"):
        self.tasks = []
        self.storage_file = storage_file
        self.load_tasks()

    def load_tasks(self):
        """load tasks from the storage file."""
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        """save the current tasks to the storage file."""
        with open(self.storage_file, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, task):
        """add a new task."""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id):
        """remove a task by its ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def find_task_by_title(self, title):
        """find a task by its title."""
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all_tasks(self):
        """get all tasks."""
        return self.tasks

    def mark_task_as_completed(self, task_id):
        """mark a task as completed by its ID."""
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            task.completed = True
            self.save_tasks()

    def get_display_text(self, task):
        """get the display-friendly text of the task."""
        due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"  # Chỉ lấy phần ngày
        return f"Title: {task.title} - Description: {task.description} - Due date {due_date_str} ({'Completed' if task.completed else 'Pending'})"

