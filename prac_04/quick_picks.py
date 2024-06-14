import random
CONSTANTS = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45

rows = int(input("How many quick picks? "))
for x in range(0, rows):
    random_list = []
    for y in range(0, CONSTANTS):
        result = int(random.randint(LOWEST_NUMBER, HIGHEST_NUMBER))
        while result in random_list:
            result = int(random.randint(LOWEST_NUMBER, HIGHEST_NUMBER))
        random_list.append(result)
    random_list.sort()
    for z in range(len(random_list)):
        random_list[z] = f"{str(random_list[z]):>2}"
    print(" ".join(random_list))

