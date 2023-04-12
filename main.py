import random
import sys


def shuffle_and_print_items(filename):
    with open(filename, 'r') as file:
        items = file.readlines()

    items = [item.strip() for item in items]

    random.shuffle(items)

    for item in items:
        print(item)


def get_random_school(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    random_line = random.choice(lines)

    return random_line


if __name__ == '__main__':
    filename = sys.argv[1]
