# todo_app.py

def display_menu():
    """Display the main menu options."""
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Empty task cannot be added.")

def view_tasks(tasks):
    """View all current tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(tasks):
    """Delete a task by index."""
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        view_tasks(tasks)
        index = int(input("Enter the number of the task to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f'Task "{removed}" deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid integer.")

def main():
    """Main function to run the To-Do List app."""
    tasks = []
    while True:
        display_menu()
        try:
            choice = input("Select an option (1–4): ").strip()
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("\n-----------------------------------")

if __name__ == "__main__":
    main()
