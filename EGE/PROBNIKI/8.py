import itertools

alp = "0123456789"

arr = list(set(itertools.permutations(alp, 6)))

flag = False
count = 0
print(arr)
for i in arr:
    if (i[0] != "0"):
        x = int(i[0] + i[1] + i[2] + i[3] + i[4] + i[5])
        if (x % 5 == 0):
            for a in range(1,6):
                if (int(i[a]) % 2 == 0 and int(i[a - 1]) % 2 == 0):
                    flag = True
                    break
                if (int(i[a]) % 2 != 0 and int(i[a - 1]) % 2 != 0):
                    flag = True
                    break
            if (not flag):
                count += 1
            flag = False


print(count)














# for a1 in alp:
#     for a2 in alp:
#         for a3 in alp:
#             for a4 in alp:
#                 for a5 in alp:
#                     for a6 in alp:
