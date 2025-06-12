numbers = [3, 1, 4, 1, 5, 9, 2]

#numbers[0]: index position 0 in list 'numbers', has value 3
#numbers[-1]: index position from last positions forward, has value 2
#numbers[3]: index position 3 (0, 1, 2, 3), value 1
#numbers[:-1]: all index position up to but not including position -1, value [3, 1, 4, 1, 5, 9]
#numbers[3:4]: all index positions including starting index (3) but excluding ending index (4), value 1
#5 in numbers: will check list numbers for 5 returning True if 5 is there or False if not, returns True
#7 in numbers: will check list numbers for 5 returning True if 7 is there or False if not, returns False
#"3" in numbers: will check list numbers for the string 3 (numbers = ("3", ...)), returns False
#numbers + [6, 5, 3]: updates numbers to include the new values, returns [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#run code to check answers above
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

#change first index to "ten"
numbers[0] = "Ten"
#change last index to 1
numbers[-1] = 1
#print all index excluding first 2
print(numbers[2:])
#check if 9 is an element of numbers
9 in numbers
