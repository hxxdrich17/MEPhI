# def f(n):
#     global t, maxdel
#     d = 1
#     arr = []
    

#     while (d * d < n):
#         if (n % d == 0):
#             arr.append(d)
#             arr.append(n // d)
#         d += 1
#         # if (len(arr) > 5):
#         #     break

#     if (d * d == n):
#         arr.append(d)
#     maxdel = max(maxdel, len(arr))
#     arr.append(i)
#     # if (len(arr) == 5):
#     #     arr.sort()
#     #     print(*arr)

#     # if (arr != []):
#     #     m = max(arr) - min(arr)
#     #     # print(str(m)[len(str(m))-3:])
#     #     if (str(m)[-1] == "8" and str(m)[-2] == "1"):
#     #         print(i, m)
#     #         t += 1
#     # if (t == 6):
#     #     return True
#     return arr
        
# t = 0
# maxdel = -1
# ans = []

# for i in range(394441, 394505 + 1):
#     # if ((i ** 0.5) == int(i ** 0.5)):
#         x = f(i)
#         ans.append(x)

# ans[9].pop(-1)
# ans[9].remove(max(ans[9]))
# print(max(ans[9]))
# ans[9].remove(max(ans[9]))
# print(max(ans[9]))
# print(maxdel)

# # for i in range(len(ans)):
# #     if (len(ans[i]) - 1 == maxdel):
#         # print(ans[i][-1], i, end="\n\n")

        






# #     while d * d < i:
# #         if (i % d == 0):
# #             dl += 2
# #             arr.append(d)
# #             arr.append(i // d)
# #         d += 1
# #     if (d * d == i):
# #         arr.append(d)
# #     if (len(arr) == 3):
# #         print(*arr)
# #         ans.append([i, max(arr)])
# #     arr.clear()
# #     dl = 0
# #     d = 2

# # ans.sort()
# # print(ans)


# # arr = []
# # ans = []
# # d = 2
# # dl = 0
# # for i in range(len(ans)):
#     # x = ans[i][0] * ans[i][1]

'''
CHAST' 2
'''

# простые числа
# def prime(n):
#     d = 2
#     while (d * d <= n):
#         if (n % d == 0):
#             return False
#         d += 1
#     return True

# def prime1(n):
#     return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# ans = []
# def primeDel(n):
#     global ans
#     d = 2
#     arr = []
#     t = 0
#     while (d * d < n):
#         if (n % d == 0):
#             arr.append(d)
#             arr.append(n // d)
#         d += 1
#     if (d * d == n):
#         arr.append(d)
#     for i in arr:
#         if (prime1(i)):
#             t += 1
#     ans.append([n, t])


# k = 0
# for i in range(2, 20000):
#     # if (prime1(i)):
#     #     k += 1
#     #     print(k, i)
#     primeDel(i)

# maxd = -1
# for i in range(len(ans)):
#     maxd = max(maxd, ans[i][1])
# t = 0
# while True:
#     if (ans[t][1] < maxd):
#         ans.pop(t)
#         t -= 1
#     t += 1
#     if (t >= len(ans)):
#         break
# print(ans, min(ans))



# -----------test-------------
def prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

arr = []
def del1(n):
    global arr
    d = 2
    while (d * d < n):
        if (n % d == 0):
            if (prime(d) and prime(n//d)):
                arr.append(n)
        d += 1

def del2(n):
    arr = []
    d = 2
    t = 0
    while (d * d < n):
        if (n % d == 0):
            if (prime(d)):
                t += 1
            if (prime(n//d)):
                t += 1
        d += 1
    return t > 3

ans1 = []
def del3(n):
    global ans
    d = 2
    arr = []
    arr1 = []
    while (d * d < n):
        if (n % d == 0):
            if (prime(d) and prime(n//d)):
                arr.append(d)
                arr.append(n//d)
                arr1.append([(n//d) - d, d, n // d])
        d += 1
    if (arr1 != []):
        ans.append(min(arr1))

def del4(n):
    global ans
    d = 2
    arr = []
    while (d * d < n):
        if (n % d == 0):
            if (prime(d)):
                arr.append(d)
            if (prime(n//d)):
                arr.append(n//d)
        d += 1
    if (len(arr) >= 6):
        ans.append([n, max(arr)])

t = 0
def del5(n):
    global t
    d = 2
    arr = []
    while (d * d < n):
        if (n % d == 0):
            if (prime(d)):
                arr.append(d)
            if (prime(n//d)):
                arr.append(n//d)
        d += 1
    summ = sum(arr)
    if (summ != 0 and summ % 11 == 0):
        t += 1
        return [n, summ, t]            

def del6(n):
    global t
    d = 2
    arr = []
    while (d * d < n):
        if (n % d == 0):
            arr.append(d)
            arr.append(n//d)
        d += 1
    if (prime(max(arr)) == False):
        t += 1
        return [n, max(arr), t]

def justDel(n):
    d = 2
    arr = []
    while (d * d < n):
        if (n % d == 0):
            arr.append(d)
            arr.append(n//d)
    if (len(arr) == 2):
        return True
    else:
        return False

def del7(n):
    global ans1
    d = 2
    arr = []
    arr1 = []
    while (d * d < n):
        if (n % d == 0):
            arr.append(d)
            arr.append(n//d)
        d += 1
    for i in range(len(arr)):
        if (prime(arr[i])):
            arr1.append(arr[i])
    flag = True
    for x in arr1:
        for y in arr1:
            for z in arr1:
                if (x != y and y != z and x != z and flag):
                    a = x * y * z
                    if (a == n):
                        ans1.append(n)
                        flag = False
                        break
        if (not flag):
            break
    
    # for i in range(0, len(arr), 2):
    #     if (prime(arr[i]) and prime(arr[i+1]) == False):
    #         if (justDel(arr[i+1])):
    #             ans.append(n)
    #     elif (prime(arr[i+1]) and prime(arr[i]) == False):




# for i in range(158928, 345293 + 1):
#     del7(i)
#     # print(ans)

# print(len(ans1), min(ans1))


# mind = 1000000
# for i in range(len(ans)):
#     mind = min(mind, ans[i][0])

# for i in range(len(ans)):
#     if (ans[i][0] == mind):
#         print(ans[i])
    

'''
CHAST 3
'''
# arr = []
# c1 = "12345"
# c2 = "7"
# c3 = "8"
# for x in range(10):
#     for y in range(10):
#         ans = int(c1+str(x)+c2+str(y)+c3)
#         if (ans % 31 == 0):
#             arr.append(ans)
#             print(ans, ans // 31)

# print(arr)

# 1000000000 == 10**9
# 000
# c1 = "1234"
# c2 = "7"
# c3 = "8"
# arr = []
# for y in range(10):
#     for x in range(100):
#         if (int(c1 + c2 + str(y) + c3) % 137 == 0 and int(c1 + c2 + str(y) + c3) not in arr):
#             arr.append(int(c1 + c2 + str(y) + c3))
#         ans = int(c1 + str(x) + c2 + str(y) + c3)
#         if (ans % 137 == 0 and ans not in arr):
#             arr.append(ans)
#         if (len(str(x)) == 1):
#             ans = int(c1 + "0" + str(x) + c2 + str(y) + c3)
#         if (ans % 137 == 0 and ans not in arr):
#             arr.append(ans)
        
# arr.sort()
# for i in arr:
#     print(i, i//137)



# 100000000 == 10**8
# 0000

# arr = []
# c1 = '11'
# c2 = '223'

# for x in range(1000):
#     # kogda -
#     a = str(x)
#     ans = int(c1 + a + c2)
#     if (ans % 149 == 0 and ans not in arr):
#         arr.append(ans)
#     for y in range(2):
#         if (len(a) == 1):
#             a = "0" + a
#         elif (len(a) == 2):
#             a = "0" + a
#         ans = int(c1 + a + c2)
#         if (ans % 149 == 0 and ans not in arr):
#             arr.append(ans)

# if (int(c1 + c2) % 149 == 0):
#     arr.append(int(c1 + c2))

# arr.sort()
# for i in arr:
#     print(i, i//149)


# 10000000000 == 10**10
# 1000

# arr = []
# c1 = "1"
# c2 = "493"
# c3 = "41"

# for x in range(1000):
#     a = str(x)
#     for y in range(10):
#         if (int(c1 + str(y) + c2 + c3) % 2023 == 0 and int(c1 + str(y) + c2 + c3) not in arr):
#             arr.append(int(c1 + str(y) + c2 + c3))
#         ans = int(c1 + str(y) + c2 + str(a) + c3)
#         if (ans % 2023 == 0 and ans not in arr):
#             arr.append(ans)
#         for i in range(2):
#             if (len(a) == 1 or len(a) == 2):
#                 a = "0" + a
#             ans = int(c1 + str(y) + c2 + str(a) + c3)
#             if (ans % 2023 == 0 and ans not in arr):
#                 arr.append(ans)
# arr.sort()
# print(arr)


# arr = []
# # a = '3261--649'
# # print(a[:4], a[6:8])


# for i in range(0, 10**9, 163):
#     a = str(i)
#     if (a[:4] == '3261' and a[6:8] == "64"):
#         if (i % 163 == 0):
#             print(i, i//163)

# a = '123456789'
# # print(a[-1])

# for i in range(0, 10**9, 2079):
#     a = str(i)
#     if (a[:2] == "33" and a[-1] == "7" and a[-4:-2] == "21"):
#         if (i % 2079 == 0):
#             print(i, i//2079)


arr = []

# for i in range(0, 10**8, 149):
#     a = str(i)
#     if (a[0:1] == "1" and a[2:5] == "234" and a[-1] == "6"):
#         print(i, i//149)

# import itertools

# def dels(n):
#     d = 1
#     # t = 2
#     arr = []
#     while (d * d < n):
#         if (n % d == 0 and d != 1):
#             arr.append(d)
#             arr.append(n//d)
#         elif (n % d == 0 and d == 1):
#             arr.append(d)
#         d += 1
#     if (d * d == n):
#         arr.append(d)
#     return arr

def check(a,dels):
    n = len(dels)
    for i in range(1,n+1):
        dd = itertools.combinations(dels,i)
        for d in dd:
            s = sum(d)
            if s == a:
                return True
    return False

# for i in range(300, 351):
#     a = dels(i)
#     if (check(i,a)):
#         print(i)




# # [153222; 153270]
# # a**2 + b**2, a <= b

# def roots(n):
#     arr = []
#     for i in range(1, n):
#         if ((i**0.5).is_integer()):
#             arr.append(int(i**0.5))
#     return arr
    
# def check(rt, i):
#     arr = []
#     for x in range(len(rt)):
#         for y in range(x, len(rt)):
#             if (rt[x] <= rt[y]):
#                 if (rt[x]**2 + rt[y]**2 == i):
#                     arr.append([rt[x], rt[y]])
#     if (len(arr) > 1):
#         return []
#     else:
#         return arr

# # 153271
# for i in range(153222, 153271):
#     rt = roots(i)
#     ans = check(rt, i)
#     # print(ans)
#     if (ans != []):
#         arr.append([ans[0][0],ans[0][1],ans[0][0]**2 + ans[0][1]**2])
# # arr1 = []
# # for i in range(len(ans)):
# #     arr1.append(ans[i][0]**2 + ans[i][1]**2)

# for i in arr:
#     print(i)
# # print(arr1)


# def dels(n):
#     d = 2
#     arr = []
#     while (d * d < n):
#         if (n % d == 0):
#             arr.append(d)
#             arr.append(n//d)
#         d += 1
#         if len(arr) > 3:
#             return False
#     if (d * d == n):
#         arr.append(d)
    
#     if (len(arr) == 3):
#         flag = True
#         for i in range(len(arr)):
#             if (arr[i] % 2 != 0):
#                 flag = False
#         if flag: return True
#         else: return False
#     else:
#         return False
    


# for i in range(101000000, 102000000 + 1):
#     if i % 2 == 0:
#         count = 1
#         sqrtI = round(i ** 0.5)
#         for j in range(2, sqrtI + 1):
#             if i % j == 0:
#                 if j % 2 == 0:
#                     count += 1
#                 k = i // j
#                 if k % 2 == 0:
#                     count += 1
#                     if j == k:
#                         count -= 1
#                 if count > 3:
#                     break
#         if count == 3:
#             print(i)