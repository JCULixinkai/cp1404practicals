
def main():
    emails = get_emails()
    print_emails(emails)

def get_emails():
    emails = {}
    email = input("Email: ").strip()
    while email:
        name = extract_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if correct_name not in ('', 'y', 'yes'):
            name = input("Name: ").strip()
        emails[email] = name
        email = input("Email: ").strip()
    return emails

def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = " ".join(part.capitalize() for part in name_parts)
    return name

def print_emails(emails):
    for email, name in emails.items():
        print(f"{name} ({email})")

    main()


