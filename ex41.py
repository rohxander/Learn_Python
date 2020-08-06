class Employee:
	num_of_emps = 0

	def __init__(self, shit, last, pay):
		self.fname = shit
		self.last = last
		self.pay = pay
		self.email = shit + '.' + last + '@company.com'

		Employee.num_of_emps += 1 

	def fullname(self):
		return f"{self.fname} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('Corey', 'Schefer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)