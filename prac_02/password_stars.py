
def main():
    """Get password and display asterisks"""
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    """Display the given number of asterisks."""
    print(len(password) * "*")


def get_password():
    """Get password"""
    password = input("Enter your password: ")
    return password


main()
