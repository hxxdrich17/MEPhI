def copy(ans):
	import pyperclip
	pyperclip.copy(ans)
	print(ans)


# ch1 = 1 * 37**3 + 2 * 37**2 + 3 * 37**1
# ch2 = 4 * 37**3  + 5 * 37**1 + 9


# for p in range(10, 100):
# 	for x in range(p):
# 		for y in range(p):
# 			ch1 = 3 * p**3 + 4 * p**2 + x * p + 5
# 			ch2 = x * p**3 + 9 * p**2 + x * p + 3
# 			ch3 = y * p**3 + y * p**2 + 6 * p + 8
# 			if (ch1 + ch2 == ch3):
# 				copy(y * p**3 + x * p**2 + x * p + y)
# 				break


# ch1 = 3 * 111**2 + 2 * 111**1 + 1
# ch2 = 1 * 211**3 + 7 * 211**2 + 4

# flag = True
# arr = []

# for x in range(111):
# 	# for y in range(21):
# 	ans = ch1 + x * 111 ** 3 + ch2 + x * 211
# 	if (ans % 111 == 0):
# 		arr.append(x)
# # if (flag):
# # 	arr.append(x)
# # flag = True

# copy((ch1 + 17 * 111 ** 3 + ch2 + 17 * 211) // 111)





# ch1 = 2 * 158**4 + 7 * 158**3 + 3 * 158**2 + 2
# ch2 = 1 * 158**4 + 3 * 158**2 + 9 * 158 + 0

# arr = []

# for x in range(158):
# 	ans = ch1 + x * 158 + ch2 + x * 158**3
# 	if (ans % 73 == 0):
# 		arr.append(x)

# ans = 0

# for i in range(len(arr)):
# 	ans += (ch1 + arr[i] * 158 + ch2 + arr[i] * 158**3) // 73


# copy(ans)


def ss(num, osn):
	ans = ""
	dlt = osn
	t = 0
	while num >= dlt:
		t += 1
		ans += str(num % dlt)
		num = num // dlt
		if (num < dlt):
			ans += str(num % dlt)
		if (t > 1000):
			break
	ans = ans[::-1]
	print(ans)
	return ans



# num = 8**4024 - 4**1605 + 2**1024 - 126

# copy(ss(num, 2).count("1"))


# arr = []

# for x in range(1000000):
# 	ch1 = x
# 	ch2 = hex(x)[2:]
# 	ch3 = oct(x)[2:]
# 	if (len(ch2) == 2 and ch2[1] == "a" and len(ch3) == 3):
# 		arr.append(x)

# print(arr, len(arr))

arr = []

for n in range(1, 64):
	a = ss(63, n)
	if (len(a) >= 2):
		if (a[-1] == "3" and a[-2] == "2"):
			arr.append(n)

print(arr, len(arr))