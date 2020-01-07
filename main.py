import csv
import random


def load_all_items() -> list:
    """Real all items from the file into alist"""
    with open('items.txt') as file:
        items = file.read().splitlines()
    return items


def input_integer() -> int:
    """Obtain an integer from the user"""
    valid_integer = None

    while valid_integer is None:
        try:
            valid_integer = int(input('How many items do you require?'))

        except ValueError:
            print('Please enter an integer.')
            continue
    return valid_integer


def select_items(number: int) -> list:
    """Select random items from the list"""
    selected_items = random.choices(all_items, k=number_of_items)
    return selected_items


all_items = load_all_items()
number_of_items = input_integer()
selected_items = select_items(number_of_items)

print(selected_items)
