def knight(p1, p2):
    num = [0,1,2,3,4,5,6,7,8] # 1 == index(1)
    let = list("-abcdefgh")   # 1 == index(a)
    spos = list(p1)
    epos = list(p2)







#                a  b  c  d  e  f  g  h   
#             8 [*][~][*][~][*][$][*][~] 8      * - white
#             7 [~][*][~][*][~][*][~][*] 7      ~ - black
#             6 [*][~][*][~][*][~][*][~] 6
#             5 [~][*][~][*][~][*][~][*] 5
#             4 [*][~][*][~][*][~][*][~] 4
#             3 [~][*][~][*][~][*][~][*] 3
#             2 [*][@][*][~][*][~][*][~] 2
#             1 [~][*][~][*][~][*][~][*] 1
#                a  b  c  d  e  f  g  h


arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
for i in arr:
    print(f"ANS: {knight(arr[i][0], arr[i][1])} | EXP: {arr[i][2]}")