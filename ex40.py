class Employee:
	def __init__(self, shit, last, pay):
		self.fname = shit
		self.last = last
		self.pay = pay
		self.email = shit + '.' + last + '@company.com'

	def fullname(self):
		return f"{self.fname} {self.last}"

emp_1 = Employee('Corey', 'Schefer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)
print(emp_2.email)

print(emp_1.fullname())