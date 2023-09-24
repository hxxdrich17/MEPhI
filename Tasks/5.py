n = int(input())
total = 1

for i in range(0, int(n / 2) + 1):
    if (i == 0):
        total = total * n
        for y in range(1, int(n / 2) + 1):
            if n % y == 0:
                total = total * y
        if (total == n):
            print(n)
            break
        else:
            total = 1
    elif n % i == 0:
        total = total * i
        for y in range(1, int(i / 2) + 1):
            if i % y == 0:
                total = total * y
        if (total == n):
            print(i)
            break
        else:
            total = 1






# n = int(input())
# div = []
# total = 1

# for i in range(1, int(n / 2) + 1):
#     if n % i == 0:
#         div.append(i)

# div.append(n)

# for y in div:
#     total = total * y
#     for i in range(1, int(y / 2) + 1):
#         if y % i == 0:
#             total = total * i
#     if (total == n):
#         print(y)
#         break
#     else:
#         total = 1
