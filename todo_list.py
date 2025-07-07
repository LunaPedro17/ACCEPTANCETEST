class Task:
    def __init__(self, description, status="Pending", priority="Medium"):
        self.description = description
        self.status = status
        self.priority = priority

    def mark_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.description} - {self.status} (Priority: {self.priority})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority="Medium"):
        task = Task(description, priority=priority)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks.copy()

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return True
        return False

    def clear_all_tasks(self):
        self.tasks.clear()

    def find_task(self, description):
        for task in self.tasks:
            if task.description == description:
                return task
        return None