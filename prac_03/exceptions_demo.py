"""Answer the following questions:
1. When will a ValueError occur?
  A ValueError will occur when the user inputs a numerator or denominator that is not a valid integer. 
  For example, entering a letter or any non-numeric character.
2. When will a ZeroDivisionError occur?
   Before attempting a division operation, check if the denominator is zero. 
   If it is zero, it prompts the user that the denominator cannot be zero and avoids division operations, thereby avoiding ZeroDivisionError.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?"""""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
