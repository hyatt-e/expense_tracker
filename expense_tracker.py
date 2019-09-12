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

    parser.add_argument("-a", nargs=2, help="Add Expense. Arguments: 1)Dollar amount of expense 2)Description of expense")
    parser.add_argument("-db", help="Create Database. Argument: DB file path and name")
    parser.add_argument("-p", type=bool,
        help="Print to console. Default: False", default=False)

    args = parser.parse_args()

    # check for arguments; print help if no arguments given
    if len(sys.argv) > 1:
        if args.db is not None:
            create_db_return = expense_db_setup.create_db(args.db)
            print(create_db_return)


        if args.a is not None:
            amount = args.a
            NewExpense = Expense(amount, desc)
            return NewExpense

    else:
        # print help as standard error
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.p:
        NewExpense.print_expense()


if __name__ == '__main__':
    # run CLI if module is called directly.
    # NewCollection = CollectExpense()
    # NewCollection.NewExpense = NewCollection.cli_parse()
    # if NewCollection.NewExpense is None:
    #     NewCollection.NewExpense = CollectExpense.request_expense_details()

    # NewCollection = Expense()

    NewExpense = cli_parse()
