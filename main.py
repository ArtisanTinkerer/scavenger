import csv


def load_all_items() -> list:
    """Real all items from the file into alist"""
    with open('items.txt') as file:
        items = file.read().splitlines()
    return items


all_items = load_all_items()
print(all_items)
