import random
import sys


def shuffle_and_print_items(filename):
    with open(filename, 'r') as file:
        items = file.readlines()

    items = [item.strip() for item in items]

    random.shuffle(items)

    for item in items:
        print(item)


if __name__ == '__main__':
    filename = sys.argv[1]

shuffle_and_print_items(filename)
