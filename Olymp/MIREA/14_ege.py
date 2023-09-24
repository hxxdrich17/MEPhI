# # шаблон для одного X
# # 16:  1 2 3 4 5 6 7 8 9 A(10) B(11) C(12) D(13) E(14) F(15)
# # 135x7_15 + 7x531_15 1x11 10 13 16+212x151416
# a = (1 * 15 ** 4) + (3 * 15 ** 3) + (1 * 15 ** 2) + (1 * 15 ** 0)
# b = (1 * 17 ** 3) + (3 * 17 ** 2) + (3 * 17 ** 0)

# # (..min(x)..)_15 + (..min(x)..)_15 % 14_10 == 0 ?
# end = int(input())
# d = int(input())

# for x in range(0, end):
# # for x in range(0, 17):
#     # s = a + b + (x * end ** 2) + (x * end ** 4)
#     s = a + b + (x * 15 ** 1) + (x * 17 ** 1)
#     if (s % d == 0):
#         print(x, s // d)


# # Шаблон для Y и X

# a = (2 * 22 ** 3) + (3 * 22 ** 2) + (5 * 22 ** 0)
# b = (6 * 13 ** 4) + (7 * 13 ** 3) + (9 * 13 ** 1)

# flag = True

# for x in range(0, 22):
#     for y in range(0, 13):
#         # s = a + b + (x * 21 ** 1) + (y * 21 ** 2) + (y * 21 ** 2)
#         s1 = a + (x * 22 ** 4) + (x * 22 ** 1)
#         s2 = b + (y * 13 ** 2) + (y * 13 ** 0)
#         s = s1 - s2
#         # if (s % 57 != 0):
#         #     flag = False
#         #     break
#         if (s % 57 == 0):
#             print(x,y, s // 57, s % 57)
#     # if (flag):
#     #     print(x, (a + b + (5 * 21 ** 2) + (5 * 21 ** 2) + (x * 21 ** 1)) // 18) 
#     flag = True

# # шаблон для M,N,A с y,x
# m = (2 * 15 ** 5) + (2 * 15 ** 3) + (3 * 15 ** 2) + (5 * 15 ** 0)
# n = (6 * 13 ** 4) + (7 * 13 ** 3) + (9 * 13 ** 1)
# flag = False
# arr = []
# for x in range(0, 15):
#     for y in range(0, 13):
#         sm = m + (y * 15 ** 4) + (x * 15 ** 1)
#         sn = n + (x * 13 ** 2) + (y * 13 ** 0)
#         for i in range(m):
#             if ((sm + i) % sn == 0):
#                 arr.append(i)
    
# print(min(arr))

# # шаблон для минимального x с переводом в СС и условием по кол-ву итоговых чисел в СС
# ss = 7
# ans = []
# x = 0
# while True:
#     n = 343**5 + 7 ** 3 - 1 - x
#     while True:
#         ost = n % ss
#         n = n // ss
#         ans.append(ost)
#         if (n // ss == 0):
#             ans.append(n % ss)
#             break
#     if (ans.count(6) == 12):
#         print(x)
#         break
#     ans.clear()
#     x += 1

# ans.reverse()
# # print(ans.count(4))
# print(ans)

# # шаблон для промежутка x с максимальной суммой отдельных чисел в промежуточных СС
# n = 1234
# arr = []
# ans = []

# for i in range(2, 11):
#     while True:
#         ost = n % i
#         n = n // i
#         ans.append(ost)
#         if (n // i == 0):
#             ans.append(n % i)
#             break
#     arr.append([sum(ans), i])
#     ans.clear()
#     n = 1234
# print(arr)
# print(max(arr))



