lst = []
num = 0
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele)
print(lst)
while(num < len(lst)):
	if lst[num] >= 0:
		print(lst[num], end = " ")
	num += 1