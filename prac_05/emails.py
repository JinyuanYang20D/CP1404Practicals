"""
emails
Estimate: 20 minutes
Actual:   35 minutes
"""

import re
def main():
    """Get user email and name and store them in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation == "" or confirmation == "y":
            email_to_name[email] = name
        else:
            name = input("Name: ").title()
            email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extracts the name from an email address."""
    name = re.findall(r"[a-zA-Z]+", email.split('@')[0])
    return ' '.join(name).title()

main()