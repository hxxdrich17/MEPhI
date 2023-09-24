num =(2 * (216 ** 6)) + (3 * (36 ** 9)) - 432

x = []
while (num >= 6):
    x.append(num % 6)
    num = num // 6

x.reverse()
print(str(x).count("5"))