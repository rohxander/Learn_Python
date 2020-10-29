class Employee:
	raise_amount= 1.04
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

	@classmethod
	def set_raise_amt(cls, amount): 
		cls.raise_amount = amount
		
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

emp_1 = Employee('Corey', 'Schefer', 50000)
emp_2 = Employee('Test', 'User', 60000)




# Employee.set_raise_amt(1.05)
# print(Employee.num_of_emps)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

