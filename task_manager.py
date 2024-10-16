import json
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_json(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

tasks = []


def add_task(title):
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)
    message = "Task " + title + " added with ID " + str(task_id) + "."
    print(message)


def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = 'X' if task.completed else ' '
            message="["+status+"]  " + " : " +  str(task.id) + " : " +task.title
            print(message)


def delete_task(task_id):
    global tasks
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            message = "Task with ID " + str(task_id) + " deleted."
            print(message)
            return
    else:
        print("Task with ID " + str(task_id) + " not found.")


def task_status(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            message = "Task with ID " + str(task_id) + " marked as complete"
            print(message)
            return
    print("Task with ID not found.")




def save_tasks(filename="tasks.json"):
    task_data = []
    for task in tasks:
        task_data.append(task.to_json())
    file = open(filename, "w")
    try:
        json.dump(task_data, file)
        print("Tasks saved to file.")
    finally:
        file.close()


def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            file_content = file.read().strip()
            if not file_content:
                print("No tasks found in file. Starting with an empty task list.")
                return []

            loaded_tasks = json.loads(file_content)
            for task_data in loaded_tasks:
                task = Task(task_data['id'], task_data['title'], task_data['completed'])
                tasks.append(task)
            return tasks

    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty task list.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. The file might be corrupted. Starting with an empty task list.")
        return []


def manager_command():
    print("\nTask Manager CLI      \n")
    print("1. Add Task",end=" ")
    print("2. View Tasks",end=" ")
    print("3. Delete Task",end=" ")
    print("4. Mark Task as Complete",end=" ")
    print("5. Save Tasks",end=" ")
    print("6. Exit",end=" ")
    print("\n")


def main():
    global tasks
    tasks = load_tasks()

    while True:
        manager_command()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark complete: "))
            task_status(task_id)
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            print("Command Line Application Exited")
            break
        else:
            print("Invalid choice, please try again.")


main()
