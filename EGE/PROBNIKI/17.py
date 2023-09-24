f = open("17.txt", "r", encoding="UTF-8")
f = f.readlines()
f = [int(i.split("\n")[0]) for i in f]

count = 0
arr = []

for i in range(2, len(f)):
    if (int(f[i]^2) == int(f[i-1]^2 + f[i-2]^2) or int(f[i - 1]^2) == int(f[i]^2 + f[i-2]^2) or int(f[i - 2]^2) == int(f[i]^2 + f[i-1]^2)):
        count += 1
        arr.append(f[i] + f[i-1] + f[i-2])



print(count, max(arr))