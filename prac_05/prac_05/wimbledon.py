

def main():
    filename = "wimbledon.csv"
    data = load_data(filename)
    champions = count_champions(data)
    countries = extract_countries(data)
    display_champions(champions)
    display_countries(countries)

def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(",") for line in in_file.readlines()[1:]]

def count_champions(data):
    champions = {}
    for row in data:
        champion = row[2].strip()
        champions[champion] = champions.get(champion, 0) + 1
    return champions

def extract_countries(data):
    countries = {row[1].strip() for row in data}
    return sorted(countries)

def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")
    print()

def display_countries(countries):
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))
main()
