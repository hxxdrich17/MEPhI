num = input()
nums = ['2','3','4','5','2-','3-','4-','5-']
ots = []
for i in range(len(num)):
    if (num[i] in nums and i != len(num) - 1):
        if (num[i] + num[i+1] in nums):
            ots.append(float(float(num[i]) - 0.5))
        if (num[i] in nums and num[i] + num[i+1] not in nums):
            ots.append(int(num[i]))
    else:
        if (num[i] in nums):
            ots.append(int(num[i]))
    
print(ots)

print(sum(ots) / len(ots))



# 5 5 5 5
# 5 5 5 5 5- 5-

# 5 5 5 5 4.5 4.5

# 4.83

# a = input().split(" ") ots.append(float(float(num[i][0]) - 0.5))
# a = [float(i) for i in a]
# print(sum(a)/len(a))