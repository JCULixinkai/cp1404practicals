import random
# Line 1: Generate a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20)) # The smallest number is 5, and the largest number is 20.
# Example output: 12

# Line 2: Generate a random number between 3 and 10 with a step of 2
print(random.randrange(3, 10, 2)) # Example output: 5
# The smallest number is 3, and the largest number is 9

# Line 3: Generate a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5)) # Example output: 3.9825
# The smallest number is 2.5, and the largest number is 5.5.

# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
