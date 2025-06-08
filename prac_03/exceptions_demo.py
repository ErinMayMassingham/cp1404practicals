"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The denominator cannot be zero. Please try again.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

#When will a ValueError occur?
#A value error will occur when a non-number or non-integer is entered as either the numberator or denomincator

#When will a ZeroDivisionError occur?
#A zero division will occur when the integer zero (0) is entered in place of the denominator

#Could you change the code to avoid the possibility of a ZeroDivisionError?
#Yes, by giving users the option to be notified of the ZeroDivisonError and renter a new denominator it can be avoided.
