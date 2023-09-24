def smaller(arr):
    return [len([x for x in arr[i:] if x < arr[i]]) for i in range(0, len(arr))]


   # data = []
    # for x in range(len(arr)):
    #     z = arr[x]
    #     dt = arr[x + 1:]
    #     t = 0
    #     for y in range(len(dt)):
    #         if (z > dt[y]):
    #             t += 1
    #     data.append(t)
    # return data

print(smaller([5, 4, 3, 2, 1]))