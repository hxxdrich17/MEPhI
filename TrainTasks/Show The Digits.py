import itertools

def est_subsets(arr):
    n = 0
    arr = list(set(arr))
    for i in range(1, len(arr) + 1):
        arr1 = itertools.combinations(arr, i)
        n += len(list(arr1))
    return n


