the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', '2', 'dimes', 3, 'quarters']

for number in the_count:
	print(f"This is count {number}")

for fruit in fruits:
	print(f"This is the {fruit}")

for i in change:
	print(f"I got {i}")

elements = []

for ok in fruits:
	print(f"Adding {ok} to the list.")
	elements.append(fruits)

# for i in elements:
print(f"Element is: {elements}")
