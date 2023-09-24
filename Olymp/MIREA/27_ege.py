import pyperclip


def copy(text):
	pyperclip.copy(text)
	print(text)


f = open('27_A (4).txt', 'r', encoding='utf-8')
f = f.readlines()
n = int(f[0])
f.pop(0)

arr = []

for i in range(len(f)):
	a = f[i].split(" ")
	arr.append([int(a[0]), int(a[1].split("\n")[0])])

arr1 = []
nxt = []
ans = 0
t = 0
flag = False


print(arr)

















# [8, 20, 5, 7, 13, 19]
#  0,  1, 2, 3,  4,  5

# def func(n1, summ, t, f):
# 	if (n1 != 0):
# 		n = n1[0]
# 	else:
# 		n = n1
# 	if (t == 3):
# 		return summ
# 	if (n != (len(f) - 1) and n != 0):
# 		# print(1)
# 		summ += 4 * t * f[n-1] + 4 * t * f[n+1]
# 		if (t != 0):
# 			nxt = 
# 		else:
# 			nxt = [n-1, n+1, n]
# 		t += 1
# 	elif (n == 0):
# 		# print(2)
# 		summ += 4 * t * f[-1] + 4 * t * f[n+1]
# 		if (t != 0):
# 			nxt = 
# 		else:
# 			nxt = [-1, n+1, n]
# 		t += 1
# 	elif (n == (len(f) - 1)):
# 		# print(3)
# 		summ += 4 * t * f[n-1] + 4 * t * f[0]
# 		if (t != 0):

# 		else:
# 			nxt = [n-1, 0, n]
# 		t += 1
# 	# print(summ)
# 	return func(nxt, summ, t, f) + func(nxt, summ, t, f)

# for i in range(len(f)):
# 	print(func(i, 0, 0, f))

# for x in range(len(f)):
# 	start = f[x]
# 	idst = x
# 	ans = 0
# 	t = 1
# 	if (idst != (len(f) - 1)):
# 		ans += 4 * t * f[x-1] + 4 * t * f[x+1]
# 		nxt = [x-1, x+1]
# 	elif (idst == (len(f) - 1)):
# 		ans += 4 * t * f[x-1] + 4 * t * f[0]
# 		nxt = [x-1, 0]
# 	for y in range(len(f)):
		
# 		for z in range(2):







# def fu(n, s, t, f, arr):
# 	if (t == 3):
# 		return s, n+1, arr
# 	if (n != len(f) - 1):
# 		s += t * f[n+1]
# 		arr.append([f[n+1], n])
# 		n += 1

# 	elif (n == len(f) - 1):
# 		s += t * f[0]
# 		arr.append([f[0], n])
# 		n = 0

# 	t += 1
# 	return fu(n, s, t, f, arr)

# def fu2(n, s, t, f, arr1):
# 	if (t == 3):
# 		return s, n-1, arr1
# 	if (n != len(f) - 1):
# 		s += t * f[n-1]
# 		arr1.append([f[n-1], n-1])
# 		n = n - 1
# 	elif (n == len(f) - 1):
# 		s += t * f[n-1]
# 		arr1.append([f[n-1], n-1])
# 		n = n - 1

# 	t += 1
# 	return fu2(n, s, t, f, arr1)


# for i in range(len(f)):
# 	a = fu(i, 0, 1, f, [])
# 	b = fu2(i, 0, 1, f, [])
# 	print(a[0] + b[0] + 3 * f[b[1]])
# 	# print(f[i], a[2], a[1])
# 	# print(f[i], b[2], b[1])



# [8, 20, 5, 7, 13, 19]
#  0,  1, 2, 3,  4,  5