def square_sums(num):
    ans,ans1,ans2,arr = [],[],[],[]
    count = []
    ones = []
    pos = []
    x,y,z,k = 0,0,0,1
    flag1, flag = False, True
    pos_nums = [i for i in range(1, num + 1)]
    dic = {}

    for i in range(num):
        dic[pos_nums[i]] = []
        for o in range(num):
            if (((pos_nums[i] + pos_nums[o]) ** 0.5).is_integer() and pos_nums[i] != pos_nums[o]):
                dic[pos_nums[i]].append(pos_nums[o])
        count.append(len(dic.get(pos_nums[i])))

    for i in range(1, num + 1):
        x = dic.get(i)
        if (x == []):
            return False

    for i in range(1, num + 1):
        x = dic.get(i)
        if (len(x) == 1):
            ans.append(i)
            ans.append(x[0])
            k = x[0]

    if (ans != []):
        flag1 = True

    for i in range(1, num + 1):
        if (flag1):
            x = dic.get(k)
            for o in range(len(x)):
                count[x[o]] = len(dic.get(x[o]))
                # print(count[x[o]])




                # for p in range(x2):
                #     if (x2[p] not in ans):
                #         ans.append(x[p])
                #         k = x[o]
                #         break
                # x1.pop(min(x1))

                



    mn = count.index(min(count)) + 1
    x = dic.get(mn)

    if (len(x) == 1):
        ones.append(mn)
        if (flag): 
            ans.append(mn)
            ans.append(x[0])
            k = x[0]
    

    for i in range(1, num + 1):
        if (ans != []):
            for o in range(len(dic.get(k))):
                pos.append(len(dic.get(dic.get(k)[o])))
            for o in range(len(dic.get(k))):
                x = pos.index(min(pos))
                x = dic.get(dic.get(k)[x])
                print(x)




        if (len(x) == 1): ones.append(mn)
        if (len(ones) > 2): return False




        count.pop(count.index(min(count)))






    
    return ans






x = square_sums(15)
# for i in range(1, len(x) + 1):
#     print(f"{i}: {x.get(i)}")
print(x)