"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""
numberOfItems = int(input("Number of items: "))

totalPrice = 0
i = 1
while i <= numberOfItems:
    for i in range(1, numberOfItems + 1, 1):
        priceOfItem = float(input("Item price: $"))
        print(f"Price of item: {priceOfItem}")
        totalPrice += priceOfItem
        i = i + 1
    print()
if totalPrice > 100:
    discount = totalPrice / 10
    totalPrice = totalPrice - discount

print(f"Total price for {numberOfItems} items is ${totalPrice}")

