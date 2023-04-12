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


def main():
    # Display Options
    print('Select an Option.')
    print('')
    print('1. Select one object')
    print('2. Shuffle list of objects')
    print('') 
    # Get the user's choice
    choice = input("Enter a choice ( 1 or 2 ): ")
    print('')
    # Perform operation based upon user choice
    if choice == '1':
        print(get_random_school(filename))
    elif choice == '2':
        print(shuffle_and_print_items(filename))
    else:
        print('Invalid object')


if __name__ == '__main__':
    filename = sys.argv[1]
    main()
