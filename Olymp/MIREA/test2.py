f = open('27_B.txt', 'r', encoding="UTF-8")
f = f.readlines()
f = [int(i.split("\n")[0]) for i in f]

N = f[0]
f.pop(0)
m = 80
b = 50

arr = []
arr1 = []
ans = []
t = 0

# for x in range(len(f)):
# 	for y in range(x+1, len(f)):
		if (x != y and (f[x] + f[y]) % m == 0 and (f[x] > b or f[y] > b)):
			if ([x,y] not in arr and [y,x] not in arr):
				# print([x,y])
				arr.append([x,y])


# [f[x], f[y]] not in arr and [f[y], f[x]] not in arr
# u = 49
# for i in range(len(arr)):
# 	if (arr[i][0] == u or arr[i][1] == u):
# 		print(arr[i])
print(len(arr))
