from interfaces import ITask, ITaskManager
from typing import List

class Task(ITask):
    def __init__(self, title: str, description: str, is_completed: bool = False):
        self.title = title
        self.description = description
        self.is_completed = is_completed

class TaskManager(ITaskManager):
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, title: str) -> None:
        self.tasks = [task for task in self.tasks if task.title != title]

    def get_all_tasks(self) -> List[Task]:
        return self.tasks
