"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_celcius_to_farenheit():
    global fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_farenheit_to_celcius():
    global celcuis
    farenheit = float(input("Fahrenheit: "))
    celcuis = 5 / 9 * (farenheit - 32)


while choice != "Q":
    if choice == "C":
        convert_celcius_to_farenheit()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        convert_farenheit_to_celcius()
        print(f"Result: {celcuis:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")