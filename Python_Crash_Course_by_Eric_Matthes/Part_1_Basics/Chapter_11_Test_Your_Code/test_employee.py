import unittest
from employee import Employee

class EmployeeTestCases(unittest.TestCase):
	"""Tests for the Employee class"""

	def setUp(self):
		"""
		Create an employee and a custom amount for use in all tests.
		"""

		self.annual_base_salary = 100000
		self.employee 			= Employee(
			'John',
			'Doe',
			self.annual_base_salary
		)

	def test_give_default_rise(self):
		"""Test that the default raise is applied: $105000"""

		self.employee.give_raise()
		self.assertEqual(
			self.employee.annual_salary,
			self.annual_base_salary + 5000
		)

	def test_give_custom_raise(self):
		"""Test that a custom raise is applied: $115000"""

		custom_amount = 15000
		self.employee.give_raise(custom_amount)
		self.assertEqual(
			self.employee.annual_salary,
			self.annual_base_salary + custom_amount
		)

unittest.main()
