# l,r = int(input()), int(input())


# # ans = len(str(l)) + len(str(r))
# # if (l == r):
# #     print(len(str(l)))
# #     quit()

# # for i in range(len(str(r - l)) + 1):
# #     if (len(str(10**i)) <= len(str(r - l))+1):
# #         # x = ((10**(len(str(l + 1))) - 10**(len(str(l+1))-1)) - l1) * len(str(l + 1))
# #         x = (((10**(i) - 10**(i-1)) - 1) * len(str(i)))
# #         ans += len(str(x))
# #     else:
# #         break


# # print(ans)
# ans = len(str(l)) + len(str(r))
# for i in range(len(str(r - l))):

L = int(input())
R = int(input()) + 1
sum = 0
while L != R:
    I = L
    r = R
    while I + 1 != r:
        m = (I + r) // 2
        if len(str(L)) == len(str(m)):
            I = m
        else:
            r = m
    sum += (r - L) * len(str(L))
    L = r
print(sum)