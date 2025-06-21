COLOUR_HEX = {"absolute zero": "#0048ba",
                "acid green": "#b0bf1a",
                "aliceblue": "#f0f8ff",
                "alizarin crimson": "#e32636",
                "amaranth": "#e52b50",
                "amber": "#eedfcc",
                "amethyst": "#9966cc",
                "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb",
                "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0",
                "antiquewhite4": "#8b8378"}

colour_name = input("Enter a colour name: ").title()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").title()
