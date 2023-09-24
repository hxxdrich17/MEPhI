import sys # для установки лимита рекурсии
sys.setrecursionlimit(2000)

def m1(h): # Для одной кучи
    return h*2, h+1

def m2(a, b): # Для двух куч
    a,b = h
    return (a*2,b), (a,b*2), (a+1,b), (a,b+1)

from functools import * # обязательно!
@lru_cache(None) # тоже!

# Одна куча

def g_1(h):
    if h >= 129: return 'WIN'
    if any(g_1(i) == 'WIN' for i in m1(h)): return 'P1' # if g_1(h * 2) == 'WIN' or g_1(h + 1) == 'WIN'
    if all(g_1(i) == 'P1' for i in m1(h)): return 'V1' # if g_1(h * 2) == 'P1' and g_1(h + 1) == 'P1'
    if any(g_1(i) == 'V1' for i in m1(h)): return 'P2' # if g_1(h * 2) == 'V1' or g_1(h + 1) == 'V1'
    if all(g_1(i) == 'P1' or g_1(i) == 'P2' for i in m1(h)): return 'V2' #if (g_1(h * 2) == 'P2' or g_1(h + 1) == 'P2') and (g_1(h * 2) == 'P1' or g_1(h + 1) == 'P1')

# Две кучи
def g_2(h):
    a,b = h
    if a + b >= 129: return 'WIN'
    if any(g_1(i) == 'WIN' for i in m2(h)): return 'P1' # if g_1(h * 2) == 'WIN' or g_1(h + 1) == 'WIN'
    if all(g_1(i) == 'P1' for i in m2(h)): return 'V1' # if g_1(h * 2) == 'P1' and g_1(h + 1) == 'P1'
    if any(g_1(i) == 'V1' for i in m2(h)): return 'P2' # if g_1(h * 2) == 'V1' or g_1(h + 1) == 'V1'
    if all(g_1(i) == 'P1' or g_1(i) == 'P2' for i in m2(h)): return 'V2' #if (g_1(h * 2) == 'P2' or g_1(h + 1) == 'P2') and (g_1(h * 2) == 'P1' or g_1(h + 1) == 'P1')



for i in range(1 , 140):
    h = 17, i # Для двух куч
    res = g_2(h) # Для двух куч
    res = g(i) # Для одной кучи
    # if res == 'V1':
    #     print(i, res)
    # if res == 'P2':
    #     print(i, res)
    # if res == 'V2':
    #     print(i, res)
    if (res != None and res != "WIN" and res != "P1"):
        print(i ,res)

