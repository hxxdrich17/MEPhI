from functools import reduce
import copy

arr = [i for i in range(1, 11)]

x = lambda x, y: x * y
print(x(2, 5))

arr = list(map(str, arr))
print(arr)

# arr = list(map(int, arr))
arr = list(map(lambda x: int(x) * int(x), arr))
print(arr)

vol = reduce(lambda x, y: x * y, arr)
print(vol)

names = ["Гоша", "Аня", "Маша", "Катя", "Анастасия"]
names = list(filter(lambda x: x.startswith("А"), names))
print(names)

# copy of arr
num = [[ [1, [123, 3475, ["satd", "ufgasy", 1374, [True, "123"]]]], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]]
numc = num
numc.append(10)
print(num, numc)

numc = num[:] # только поверхностное копирование. с вложенными массивами могут возникнуть проблемы. то же самое что numc = copy.copy(num)
numc.append(20)
print(num, numc)

numc = copy.deepcopy(num) # полное копирование с вложенными массивами. лучше использовать.


# reverse arr
print(num, num[::-1])

# if
name = "asd"
if (name == "asd" or name == "qwe" or name == "zxc"): # не стоит
    pass
if (name in ("asd", "qwe", "zxc")): # лучше использовать
    pass

a = b = c = e = d = True
if (all((a, b, c, e, d))): print("All True") # Все истинно
if (any((a, b, c, e, d))): print("Sth is True") # Что-либо из этого истинно

local = "True" if a else "False"
print(local)

# func in dict
x = lambda name: name * 2
y = lambda name: name * 3
dic = {
    "first": x,
    "second": y,
}
print(dic["first"]("Gosha"))
print(dic["second"]("Ksysha"))