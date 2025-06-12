import random

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    numbers = []
    for j in range(6):
        rand_number = random.randint(1, 45)
        numbers.append(rand_number)
    numbers.sort()
    print(" ".join(sorted(f"{numbers:2}" for numbers in numbers)))
