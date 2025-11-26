import datetime
from project import Project


def load_projects(filename="projects.py"):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                projects.append(Project.load_from_string(line.strip()))
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            file.write(project.to_string() + '\n')
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    incomplete.sort(key=lambda p: p.priority)
    complete.sort(key=lambda p: p.priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects, date_string):
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered = [project for project in projects if project.start_date > date]
    filtered.sort(key=lambda p: p.start_date)

    print(f"Projects starting after {date_string}:")
    for project in filtered:
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    valid_date = False
    while not valid_date:
        try:
            start_date = input("Start date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            valid_date = True
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")

    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    percent_complete = input("Percent complete: ")

    projects.append(
        Project(name, start_date.strftime("%d/%m/%Y"), int(priority), float(cost_estimate), int(percent_complete)))
    print("Project added successfully.")


def update_project(projects):
    display_projects(projects)
    project_index = get_valid_index("Project choice: ", len(projects))
    selected_project = projects[project_index]

    percent_complete = input("New Percentage (leave blank to retain current): ")
    priority = input("New Priority (leave blank to retain current): ")

    if percent_complete:
        selected_project.update(percent_complete=int(percent_complete))
    if priority:
        selected_project.update(priority=int(priority))

    print(f"{selected_project.name} has been updated.")


def get_valid_index(prompt, limit):
    valid_index = False
    while not valid_index:
        try:
            index = int(input(prompt))
            if 0 <= index < limit:
                valid_index = True
            else:
                print("Invalid project number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return index


def main():
    projects = load_projects()
    choice = None

    menu = (
        "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
        "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    )

    while choice != 'q':
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to projects.txt? (yes/no) ").lower()
            if save_choice in ['yes', 'y']:
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice, please try again.")


main()
