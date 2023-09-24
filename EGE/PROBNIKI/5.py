arr = []
x,y = 0,0
a1,a2,a3=0,0,0

for i in range(1000, 10000):
    a = [int(b) for b in str(i)]
    a1 = a[0] + a[1]
    a2 = a[1] + a[2]
    a3 = a[2] + a[3]
    l = [a1,a2,a3]
    l.remove(min(l))
    l.sort()
    x = int(str(l[0]) + str(l[1]))
    if (x == 1315):
        arr.append(i)
    
print(max(arr), arr)