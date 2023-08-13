"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
def main():
    """Get a score and display its result."""
    score = float(input("Enter score: "))
    result = get_result(score)
    random_score = random.randint(0, 100)
    print(result)
    print(get_result(random_score))

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

main()