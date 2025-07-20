"""CP1404 Prac 7 Project Management"""

from project import Project

FILENAME = "projects.txt"

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

def main():
    """Main program for managing projects"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_projects(projects)

main()
