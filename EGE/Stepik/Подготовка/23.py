def f(x, y):
    if x > y or x == 32:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

print(f(3, 15) * f(15, 50))





