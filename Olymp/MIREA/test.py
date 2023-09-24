arr = []



for x in range(0, 10):
    for y in range(100):
        y1 = str(y)
        if (len(str(y)) == 1):
            y1 = "0" + str(y)
        # if (len(str(y)) == 2):
        #     y1 = "0" + str(y)
        ans = int("1" + str(x) + "234" + y1 + "6")
        print(ans)
        if (ans % 149 == 0 and ans <= 10**8):
            arr.append(ans)
        ans = int("1" + str(x) + "234" + "6")
        if (ans not in arr and ans % 149 == 0):
            arr.append(ans)
        y1 = str(y)
        ans = int("1" + str(x) + "234" + y1 + "6")
        if (ans not in arr and ans % 149 == 0 and ans <= 10**8):
            arr.append(ans)

for i in range(len(arr)):
    print(arr[i], arr[i] // 149)

