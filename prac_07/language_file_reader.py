"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage



def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('/mnt/data/languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Year,PointerArithmetic
        in_file.readline()  # Skip the header line
        # All other lines are language data
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            languages.append(language)

    # Display all languages
    for language in languages:
        print(language)

main()

def using_csv():
    """Language file reader version using the csv module."""
    with open('/mnt/data/languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Skip the header line
        reader = csv.reader(in_file)
        for row in reader:
            print(row)

def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('/mnt/data/languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)
        for row in reader:
            row[2] = row[2] == "Yes"
            row[4] = row[4] == "Yes"
            language = Language._make(row)
            print(repr(language))

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open("/mnt/data/languages.csv", "r") as in_file:
        in_file.readline()  # Skip the header line
        reader = csv.reader(in_file)
        for row in reader:
            row[2] = row[2] == "Yes"
            row[4] = row[4] == "Yes"
            language = Language._make(row)
            print(f"{language.name} was released in {language.year}")
            print(repr(language))

