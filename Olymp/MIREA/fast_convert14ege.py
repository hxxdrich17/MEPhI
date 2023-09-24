import pyperclip3

num = input()
ss = num.split()[1]
num = num.split()[0]
sym = "+-%/*–"
alp = "abcdefghijklmnopqrstuvwxyzабфвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a,b = "", ""
n = 0
for i in range(len(num)):
    if (num[i] in sym):
        n = i
        break
    a += num[i]

for i in range(n + 1, len(num)):
    if (num[i] in sym):
        break
    b += num[i]

a = a[:len(a) - len(ss)]
b = b[:len(b) - len(ss)]
ans1, ans2 = "a = ", "b = "
# print(a,b)
for i in range(len(a) - 1, -1, -1):
    # print(a[-i-1] in alp)
    if (a[-i-1] in alp):
        # print(1, a[-i-1])
        pass
    elif (i == 0):
        # print(2, a[-i-1])
        ans1 += f"({a[-i-1]} * {ss} ** {i})"
    else:
        # print(3, a[-i-1])
        ans1 += f"({a[-i-1]} * {ss} ** {i}) + "

for i in range(len(b) - 1, -1, -1):
    # print(b[-i-1] in alp)
    if (b[-i-1] in alp):
        # print(1, b[-i-1])
        pass
    elif (i == 0):
        # print(2, b[-i-1])
        ans2 += f"({b[-i-1]} * {ss} ** {i})"
    else:
        # print(3, b[-i-1])
        ans2 += f"({b[-i-1]} * {ss} ** {i}) + "


pyperclip3.copy(f"{ans1}\n{ans2}")
