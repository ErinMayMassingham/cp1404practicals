"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_details(data)


def print_details(data):
    for details in data:
        print(f"{details[0]} is taught by {details[1]} and has {details[2]} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    details = []
    input_file = open(FILENAME)
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        details.append(parts)
    input_file.close()
    return details


main()