def add_study_hours(data):
    try:
        hours = float(input("Enter study hours: "))

        if hours > 0:
            data["study_hours"] += hours
            print("Study time recorded.")
        else:
            print("Enter a positive number.")

    except ValueError:
        print("Please enter a number.")


def show_study_hours(data):
    print(f"Total study hours: {data['study_hours']}")