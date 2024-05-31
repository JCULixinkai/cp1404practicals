def main():
    score = get_valid_score()
    choice = ""
    while choice != 'Q':
        print_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"Result: {get_result(score)}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")


def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))

main()
