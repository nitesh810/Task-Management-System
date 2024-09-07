class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority="Medium"):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number!")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Invalid task number!")

    def edit_task(self, index, description=None, due_date=None, priority=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority
        else:
            print("Invalid task number!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            data = [task.__dict__ for task in self.tasks]
            json.dump(data, file)

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
        except FileNotFoundError:
            print("No saved tasks found.")
