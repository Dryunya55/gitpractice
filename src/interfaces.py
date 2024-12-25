from typing import List

class ITask:
    title: str
    description: str
    is_completed: bool

class ITaskManager:
    def add_task(self, task: ITask) -> None:
        pass

    def remove_task(self, title: str) -> None:
        pass

    def get_all_tasks(self) -> List[ITask]:
        pass
