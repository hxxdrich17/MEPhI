maxi = 0 
for i in range(123456789, 223456790):
    sqrti = i**0.5
    numdel = 0
    if round(sqrti) == sqrti:
        maxdel = 1
        for j in range(2, round(sqrti) - 1):
            if i % j == 0:
                if maxdel == 1: maxdel = i // j
                numdel += 2
        if numdel == 2: print(i, maxdel)