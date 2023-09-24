n, m = [int(i) for i in input().split()]
a = input()
b = input()

ans = []
p = 0

mx = max(n,m) - min(n,m)
if (len(a) < len(b)):
    a = "0" * mx + a
else:
    b = "0" * mx + b
    
for i in range(len(a) - 1, -1, -1):
    x1 = int(a[i])
    x2 = int(b[i])
    summ = x1 + x2 + p
    ost = summ % 10
    p = summ // 10
    ans.append(ost)
    if (i == 0 and p == 1):
        ans.append(1)

ans.reverse()
print("".join([str(i) for i in ans]))