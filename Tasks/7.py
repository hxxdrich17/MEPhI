n, m = [int(i) for i in input().split(" ")]
a = [int(i) for i in input().split(" ")]
poss, poss1 = "", ""

for i in range(1, n + 1):
    x = list(str(a[i]))
    for y in range(len(x)):
        if (x[y] == i):
            pass