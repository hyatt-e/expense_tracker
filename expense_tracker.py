from datetime import datetime
from datetime import date
import json
import argparse
import sys


class Expense():
    '''Handles input of expense information to be stored'''

    @classmethod
    def request_expense_details(cls):
        try:
            amount = float(input("Expense Amount: "))
        except:
            "Please enter a number"
        desc = input("Expense Description: ")

        return amount, desc

    def __init__(self, amount=None, desc=None):
        self.amount = amount
        self.desc = desc
        self.date = str(date.today())

        if self.amount is None and self.desc is None:
            (self.amount, self.desc) = \
                Expense.request_expense_details()

    def print_expense(self):
        print("Expense Amount: ", self.amount)
        print("Expense Description: ", self.desc)
        print("Expense Date: ", self.date)


# Save input
# # CSV or json
def expense_to_json(amount, desc, date):
    data = {'amount': amount, "desc": desc, 'date': date}
    with open('./expenses/expenses.json', "w") as file:
        json.dump(data, file, indent=4)


# Retreive expenses
# # Display list of expenses
def json_to_expense():
    with open('./expenses/expenses.json') as file:
       return json.load(file)


def cli_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", type=float, required=True,
        help="Dollar amount of expense")
    parser.add_argument("-d", help="Description of expense")
    parser.add_argument("-p", type=bool,
        help="Print to console. Default: False", default=False)

    args = parser.parse_args()

    if args is not None:
        amount = args.a
        desc = args.d
        NewExpense = Expense(amount, desc)
    else:
        return None

    if args.p:
        NewExpense.print_expense()


if __name__ == '__main__':
    # run CLI if module is called directly.
    # NewCollection = CollectExpense()
    # NewCollection.NewExpense = NewCollection.cli_parse()
    # if NewCollection.NewExpense is None:
    #     NewCollection.NewExpense = CollectExpense.request_expense_details()

    NewCollection = Expense()
