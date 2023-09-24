def dirReduc(arr):
    for i in range(len(arr)):
        if ("NORTH" in arr and "SOUTH" in arr):
                arr.remove("NORTH")
                arr.remove("SOUTH")
        elif ("WEST" in arr and "EAST" in arr):
                arr.remove("EAST")
                arr.remove("WEST")
    return arr







print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))