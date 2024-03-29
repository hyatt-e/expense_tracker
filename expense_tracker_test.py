import unittest
from unittest.mock import patch
import os
import json
import expense_tracker
import expense_db_setup
# import id_nums


class TestExpenseCollectionWithArgs(unittest.TestCase):
    '''Check that instance of Expense is created when amount and
    desc are given'''

    @classmethod
    def setUpClass(cls):
        cls.NewExpense = expense_tracker.Expense(40, 'gas')

    def test_create_expense(self):
        self.assertIsInstance(TestExpenseCollectionWithArgs.NewExpense, expense_tracker.Expense)

    def test_print_expense(self):
        TestExpenseCollectionNoArgs.NewExpense.print_expense()

    def test_new_expense_amount_is_float(self):
        self.assertTrue(type(TestExpenseCollectionWithArgs.NewExpense.amount) is float or int)

    # def test_save_expense(self):
        # can the file be opened and read?

    @classmethod
    def tearDownClass(cls):
        pass


class TestExpenseCollectionNoArgs(unittest.TestCase):
    '''Check that instance of Expense is created when amount and
    desc are NOT given, and need to be entered through stdin'''

    @classmethod
    def setUpClass(cls):
        user_input = [25, 'ball']
        with patch('builtins.input', side_effect=user_input):
            cls.NewExpense = expense_tracker.Expense()

    def test_create_expense(self):
        self.assertIsInstance(TestExpenseCollectionNoArgs.NewExpense, expense_tracker.Expense)

    def test_print_expense(self):
        TestExpenseCollectionNoArgs.NewExpense.print_expense()

    def test_new_expense_amount_is_float(self):
        self.assertTrue(type(TestExpenseCollectionNoArgs.NewExpense.amount) is float)

    @classmethod
    def tearDownClass(cls):
        pass


class TestSaveToJson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_input = [18, 'book']
        with patch('builtins.input', side_effect=cls.user_input):
            cls.NewExpense = expense_tracker.Expense()

    def test_expense_to_json(self):
        expense_tracker.expense_to_json(TestSaveToJson.NewExpense.amount, TestSaveToJson.NewExpense.desc, TestSaveToJson.NewExpense.date)
        data = expense_tracker.json_to_expense()
        self.assertEqual(data['amount'], TestSaveToJson.user_input[0])
        self.assertEqual(data['desc'], TestSaveToJson.user_input[1])

    @classmethod
    def tearDownClass(cls):
        pass


class TestDB(unittest.TestCase):

    def setUp(self):
        self.db_doesnt_exist = "not_a_real.db"

    def test_create_db(self):
        self.assertEqual(expense_db_setup.create_db("loaf_0.db"), "DB already exists")
        self.assertEqual(expense_db_setup.create_db(self.db_doesnt_exist), "DB created at not_a_real.db")

    def tearDown(self):
        try:
            os.remove(self.db_doesnt_exist)
        except FileNotFoundError:
            # TODO: change to logging
            print("The DB file {} was not created".format(self.db_doesnt_exist))


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        pass

    def test_id_6_digits(self):
        uid = id_nums.gen_uid()
        self.assertTrue(len(str(uid)), 6)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
