from storage import load_data, save_data
from tasks import add_task, view_tasks, complete_task
from study import add_study_hours
from progress import show_progress
from utils import show_menu

data = load_data()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(data)
        save_data(data)

    elif choice == "2":
        view_tasks(data)

    elif choice == "3":
        complete_task(data)
        save_data(data)

    elif choice == "4":
        add_study_hours(data)
        save_data(data)

    elif choice == "5":
        show_progress(data)

    elif choice == "6":
        save_data(data)
        print("Thank you for using StudyMate!")
        break

    else:
        print("Invalid choice.")