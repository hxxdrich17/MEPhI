def count(s):
    arr = []
    ans = {}
    for i in range(len(s)):
        a = s[i]
        if (a not in arr):
            arr.append(a)
            cnt = s.count(a)
            ans[a] = cnt
    return ans



print(count("aba"))