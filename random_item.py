import random


def get_random_school():
    with open('schools.txt', 'r') as file:
        lines = file.readlines()

    random_line = random.choice(lines)

    return random_line


random_school = get_random_school()
print(random_school)