n = int(input())
arr = []
for i in range(n):
    arr.append([int(i) for i in input().split()])

ans = []

for x in range(n):
    ans.append([])
    for y in range(n):
        ans[x].append(arr[y][x])

for i in range(n):
    print(" ".join([str(x) for x in ans[i]]))