"""
languages.py
"""

from programming_language import ProgrammingLanguage

def main():
    languages = [
        ProgrammingLanguage("Python", "Dynamic", True, 1991),
        ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
        ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ]

    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    main()
