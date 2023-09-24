f = open("24var05-08.txt")
f = f.readline()

arr = []
t = 0
for i in range(len(f) - 2):
    if (f[i] == "0" and f[i+1] == "0" and f[i+2]=="0"):
        arr.append(t)
        t = 0
    else:
        t += 1
arr.append(t)
    
print(arr)