def add_task(data):
    task = input("Enter task: ")
    if task:
        data["tasks"].append({"name": task, "done": False})
        print("Task added.")


def view_tasks(data):
    if not data["tasks"]:
        print("No tasks yet.")
        return

    for i, task in enumerate(data["tasks"], 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['name']} - {status}")


def complete_task(data):
    view_tasks(data)

    if not data["tasks"]:
        return

    try:
        number = int(input("Enter task number: "))
        data["tasks"][number - 1]["done"] = True
        print("Task completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")