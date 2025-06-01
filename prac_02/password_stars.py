min_length = 8

password = input("Password: ")
while len(password) < min_length:
    print(f"Error: Password must be at least {min_length} characters.")
    password = input("Password: ")

print("*" * len(password))