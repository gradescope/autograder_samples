import unittest
from gradescope_utils.autograder_utils.decorators import weight
import mysql.connector
from queries import Queries

class TestSimpleQueries(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(database='test_data')
        self.queries = Queries(self.connection)

    def tearDown(self):
        self.connection.close()

    @weight(1)
    def test_department_budget(self):
        """Get department budget by name"""
        val = self.queries.department_budget("Engineering")
        self.assertEqual(val, 1000000)

    @weight(1)
    def test_department_expenses(self):
        """Get department expenses by name"""
        val = self.queries.department_budget("Engineering")
        self.assertEqual(val, 200000)
