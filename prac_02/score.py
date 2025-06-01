def main():
    MENU = """(G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
        else:
            if choice == "P":
                print(get_score_result(score))
            elif choice == "S":
                print("*" * len(score))
            else:
                print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Farewell")

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"