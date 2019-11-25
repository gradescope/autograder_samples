import unittest
from gradescope_utils.autograder_utils.decorators import weight
import mysql.connector
from queries import Queries

class TestSimpleQueries(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(user='test', password='password', database='test_data')
        self.cursor = self.connection.cursor()
        self.queries = Queries(self.cursor)

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    @weight(1)
    def test_department_budget(self):
        """Get department budget by name"""
        val = self.queries.department_budget("Engineering")
        self.assertEqual(val, 1000000)

    @weight(1)
    def test_department_expenses(self):
        """Get department expenses by name"""
        val = self.queries.department_expenses("Engineering")
        self.assertEqual(val, 200000)
