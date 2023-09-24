f = open("ЕГЭ/Stepik/Подготовка/24.txt", "r", encoding="UTF-8")
f = f.readlines()
res = 0
for i in range(len(f)):
    if (f[i].count("E") > f[i].count('A')):
        res += 1

print(res)