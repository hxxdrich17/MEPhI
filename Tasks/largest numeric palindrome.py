def numeric_palindrome(*args):
    multy = []
    nums = {}
    needful = []
    total = []
    k = 0
    for x in range(len(args) - 1):
        for y in range(x + 1, len(args)):
            multy.append(args[x] * args[y])
    
    for i in range(len(multy)):
        x = list(str(multy[i]))
        for z in range(10):
            nums[z] = x.count(str(z))
            if (nums.get(z) % 2 == 0 and nums.get(z) != 0):
                needful.append(str((nums.get(z) * z) // 2))
            else:
                if (nums.get(z) != 0):
                    k = z
        needful.sort(reverse=True)
        total += needful
        total.append(str(k))
        needful.sort()
        total += needful
        return int("".join(total))



















        #     if (nums.get(z) % 2 == 0 and nums.get(z) != 0):
        #         needful.append(str(z) * (nums.get(z) // 2))
        #     else:
        #         if (nums.get(z) > k):
        #             k = nums.get(z)
        # print(k)
        # needful.sort(reverse=True)
        # total1 = needful
        # total1.append(str(k))
        # needful.sort()
        # print(needful)
        # total1.append(needful)
        # print(total1)
        # # print("".join(total1))

        # x.sort(reverse=True)
        # print(x)




# print(numeric_palindrome(48,9,3,67))
print(numeric_palindrome(937,113)) # 105881  81518