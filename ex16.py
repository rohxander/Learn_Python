def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Enter your desired cheese count and boxes of crackers:")
cheese_count = input(">")
boxes_of_crackers = input(">")
cheese_and_crackers(cheese_count,boxes_of_crackers)

print("Enter your desired cheese count and boxes of crackers again:")
cheese_and_crackers(input(">"),input(">"))