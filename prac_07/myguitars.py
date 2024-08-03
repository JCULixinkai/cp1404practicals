import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)


def main():
    """Load, display, sort, add, and save guitars."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("All Guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    print("\nAdd new guitars (type 'done' to finish):")
    adding_guitars = True
    while adding_guitars:
        name = input("Name: ")
        if name.lower() == 'done':
            adding_guitars = False
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitars.append(Guitar(name, year, cost))

    save_guitars(filename, guitars)
    print("\nUpdated Guitar List:")
    display_guitars(guitars)

main()

