import json
from datetime import datetime

class Task:
    def __init__(self, description, due_date, priority="Medium"):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.description}, Due: {self.due_date}, Priority: {self.priority}, Status: {status}"

# Helper function to convert date
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")
