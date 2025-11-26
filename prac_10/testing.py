import doctest
from prac_06.car import Car  # Ensure this path is correct


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    
    >>> repeat_string("hello", 3)
    'hello hello hello'
    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("hi", 2)
    'hi hi'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Formats a phrase as a sentence, starting with a capital and ending with a single full stop.
    
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('format this as a sentence')
    'Format this as a sentence.'
    """
    phrase = phrase.capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # assert test to see if Car sets the fuel correctly
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"

    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel to default correctly"


run_tests()

# Uncomment the following line and run the doctests
doctest.testmod()
