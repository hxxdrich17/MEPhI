from math import sqrt

class Sudoku(object):
    def __init__(self, data):
        self.data = data
        pass
    def is_valid(self):
        arr = []
        data = self.data

        flag = True
        t = False
        # 1 point
        if (sqrt(len(data)).is_integer() != True or len(data) <= 0):
            flag = False
            # print(1.1)
            return False
        for i in range(len(data)):
            if (len(data) != len(data[i])):
                flag = False
                # print(1.2)
                return False
        # 2 point
        for x in range(len(data)):
            for y in range(len(data[x])):
                if (isinstance(data[x][y], float)):
                    flag = False
                    # print(2.1)
                    return False
                arr.append(data[x][y])
            arr.sort()
            # print(arr)
            for i in range(len(data)):
                if (i + 1 != arr[i]):
                    flag = False
                    # print(2.3)
                    return False
            arr = []
            if (len(data) not in data[x] or len(data) < max(data[x])):
                flag = False
                # print(2.2)
                return False
        # 3 point
        for x in range(len(data)):
            for y in range(len(data)):
                if (isinstance(data[y][x], float) or len(data) < data[y][x]):
                    flag = False
                    # print(3.1)
                    return False
                if (len(data) == data[y][x]):
                    t = True
                arr.append(data[y][x])
            arr.sort()
            for i in range(len(data)):
                if (i + 1 != arr[i]):
                    flag = False
                    # print(3.3)
                    return False
            arr = []
        if (flag):
            if (not t):
                flag == False
                # print(3.2)
                return False
        return flag








# Valid Sudoku
goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],  
  [1]
])

print(goodSudoku1.is_valid())
print(goodSudoku2.is_valid())
print(badSudoku1.is_valid())
print(badSudoku2.is_valid())