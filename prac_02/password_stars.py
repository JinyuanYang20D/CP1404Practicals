def main():
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    print(len(password) * "*")


def get_password():
    password = input("Enter your password: ")
    return password


main()
