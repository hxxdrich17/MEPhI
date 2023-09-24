n = int(input())
arr = []
for i in range(n):
    a = input().split()
    arr.append([int(z) for z in a])

# 1-st case
ans1 = 0
k = 1
for x in range(n):
    for y in range(k, n):
        ans1 += arr[x][y]
    k += 1

print(ans1)


# 2-nd case
ans2 = 0
k = 0
for x in range(n):
    ans2 += arr[x][k]
    k += 1

print(ans2)

# 3-rd case
ans3 = 0
k = 1

for x in range(1, n):
    for y in range(k):
        ans3 += arr[x][y]
    k += 1

print(ans3)