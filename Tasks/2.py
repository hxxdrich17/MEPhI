a = "4 3 4 4 3 5 3 3 3 5 5 4 3 4"
b = "5 5"
a = [int(i) for i in a.split(" ")]
b = [int(i) for i in b.split(" ")]
print((sum(a) + sum(b)) / (len(a) + len(b)))