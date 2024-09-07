from task_manager import TaskManager


def main():
    task_manager = TaskManager()

    # Try loading tasks from file
    task_manager.load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Edit Task\n4. Delete Task\n5. Mark Task Completed\n6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low, Medium, High): ")
            task_manager.add_task(description, due_date, priority)

        elif choice == '2':
            task_manager.view_tasks()

        elif choice == '3':
            task_manager.view_tasks()
            index = int(input("Enter task number to edit: "))
            description = input("Enter new description (or press Enter to keep it unchanged): ")
            due_date = input("Enter new due date (or press Enter to keep it unchanged): ")
            priority = input("Enter new priority (or press Enter to keep it unchanged): ")
            task_manager.edit_task(index, description, due_date, priority)

        elif choice == '4':
            task_manager.view_tasks()
            index = int(input("Enter task number to delete: "))
            task_manager.delete_task(index)

        elif choice == '5':
            task_manager.view_tasks()
            index = int(input("Enter task number to mark as completed: "))
            task_manager.mark_task_completed(index)

        elif choice == '6':
            task_manager.save_tasks()
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
