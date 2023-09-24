n,m = int(input()), int(input())
arr = [int(input()) for i in range(n)]

x = 0

while (True):
    for i in range(arr[x]):
        arr.append(arr[x])
    x += 1
    if (m <= len(arr)):
        print(arr[m-1])
        break