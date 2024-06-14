FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    subjects = []
    with open(FILENAME) as file:
        for line in file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects

def display_subject_details(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()
