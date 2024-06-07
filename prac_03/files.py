#Task 1: Write user’s name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

"""Task 2: Read the name from the file and print a greeting
python"""""
with open('name.txt', 'r') as file:
    name = file.read().strip()
print(f"Hi {name}!")

"""Task 3: Read first two numbers from numbers.txt and print their sum
Create a text file numbers.txt with the following content:"""""
17
42
400
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
result = num1 + num2
print(result)

"""Task 4: Read all numbers from numbers.txt and print their total sum"""
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(total)
