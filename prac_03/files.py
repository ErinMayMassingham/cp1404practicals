out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name_in_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_in_file}!")

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number += int(line)
        total += line
print(total)