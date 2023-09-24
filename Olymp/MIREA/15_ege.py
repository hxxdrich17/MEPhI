

# for A in range(1, 1000):
#     flag = 0
#     for x in range(1, 1000):
#         if ((x % A != 0) <= ((x % 54 == 0) <= (162 % x != 0))) == 0:
#             flag = 1
#             break
#     if (flag == 1):
#         print(A, x)
#         break


# flag1 = False
# flag2 = False

# for a in range (1, 1000):
    
#     for x in range(1, 2000):
#         if (((x <= 9) <= (x * x < a))) == False:
#             flag1 = True
#             break
#     for y in range (1, 2000):
#         if ((y * y <= a) <= (y <= 10)) == False:
#             flag2 = True
#             break
#     if (not flag1 and not flag2):
#         print(a)
#     flag1, flag2 = False, False


# flag1 = True

# for a in range(-1000, 1000):

#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (((y + 2 * x) < a) or (x > 20) or (y > 40)) == False:
#                 flag1 = False
#                 break
#         if (not flag1):
#             break
#     if (flag1):
#         print(a)
#         break
#     flag1 = True


# for a in range (0, 1000):

#     for x in range(1000):
#         if ((x & a != 0) <= ((x & 56 == 0) <= (x & 20 != 0))) == False:
#             break
#     else:
#         print(a)
#         # break


# def f(a1,a2,x):
#     return ((17 <= x <= 54) <= (((37 <= x <= 54) and (not(a1 <= x <= a2))) <= (not(17 <= x <= 54))))

# minn = 1000
# for a1 in range(-100, 100):
#     for a2 in range(a1 + 1, 100):
#         for x in range(-100, 100):
#             if (f(a1,a2,x) == False):
#                 break
#         else:
#             minn = min(minn, a2 - a1)


# print(minn)


# b = [i for i in range(50, 71)]

# for a in range(1, 1000):
#     for x in range(0, 1000):
#         if ((x % a == 0) or ((x in b) <= (x % 16 != 0))) == False:
#             break
#     else:
#         print(a)


def triangle(n, m, k):
    flag = False
    if ((n + m > k) and (m + k > n) and (n + k > m)):
        flag = True
    return flag

def fmax (a, b):
    if (a > b):
        ans = a
    elif (a <= b):
        ans = b
    return ans

for a in range(1, 1000):
    for x in range(1, 1000):
        if not((triangle(x, 12, 20) == (fmax(x, 5) <= 28)) and (triangle(x, a, 3))) == False:
            # print(x)
            break
    else:
        print(a)