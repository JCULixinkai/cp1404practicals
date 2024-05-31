def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def main():
    name = input("Enter name: ")
    choice = ''

    while choice != 'Q':
        display_menu()
        choice = input(">>> ").upper()

        if choice == 'H':
            print(f"Hello {name}")
        elif choice == 'G':
            print(f"Goodbye {name}")
        elif choice != 'Q':
            print("Invalid choice")

    print("Finished.")