"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = Converting_Celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = converting_fahrenheit(celsius, fahrenheit)
            print(f"Result: {celsius:.2f} F")
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")


def converting_fahrenheit(celsius, fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def Converting_Celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()