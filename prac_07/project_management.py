"""CP1404 Prac 7 Project Management"""

import datetime
from projects import Project

FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Main menu for managing projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        else:
            save_option = input(f"Would you like to save to {FILENAME}? ").lower()
            if save_option in ["yes", "y"]:
                save_projects(FILENAME, projects)
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").lower()

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file into a list of Projects"""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split("\t")
            name, date, priority, cost, complete = parts
            projects.append(Project(name, date, priority, cost, complete))
    return projects

def display_projects(projects):
    """Display incomplete and completed projects separately"""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete, key=lambda x: x.priority):
        print(f"  {p}")

    print("Completed projects:")
    for p in sorted(complete, key=lambda x: x.priority):
        print(f"  {p}")

def filter_projects_by_date(projects):
    """Display projects starting after user-specified date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    def get_project_start_date(project):
        return project.get_start_date()
    filtered_projects = [project for project in projects if project.get_start_date() >= filter_date]
    filtered_projects.sort(key=get_project_start_date)

    if not filtered_projects:
        print("No projects start after that date.")
    else:
        for project in filtered_projects:
            print(f"  {project}")


def add_project(projects):
    """User Input for new project details and add to list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)


def update_project(projects):
    """Update completion or priority of a selected project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)

        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_completion:
            project.completion_percentage = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)

    except (ValueError, IndexError):
        print("Invalid selection.")

def save_projects(filename, projects):
    """Save projects to file"""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")

main()
