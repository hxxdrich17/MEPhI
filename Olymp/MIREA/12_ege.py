# a1 = '1' * 20 +'2' * 10 +'3' * 70
# for x in range(100):
#     for y in range(100):
#         for z in range(100):
#             a = "0" + "1" * x + "2" * y + "3" * z
#             a1 = a


#             while ('01' in a or '02' in a or '03' in a):
#                 a = a.replace('01', '30', 1)
#                 a = a.replace('02', '101', 1)
#                 a = a.replace('03', '202', 1)
#             if (a.count('1') == 20 and a.count('2') == 10 and a.count('3') == 70):
#                 print(a, a1, a1.count('1'))
#                 break

# while ('30' in a or '101' in a or '202' in a):
#     if ('30' in a):
#         a = a.replace('30', '01', 1)
#     if ('101' in a):
#         a = a.replace('101', '02', 1)
#     if ('202' in a):
#         a = a.replace('202', '03', 1)
# print(a)
# print(a.count('1'))
# print(a.count('2'))
# print(a.count('3'))
# print('01111111111111111111111111111111111111111111111111122222222223333333333'.count('1'))

# ans = 0
# for i in range(len(a)):
#     if (a[i].isdigit()):
#         ans += int(a[i])

# arr = []
# for i in range(201, 1000):
#     a = "1" * i
#     a1 = a
#     while ('1111' in a):
#         a = a.replace('1111', '22', 1)
#         a = a.replace('222', '1', 1)

#     arr.append(a.count('1'))


# print(max(arr))

# a = '8' * 100

# while ('888' in a or '77' in a):
#     if ('888' in a):
#         a = a.replace('888', '8777', 1)
#     else:
#         a = a.replace('77', '8', 1)

# print(a, a.count('8'), a.count('7'))


# a = '2' * 30 +'3' * 30 +'1' * 30
# a = '232323232323232323232323232323232323232323232323232323232323' + '1' * 30

# while ('21' in a or '23' in a):
#     if ('21' in a):
#         a = a.replace('21', '11', 1)
#     else:
#         a = a.replace('23', '21', 1)

# print(a, a.count('1'))

# 212121212121212121212121212121212121212121212121212121212121

# a = '7' * 40 + '9' * 40 + '4' * 50

# while ('49' in a or '97' in a or '47' in a):
#     if('47' in a):
#         a = a.replace('47', '74', 1)
#     if('97' in a):
#         a = a.replace('97', '79', 1)
#     if('49' in a):
#         a = a.replace('49', '94', 1)

# print(a)
# print(a[25], a[71], a[105])


for x in range(100):
    for y in range(100):
        for z in range(100):
            a = '0' + '1' * x + '2' * y + '3' * z + '0'
            a1 = a

            while ('00' not in a):
                a = a.replace('01', '210', 1)
                a = a.replace('02', '320', 1)
                a = a.replace('03', '3012', 1)

            if (a.count('1') == 26 and a.count('2') == 54 and a.count('3') == 48):
                print(a, a1, len(a1))



# --------- CHAST 2 -------------------
import pyperclip

def copy(a):
	pyperclip.copy(a)
	print(a)

# arr = []


# a = "1" * 81

# while ("1111" in a or '88888' in a):
# 	if ('1111' in a):
# 		a = a.replace('1111', '888', 1)
# 	else:
# 		a = a.replace('88888', '888', 1)


# print(arr)
# copy(a)



# X: -7 + N * (15 + a) + 23 = 1

# Y: -1 + N * (22 + b) - 32 = -3


# N * ... = -15
# N * ... = 30


