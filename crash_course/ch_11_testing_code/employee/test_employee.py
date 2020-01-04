import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test the Employee class"""
    def setUp(self):
        """Create an employee and define a custom raise value"""
        self.employee = Employee('John', 'Doe', 50000)
        self.raise_amount = 20000

    def test_give_default_raise(self):
        """Test for the default raise amount of 5000"""
        self.employee.give_raise()
        self.assertEqual(55000, self.employee.salary)

    def test_give_custom_raise(self):
        """Test for a custom raise amount defined in setUp"""
        self.employee.give_raise(self.raise_amount)
        self.assertEqual(70000, self.employee.salary)

if __name__ == '__main__':
    unittest.main()
