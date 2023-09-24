print("Y W Z X F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((not (w <= (not (x <= y)))) and ((not x) <= ((not y) == z))) == False:
                    if ([w,x,y,z].count(1) >= 3):
                        print(y,w,z,x, 0)
                if ((not (w <= (not (x <= y)))) and ((not x) <= ((not y) == z))) == True:
                    if ([w,x,y,z].count(0) >= 2):
                        print(y,w,z,x, 1)


                # - - - x
                    