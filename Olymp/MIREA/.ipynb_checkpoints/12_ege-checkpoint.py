a = "8" * 247

while ('888' in a or '111' in a):
    if ('888' in a):
        a = a.replace('888', '1', 1)
    else:
        a = a.replace('111', '8', 1)

print(a)