def pick_peaks(arr):
    local_max = []
    for i in range(1, len(arr) - 1):
        if (arr[i-1] < arr[i] >= arr[i+1]):
            if (arr[i] == arr[i + 1]):
                for x in range(len(arr[i:]) - 1):
                    if (arr[i+x] < arr[i+x+1]): break
                    elif (arr[i+x] > arr[i+x+1]):
                        local_max.append([i, arr[i]])
                        break
            else:
                local_max.append([i, arr[i]])
                
    dict = {"pos": [],
            "peaks": []}
    for i in local_max:
        dict["pos"].append(i[0])
        dict["peaks"].append(i[1])
    return dict



def diagram(arr, local_max):
    matrix = [ [" " for i in range(len(arr))] for i in range(max(arr)) ]
    
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (arr[y] - 1 == x and y in local_max["pos"]): matrix[x][y] = "●"
            elif (arr[y] > x): matrix[x][y] = "|"
            
    matrix.reverse()
    matrix = ["".join(matrix[i]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        print(f"{len(matrix) - i}|  {matrix[i]}")
    print("—" * len(matrix) * 5)
    
    

x = pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])
diagram([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3], x)
print(x)
