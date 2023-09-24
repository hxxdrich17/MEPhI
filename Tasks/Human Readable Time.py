def make_readable(seconds):
    m = seconds // 60
    s = seconds % 60
    h = m // 60
    m = m % 60
    if (len(str(h)) == 1):
        h = "0" + str(h)
    if (len(str(m)) == 1):
        m = "0" + str(m)
    if (len(str(s)) == 1):
        s = "0" + str(s)
    return f"{h}:{m}:{s}"



print(make_readable(60))
print(make_readable(0))