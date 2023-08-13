MENU = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit"""
def main():
    """Get a score and display its result."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Valid score: "))
            result = get_result(score)
            print(result)
        elif choice == "P":
            print(result)
        elif choice == "S":
            display_asterisks(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye.")

def get_result(score):
    """Return the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def display_asterisks(score):
    """Display the given number of asterisks."""
    print(len(score) * "*")

main()
