class Employee:
	"""Simple class to model an Employee"""

	def __init__(self, first_name, last_name, annual_salary):
		"""Store employee info"""

		self.first_name    = first_name
		self.last_name 	   = last_name
		self.annual_salary = annual_salary

	def give_raise(self, amount=5000):
		"""Add amount to the employee annual_salary"""

		self.annual_salary += amount
