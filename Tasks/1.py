import time

def longest_palindrome(s):
    stime = time.time()
    arr = list(s)
    pos = []
    indx = []
    possible = []
    total = ""
    t = 0

    for x in range(len(arr)):
        z = arr[x]
        for i in range(len(arr)):
            if (z == arr[-(i + 1)]):
                if (-(i + 1) not in indx):
                    z1 = -(i + 1)
                    indx.append(z1)
                    break
                else:
                    continue
        for y in arr[arr.index(z):z1 + 1]:
            pos.append(y)
        for i in range(len(pos)):
            if (pos not in possible):
                if (len(pos) % 2 == 0):
                    if (pos[i] == pos[-(i + 1)]): t += 1
                    else: break #t -= 1
                else:
                    if (pos[i] == pos[-(i + 1)]): t += 1
                    elif (i == (len(pos) // 2)): t += 1
                    else: break #t -= 1
                if (t == len(pos)):
                    t = 0
                    possible.append(pos)
                # print(possible)
        pos = []
    try:
        maxm = possible[0]
        for i in range(len(possible)):
            lnm = len(maxm)
            lnp = len(possible[i])
            if (lnm < lnp):
                maxm = possible[i]
        for i in maxm:
            total += i
    except:
        return "None of possible arrays were found."
    etime = time.time()
    return total

    

print(longest_palindrome("baaaaaaaaaaaaaaaaaaaaaaaaaabkjhdfbbabiukjd")) # bab
# print(len("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))


n = int(input())
num = [input().split() for i in range(n)]
x, y, total = 0, 0, 0
s = 0
trig = False
for i in num:
    y += int(i[0])
    x = int(i[1])
    if (y <= 0 and not trig):
        s += total
        total = 0
        trig = True
    if (y >= 0 and trig):
        trig = False
        s += total
        total = 0
    total += abs(y) * x

print(s)







































#     i[0] = int(i[0])
#     i[1] = int(i[1])
#     for y in range(i[1]):
#         arr.append(i[0])
# if arr[len(arr-1)][0]>=

