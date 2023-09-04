"""
Replace the contents of this module docstring with your own details
Name:
Date started:
GitHub URL:
"""

places = open("places.csv", "r")
print(places.read())
places.close()

temp = open("temp.csv", "r")
print(temp.read())
temp.close()

def main():
    print("Travel Tracker 1.0 - by <Jinyuan Yang>")
    print("3 places loaded from places.csv")
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "L":
        print("List")
    elif choice == "A":
        print("Add")
    elif choice == "M":
        print("Mark")
    else:
        print("Invalid menu choice")
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")
    choice = input(">>> ").upper()
print("Have a nice day :)")
print("3 places saved to places.csv")






if __name__ == '__main__':
    main()
