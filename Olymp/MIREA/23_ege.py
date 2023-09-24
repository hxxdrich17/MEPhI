start = 2
end = 38
arr = [0] * (end + 1)
arr[start] = 1


# x = 1
# y = 34

# def f(x,y, i):
#   if x > y:
#     return 0
#   if x == y:
#     return 1
#   if (not i):
#     return f(x+1, y, i) + f(x+2, y, i) + f(x * 2, y, True)
#   if (i):
#     return f(x+1, y, False) + f(x+2, y, False)


# print(f(1,11,False))


# for i in range(start + 1, end + 1):
#     arr[i] += arr[i - 1] # hod + 1
#     arr[i] += arr[i - 2]
#     if (arr[-1] == 10):
#         flag = True

for i in range(start + 1, 16):
    # if (i != 10):
        arr[i] += arr[i - 1]
        # if (i - 2 >= 5):
        #     arr[i] += arr[i - 2]
        # if (i - 3 >= 5):
        #     arr[i] += arr[i - 3]
        if (i % 2 == 0):
            arr[i] += arr[i // 2]
        if (i % 3 == 0):
            arr[i] += arr[i // 3]

for i in range(16, end + 1):
    if (i != 27):
        arr[i] += arr[i - 1]
        # if (i - 2 >= 11):
        #     arr[i] += arr[i - 2]
        # if (i - 3 >= 11):
        #     arr[i] += arr[i - 3]
        if (i % 2 == 0 and i // 2 >= 15):
            arr[i] += arr[i // 2]
        if (i % 3 == 0 and i // 3 >= 15):
            arr[i] += arr[i // 3]

# for i in range(start + 1,  end + 1):
#     arr[i] += arr[i - 1]
#     if (i % 2 == 0):
#         arr[i] += arr[i // 2]
#     t = i**0.5
#     if (t ** 2 == i):
#         arr[i] += arr[int(i**0.5)]

# print(arr)

# from math import isqrt
# a = [0] * 39
# a[2] = 1

# for k in range(3, 39):
#  a[k] = a[k - 1]
#  if k % 2 == 0:
#    a[k] += a[k // 2]
#  t = isqrt(k)
#  if t ** 2 == k:
#    a[k] += a[t]
#  print(f"{k:3} {a[k]:5}")
