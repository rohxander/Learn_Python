states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

cities = {
	'CA' : 'San Fransisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville',
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY state has :", cities['NY'])
print("OR State has :", cities['OR'])

print('-'*10)
print("Michigan has :", cities[states['Michigan']])
print("Florida has :", cities[states['Florida']])

print('-'*10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

print('-'*10)
for abrev, city in list(cities.items()):
	print(f"{abrev} has the city {city}")

print('-'*10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated as {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-'*10)
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX'is: {city}")