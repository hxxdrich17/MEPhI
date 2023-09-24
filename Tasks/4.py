n = [int(i) for i in input().split(" ")]
k = n[1]
num = list(input())
t = 0

for i in range(n[0] - 1):
    if (num[t] < num[t + 1] and k != 0):
        num.pop(t)
        k -= 1
        if (k == 0):
            break
    if (num[t] > num[t + 1] and k != 0):
        mn = min(num[t + 1:])
        num.pop(num.index(mn))
        k -= 1
        if (k == 0):
            break

print(int("".join(num)))