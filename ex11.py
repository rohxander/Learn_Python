from sys import argv

script,user_name = argv

prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.\n")
print("I'd like to ask you a few questions.\n")
print(f"Do you like me {user_name}?\n")
likes= input(prompt)

print(f"Where do you live {user_name}?\n")
lives = input(prompt)

print("What kind of computer do you have?\n")
computer = input(prompt)

print(f"""
	Alright, so you said {likes} about liking me.
	You live in {lives}. Not sure where it is.
	And you have a {computer} computer. Nice.""")