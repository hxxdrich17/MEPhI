
# f = open('26-42.txt')
# x, y = f.readline().split()
# y = int(y)
# for_B_price = []
# for_B_kol = []
# for i in f:
#     if 'A' in i:
#         a, b, c = i.split()
#         y -= int(a) * int(b)
#     else:
#         a2, b2, c2 = i.split()
#         for_B_price.append(int(a2))
#         for_B_kol.append(int(b2))
# mini = min(for_B_price)
# index_mini = 0
# for i in range(len(for_B_price)):
#     if mini == for_B_price[i]:
#         index_mini = i
# kol_B = 0
# while y > for_B_price[index_mini]:
#     y -= for_B_price[index_mini]
#     for_B_kol[index_mini] -= 1
#     kol_B += 1
#     if for_B_kol[index_mini] == 0:
#         for_B_price[index_mini] = 1000000000
#         mini = min(for_B_price)
#         for i in range(len(for_B_price)):
#             if mini == for_B_price[i]:
#                 index_mini = i
# print(kol_B, y)


f = open('26_54.txt', 'r', encoding="utf-8")
f = f.readlines()
n, s = [int(i) for i in str(f[0]).split(" ")]
f.pop(0)
f = [int(i.split("\n")[0]) for i in f]
f.sort(reverse=True)
print(n,s)

sum1 = 0
sum2 = 0
t = 0
kol = 0
ans = []
a = 0

arr = [0 for i in range(n)]

for i in range(n - 1):
    if (s - f[i+1] <= 0):
        arr[t] = sum(arr) + f[i]
        t += 1
        s = 600
    else:
        arr[t] = sum(arr) + f[i]

print(t, arr)

