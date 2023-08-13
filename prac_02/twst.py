"""This program checks password and return stars at the same length of password"""
def main():
    password = get_password()
    display_asterisks(password)
def display_asterisks(password):
    print(len(password) * "*")
def get_password():
    password = input("Enter your password: ")
    return password
main()
