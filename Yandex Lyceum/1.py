def passed(name):
    print(f'{name} passed ✅')

def wrong(name):
    print(f'{name} not passed ❌')


def test(num, res):
    if (res == 8934):
        passed(num)
    else:
        wrong(num)

arr = [1, 4, 23, 546, 1, 324, 8934, 109]

def first():
    test(1, max(arr))

first()

def second():
    x = arr[0]
    for i in arr:
        if (i > x):
            x = i
    test(2, x)

second()

def third():
    arr.sort(reverse=True)
    test(3, arr[0])

third()