import mysql.connector


class Queries(object):
    """Database queries"""

    def __init__(self, cursor):
        self.cursor = cursor

    def department_budget(self, department_name):
        """Get department budget by name"""
        pass

    def department_expenses(self, department_name):
        """Get department expenses by name"""
        pass
