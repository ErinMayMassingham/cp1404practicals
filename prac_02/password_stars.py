
def main():
    min_length = 8
    password = get_password(min_length)
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password(min_length):
    password = input("Password: ")
    while len(password) < min_length:
        print(f"Error: Password must be at least {min_length} characters.")
        password = input("Password: ")
    return password


main()