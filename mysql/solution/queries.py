import mysql.connector


class Queries(object):
    """Database queries"""

    def __init__(self, cursor):
        self.cursor = cursor

    def department_budget(self, department_name):
        """Get department budget by name"""
        query = "SELECT budget FROM departments WHERE name = %s;"
        self.cursor.execute(query, (department_name,))
        return self.cursor.fetchone()[0]

    def department_expenses(self, department_name):
        """Get department expenses by name"""
        department_query = "SELECT id FROM departments WHERE name = %s;"
        self.cursor.execute(department_query, (department_name,))
        department_id = self.cursor.fetchone()[0]

        expenses_query = "SELECT sum(salary) from employees where department_id = %s;"
        self.cursor.execute(expenses_query, (department_id,))
        return self.cursor.fetchone()[0]
