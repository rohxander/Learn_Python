print("Enter the number of people.")
people = input(">")

print("Enter the number of cars.")
cars = input(">")

print("Enter the number of trucks.")
trucks = input(">")

if cars > people:
	print("We should take cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

if people > trucks:
	print("Alrigh, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")