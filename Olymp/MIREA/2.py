n = int(input())
num = list(input())
num.sort(reverse=True)
mx = int("".join(num))
print(mx)
num.sort()
for i in range(len(num)):
    if (num[i] != "0"):
        num[0], num[i] = num[i], num[0]
        break
mn = int("".join(num))
print(mn)