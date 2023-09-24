n = int(input())
diff = []
total, t = 0, 0
p, m = [], []

for i in range(n):
    x = [int(y) for y in input().split(" ")]
    p.append(x[0])
    m.append(x[1])

for x in range(n):
    diff.append(m[x] - p[x])
    if (p[x] <= m[x]):
        t += 1
    
if (t == n):
    print(sum(p))
else:
    mn = min(diff)
    p.pop(diff.index(mn))
    total += m[diff.index(mn)] + sum(p)
    print(total)