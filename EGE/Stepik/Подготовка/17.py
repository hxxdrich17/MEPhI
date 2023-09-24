f = open("ЕГЭ/Stepik/Подготовка/17.txt", "r", encoding="UTF-8")
f = f.readlines()
f = [int(i.split("\n")[0]) for i in f]

d = 160
p = 7
mx = 0
s = 0

for x in range(len(f) - 1):
    for y in range(x + 1, len(f)):
        if (f[x] % d != f[y] % d and 
        (f[x] % p == 0 or f[y] % p == 0)):
            s += 1
            mx = max(mx, f[x] + f[y])

print(s, mx)



