n = int(input())
k = 0
x = 0

vill = []
hero = []
result = []
while k != n :
	a = int(input())
	vill = list(map(int,input().strip().split()))[:a]
	hero = list(map(int,input().strip().split()))[:a]
	vill.sort()
	hero.sort()
	while(x <= (a-1)) :
		if(vill[x] < hero[x]):
			x = x + 1
			if (x==a):
				print("WIN")
		else:
			print("LOSE")
			break
	k = k + 1