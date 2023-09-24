
t = 0
arr = []
for i in range(100):
    x = str(i)
    n = bin(i)[2:]
    x = sum([int(a) for a in x])
    if (x % 2 == 0):
        n = n + '0'
    else:
        n = n + '1'
    x = str(int(n,2))
    x = sum([int(a) for a in x])
    if (x % 2 == 0):
        n = n + '0'
    else:
        n = n + '1'
    x = str(int(n,2))
    x = sum([int(a) for a in x])
    if (x % 2 == 0):
        n = n + '0'
    else:
        n = n + '1'
    r = int(n, 2)
    # if (r >= 123456789 and r <= 1987654321):
    t += 1
    arr.append(r)
    # if (r > 1987654321):
    #     print('STOP')
    #     break
    # if (r >= 123456789):
    #     print(r, i)
    #     break

print(t)
print(arr[0], arr[-1])
print("start")
for i in range(len(arr) - 1):
    print(arr[i+1] - arr[i])