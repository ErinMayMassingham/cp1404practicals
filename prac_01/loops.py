"""TODO:
loop that displays all the odd numbers between
1 and 20 with a space between each one
a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
d. print n lines of increasing stars. Using the same number as above,
print lines of increasing stars, starting at 1 with no blank line.
"""
#example shown
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(1, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
stars = int(input("Number of stars: "))
for i in range(1, stars + 1, 1):
    print("*", end=' ')
print()

#d
n = 1
while n <= stars:
    for n in range(1, n + 1, 1):
        print("*", end=' ')
        n = n + 1
    print()