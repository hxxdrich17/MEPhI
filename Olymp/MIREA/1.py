n, m = [int(i) for i in input().split()]
arr = []

for i in range(n):
    arr.append([int(i) for i in input().split()])

mx = [-100, 0]
for x in range(n):
    a = arr[x]
    for y in range(m):
        if (arr[x][y] > mx[0]):
            mx = [arr[x][y], y]

for i in range(n):
    arr[i][0], arr[i][mx[1]] = arr[i][mx[1]], arr[i][0]

for i in range(len(arr)):
    a = " ".join([str(i) for i in arr[i]])
    print(a)