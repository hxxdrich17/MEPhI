# f = open("Olymp/MIREA/24E.txt", "r", encoding="UTF-8")
# f = f.readlines()
# f = f[0]

# t = 1
# arr = []
# flag = False
# x = ""
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# num = "0123456789"

dic = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
}
# # zc = 0
# for i in range(1, len(f)):
#     if (f[i] != "Q" or f[i] == "Q" and f[i-1] != "Q"):
#         t += 1
#     else:
#         arr.append(t)
#         t = 1

# # print(f.count("XVI"))

# # k = 1
# # max_k = 1

# # for i in range(1, len(f)):
# #     if f[i] != '0' or f[i] == '0' and f[i-1] != '0':
# #         k += 1
# #         max_k = max(k, max_k)
# #     else:
# #         k = 1
    
# # print(max_k)
# # for i in alp:
# #     arr.append([dic.get(i), i])

# # print(dic.values())
# print(arr, max(arr))
# # print(f.count("KOT"))



######### PART 2 ##########


# for a in f:
#     for i in range(1, len(a) - 1):
#         if (ord(a[i]) > ord(a[i-1]) and ord(a[i]) > ord(a[i+1])):
#             local_max.append(i)
#         if (len(local_max) == 2):
#             arr.append(local_max[1] - local_max[0])
#             local_max.clear()

# print( max(arr))


# alp = "ABCDEF"
# kol = []
# x = f[0]
# for i in range(len(x) - 2):
#     if (alp.index(x[i]) <= alp.index(x[i+1]) and alp.index(x[i+1]) <= alp.index(x[i+2])):
#         kol.append([x[i] + x[i+1] + x[i+2], i])

# print(kol)
# print(len(kol),kol[-1][1])

# a = f[0]
# arr = []
# c = 0

# for i in range(len(a) - 2):
#     if (a[i] == a[i+2]):
#         dic[a[i+1]] += 1
    
# print(dic)

# a = f[0]
# arr = []
# k = 0

# alp = "ABCD"

# for i in range(len(a) - 2):
#     if (a[i+1] == "A" and a[i+2] == "D"):
#         dic[a[i]] += 1
    
# print(dic)

################### PART 3 #####################

# for i in range(len(f)):
#     x = f[i]
#     for a in range(1, len(x)):
#         if (x[a] == x[a-1]):
#             t += 1
#         else:
#             arr.append([t, i])
#             t = 1

# max1 = arr[0][0]
# for i in range(len(arr)):
#     x = arr[i]
#     if (x[0] >= max1):
#         max1 = max(x[0], max1)
#         print(x)
# # f[161] - 10 sym
# print("---------------")
# for i in alp:
#     g = f[161].count(i)
#     if (g != 0):
#         arr1.append([g, i])

# print(min(arr1)) # Z
# print("---------------")
# for i in range(len(f)):
#     ans += f[i].count("Z")

# print(ans)


# for i in range(len(a)):
#     if (a[i] == "A"):
#         for s in range(i+1, len(a)):
#             if (a[s] == "A"):
#                 t += 1
#                 if (t >= 12 and b >= 2):
#                     ans += 1
#                     b = 0
#                     t = 1
#                     break
#                 else:
#                     b = 0
#                     t = 1
#                     break
#             if (a[s] == "B"):
#                 b += 1
#             t += 1

# print(ans)


f = open("24 (6).txt", "r", encoding="UTF-8")
f = f.readlines()
f = [i.split("\n")[0] for i in f]
# print(f)
ans = 0
t = 0
arr = []
arr1 = []
local_max = []
max1 = -1
max2 = 0
char = ""
flag = False
b = 0

a = f[0]

for x in range(len(a)):
    for y in range(x, len(a)):
        if (a[y] == "A" or a[y] == "B"):
            b += 1
        if (b > 3):
            arr.append(t)
            t = 0
            b = 0
            break
        else:
            t += 1

print(arr)
print(max(arr))

# print(dic)
# print(max(dic.values()))
# print(t)
# print(arr)
# print(max(arr))
# print(ans)
# print(max(arr))
# print(char)