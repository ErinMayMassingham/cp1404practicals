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
        # More options added later
        else:
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

    filtered_projects = [project for project in projects if project.get_start_date() >= filter_date]
    filtered_projects.sort(key=Project.get_start_date)

    if not filtered_projects:
        print("No projects start after that date.")
    else:
        for project in filtered_projects:
            print(f"  {project}")

main()
