x,y = int(input()), int(input())
z = 2 * (x+y)
arr = [str(i)[0] for i in [x,y,z]]

for i in range(3):
    print(f"{arr[i]}:   {oct(ord(arr[i]))[2:]}   {ord(arr[i])}   {hex(ord(arr[i]))[2:]}")