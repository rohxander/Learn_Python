n = int(input())
i = 1
def fizzBuzz(k):
    if k%3==0 and k%5==0 :
        print("fizzBuzz")
    elif k%3==0 :
        print("Fizz")
    elif k%5==0:
        print("Buzz")
    elif k%3!=0 or k%5!=0:
        print(f"{k}")
while i <= n:
	num = fizzBuzz(i)
	i = i + 1