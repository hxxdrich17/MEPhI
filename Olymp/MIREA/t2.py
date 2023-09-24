def Output(res, n = 8): # Приводит все элементы в единый вид
    for i in range(n):
        if (len(res[i]) == 1): res[i] = " " + res[i]
    print("  ".join(res))
    print()

""" Первый случай
    Можно заметить определённую послеовательность для каждой строчки:
        x   y
    1: +15, +1
    2: +13, +3
    3: +11, +5
    4: +9, +7
    5: +7, +9
    6: +5, +11
    7: +3, +13
    8: +1, +15
    Последовательность для этой последовательности заключается в уменьшении
    первого числа последовательности на 2 для каждой следующей строчки и в
    увеличении второго числа последовательности на 2 для каждой следующей строчки
"""
x, y = 15, 1
res = []

for a in range(8):
    res.append(str(a))
    summ = a
    for b in range(1, 8): # range(1, 8) потому что первым числом в строке будет выступать чило в переменной a
        if (b % 2 != 0): # такое условие из-за того, что для нечетного индекса последовательность по перменной x
            summ += x
        elif (b % 2 == 0): # такое условие из-за того, что для четного индекса последовательность по перменной y
            summ += y
        res.append(str(summ))
    Output(res)
    res.clear()
    x -= 2
    y += 2

print("\n")

""" Второй случай
    Можно заметить последовательность для каждой строчки:
    Смотрим справа налево и видим, что на нечетном номере строки
    числа увеличиваются на 1, а на четном номере строки уменьшаются на 1

    Первое число строки справа налево (от 1 до 7 строки, т.к. в первой строке 0)
    строится исходя из последовательности +15 для нечётного индекса, +1 для чётного
"""
summ = 0

for a in range(8):
    if (a >= 1 and a % 2 == 0):
        summ += 1
    if (a >= 1 and a  % 2 != 0):
        summ += 15
    summ1 = summ
    res.append(str(summ))
    for b in range(1, 8):
        if (a % 2 == 0):
            summ1 += 1
        elif (a % 2 != 0):
            summ1 -= 1
        res.append(str(summ1))
    res.reverse()
    Output(res)
    res.clear()

"""

"""
print()

nums = []
num = [i for i in range(64)]

for a in range(1, 9):
    nums.append(num[:a])
    if (a % 2 != 0):
        nums[-1].reverse()
    del num[:a]

for b in range(7, 0, -1):
    nums.append(num[:b])
    if (b % 2 != 0):
        nums[-1].reverse()
    del num[:b]

x, y, n = 0, 0, 7


for a in range(8):

    y1 = y + 1
    if (x >= 7):
        n -= 1

    for b in range(x, x + n + 1):
        # print(f"b: {b} | y: {y} | x: {x} | a: {a} | n: {n} | (x + n) - y1: {(x+n)-y1} | x+n+1: {x+n+1}")
        if ((x + n) - y1 < b):

            y1 -= 1
            res.append(str(nums[b][y1]))
            # print(f"y1: {y1}")

        else:
            # print(f"b: {b} | y: {y} | x: {x} | a: {a}")
            res.append(str(nums[b][y]))
    if (a == 7): res.append(str(nums[-1][-1]))
    Output(res, n)
    res.clear()
    x += 1
    y += 1


