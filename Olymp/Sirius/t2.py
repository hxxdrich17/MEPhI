a,b,c,k = int(input()),int(input()),int(input()),int(input())

# a1 = [i + 1 for i in range(a * 3)]
# b1 = [a1[-1]+i+1 for i in range(b * 3)]
# c1 = [b1[-1]+i+1 for i in range(c * 3)]
# # print(a1,b1,c1)

total = [] # 0,9,13
arr = []

# if (k <= a):
#     total.append([i for i in range(k*3-2, k*3+1)])
#     total.append([i for i in range(k*3+7, k*3+10)])
#     total.append([i for i in range(k*3+9+13, k*3+25)])
# elif( k > a and k < c):
#     total.append([i for i in range(k*3+7, k*3+10)])
#     total.append([i for i in range(k*3+9+13, k*3+25)])
# elif ( k > b and k <= c):
#     total.append([i for i in range(k*3+9+13, k*3+25)])

# print(total)
# for i in range(1, c+1):
#     if (i <= a and i <= b and i <=c):
#         arr.append()

a1 = [i + 1 for i in range(a * 3)]
b1 = [a1[-1]+i+1 for i in range(b * 3)]
c1 = [b1[-1]+i+1 for i in range(c * 3)]
# print(a1,b1,c1)

if (k <= a):
    [print(a1[i]) for i in range(k*3-2-1, k*3)]
if (k <= b):
    [print(b1[i]) for i in range(k*3-2-1, k*3)]
if (k <= c):
    [print(c1[i]) for i in range(k*3-2-1, k*3)]

