k = 0
i = 0
a = int(input())
b = input().split()
b.sort(reverse=True)
print(b)
while(k == a):
	if(b[i] == b[i + 1]):
		k = k +1
		i = i + 1
	else:
		break
print(b[i])
