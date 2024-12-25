
from src.classes import Task, TaskManager

def main():
    task1 = Task("Task 1", "First Task")
    task2 = Task("Task 2", "Second Task", is_completed=True)

    manager = TaskManager()
    manager.add_task(task1)
    manager.add_task(task2)

    print("All Tasks:")
    for task in manager.get_all_tasks():
        print(f"{task.title}: {'Completed' if task.is_completed else 'Not completed'}")

    manager.remove_task("Task 1")
    print("After Removing 'Task 1':")
    for task in manager.get_all_tasks():
        print(task.title)

if __name__ == "__main__":
    main()

