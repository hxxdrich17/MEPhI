"""
    STRUCTURE OF .txt FILE:
        {name_of_author}
        {name}

        {quatrain_1}

        {quatrain_2}

        {quatrain_n}
    ALL SPACES ARE REQUIRED!
"""

def Cent(*a, spec=False):
    if (spec):
        a = " ".join(a)
        a = a.center(len(a)+60)
    else:
        a = " ".join(a)
        a = a.center(len(a)+120)
    return a

def Start():
    print(Cent("\033[37m"))
    print(Cent("\033[32m{}".format("Начало")))
    print(Cent("\033[36m{}".format("Автор:"), name_of_author))
    print(Cent("\033[36m{}".format("Название:"), name))
    print(Cent(f"Количество строк: {(len(f) - (len(f) // 4)) + 2} | Количество четверостиший: {len(f) // 4 - 1}"))
    print(Cent("\033[37m"))


f = open("C:/Users/hxxdrich17/Documents/Code/Python/ЕГЭ/Stepik/text.txt", "r", encoding="UTF-8")
f = f.readlines()
name_of_author = f[0].split("\n")[0]
name = f[1].split("\n")[0]
f = f[3:]
f1 = [i.split("\n")[0] for i in f]
f = []
alp = " абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alpC = alp.upper()
for v in range(len(f1)):
    g = f1[v]
    if ("-" in g): g = g.replace("-", " ")
    if ("…" in g): g = g.replace("…", " ")
    g = g.strip()
    g = [m.lower() for m in g if m in alp or m in alpC]
    l = 0
    while l <= len(g) - 2:
        if (g[l] == " " and g[l + 1] == " "):
            g.pop(l + 1)
        else:
            l += 1
    f.append("".join(g))
i = 0
flag = False
Start()

while (True):
    a = input(Cent("", spec=True)).lower()
    try:
        if (f[i] == ""):
            i += 1
        if ((a == f1[i].lower() or a == f[i]) and (a.split()[0] != "с" and a != "к" and a != "п" and a.split()[0] != "ч" and a != "e" and a != "т")):
            print(Cent("\u2705\033[37m{}".format("")))
            i += 1
            flag = False
        elif ((a != f1[i].lower() or a != f[i]) and (a.split()[0] != "с" and a != "к" and a != "п" and a.split()[0] != "ч" and a != "e" and a != "т")):
            print(Cent("\u274c\033[37m{}".format("")))    
        elif (a == "к"  or a == "e"):
            break
        elif (a.split()[0] == "с"):
            x = (int(a.split()[1]) - 1) // 4
            i = int(a.split()[1]) - 1 + x
            flag = True
        elif (a.split()[0] == "ч"):
            i = (int(a.split()[1]) * 4) + ((int(a.split()[1]) - 5))
            flag = True
        elif (a == "п"):
            print(Cent("\033[37m{}".format("-" * len(f1[i]))))
            print(Cent("\033[1m\033[33m{}".format(f1[i])))
            print(Cent("\033[37m{}".format("-" * len(f1[i]))))
            flag = True
        elif (a == "т"):
            print(Cent("\033[1m\033[33m"))
            print(Cent("\033[37m{}".format("-" * len(max(f1)))))
            for z in range(len(f)):
                print(Cent("\033[1m\033[33m{}".format(f1[z])))
            print(Cent("\033[37m{}".format("-" * len(max(f1)))))
        if (i >= len(f) and not flag):
            print(Cent("\033[32m{}".format("Конец")))
            print(Cent("\033[37m"))
            a = input()
            if (a == ""):
                i = 0
                Start()
            else:
                break
        # flag = False
    except:
        print(Cent("\033[37m"))
        print(Cent("\033[31m{}".format("Ошибка")))
        print(Cent("\033[37m"))