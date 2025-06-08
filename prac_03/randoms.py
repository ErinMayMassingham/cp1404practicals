import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#Number seen on line 1: 7
#Smallest number possible: 5
#Greatest number possible: 20

#Number seen on line 2: 3
#Smallest number possible: 3
#Greatest number possible: 9
#Produces any number starting at 3, stepping by 2 until 10 (3, 5, 7, 9)

#Number seen on line 3: 5.116876233847852
#Smallest number possible: 2.5
#Greatest number possible: 5.5
#Produces any float starting at 2.5, ending at 5.5