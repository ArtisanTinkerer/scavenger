import csv
import random
from fpdf import FPDF


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


def select_items(number_of_items: int, all_items: list) -> list:
    """Select random items from the list"""
    selected_items = random.choices(all_items, k=number_of_items)
    return selected_items


def make_pdf(selected_items):
    """Create a PDF file"""
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    pdf.cell(40, 10, 'Scavenger Hunt',ln=1)

    for item in selected_items:
        pdf.cell(40, 10, item, ln=0)
        pdf.cell(40, 10, '', ln=0)
        pdf.cell(20, 10, '', ln=1, border=1)

    pdf.output('hunt.pdf', 'F')


def main():
    all_items = load_all_items()
    number_of_items = input_integer()
    selected_items = select_items(number_of_items, all_items)
    print(selected_items)
    make_pdf(selected_items)

main()




