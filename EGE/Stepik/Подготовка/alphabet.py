import itertools as it 
alp = "ДЕМЬЯН"
glas = "ЕЯ"
perm = it.permutations(alp)
words = []
for i in perm:
    words.append(list(i))

res = 0
for x in range(len(words)):
    flag = True
    for y in range(5):
        if (words[x][y] in glas
        and words[x][y+1] == "Ь"
        or words[x][0] == "Ь"):
            flag = False
    if (flag): res += 1

print(res, len(words))



