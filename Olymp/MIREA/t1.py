k, s = int(input()), int(input())
n = [int(input()) for i in range(15)]
arr = []
arr1 = n.copy()

for i in range(k, s - 1):
	arr.append(n[i])
	arr1.remove(n[i])

arr.reverse()

for i in range(15 - len(arr)):
	if (i == k):
		for i in range(len(arr)):
			print(arr[i])
		break
	else:
		print(arr1[i])
print("#################################")
print(len(arr), k, 15- k -len(arr))
for i in range(15 - len(arr) - k, 15):
    print(i)

print(arr1, arr)