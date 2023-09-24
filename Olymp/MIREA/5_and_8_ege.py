
# for n in range(1, 100):
#     x = bin(n)[2:]
#     for i in range(len(x)):
#         if (x[i] != "0"):
#             num = len(x[i:])
#             break
#     if (num % 2 == 0):
#         x1 = x[:len(x)//2] + "1" + x[len(x)//2:]
#     else:
#         x1 = x
    
#     r = int(x1, 2)
#     if (r <= 26):
#         print(r, n)
        





























# 8 zadanine
import itertools

alp = "АЗЛОПЬ"
k = 0
flag = False
arr = []
# word = []
# pos = itertools.product(alp, repeat=7)
# pos = itertools.permutations(alp)
# arr = []
# for i in pos:
#     arr.append(list(i))

# for i in range(len(arr)):
#     if (arr[i][0] != "Б"):
#         if ("ЕА" not in "".join(arr[i])):
#             print("".join(arr[i]))
#             k += 1

for x1 in alp:
    for x2 in alp:
        for x3 in alp:
            for x4 in alp:
                for x5 in alp:
                    for x6 in alp:
                        k += 1
                        word = "".join([x1,x2,x3,x4,x5,x6])
                        # print(word)
                        # print(word)
                        if (word.count('Ь') <= 1 and word.count('А') == 1 and word.count('З') <= 2):
                            print("".join(word), k)
                            arr.append(k)
                            flag = True
    if flag:
        break
print(min(arr))
# import itertools
# alphabet = "0123456789"
# ar = itertools.permutations(alphabet, 6) #Размещение
# arl = []
# for e in ar:
#     arl.append(list(e))
# count = 0
# for e in arl:
#     flag = True
#     for i in range(len(e)-1):
#         if (e[0] == "0") or (int(e[i]) % 2 == 0 and int(e[i+1]) % 2 == 0) or (int(e[i]) % 2 != 0 and int(e[i+1]) % 2 != 0) or (e[5] != "5" and e[5] != "0"):
#             flag = False
#     if flag:
#         count += 1
# print(count)