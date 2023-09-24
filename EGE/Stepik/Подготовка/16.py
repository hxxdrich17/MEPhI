def F(x):
    if (x == 1):
        return 1
    if x > 1:
        return F(x - 1) * x

print(F(5))





