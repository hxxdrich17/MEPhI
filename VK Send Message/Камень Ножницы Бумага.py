import random

possible = ["камень", "ножницы", "бумага"]
knb = ""
f = False

print("Для остановки напиши: стоп")

while (knb != "стоп"):
    while (knb != "камень" or knb != "ножницы" or knb != "бумага"):
        print("Выбери: камень, ножнницы или бумага")
        knb = input()
        k1 = list(knb)
        if (k1[-1] == " "):
            god = True
            k1.remove(" ")
            knb = "".join(k1)
        else:
            god = False
        if (knb == "камень" or knb == "ножницы" or knb == "бумага"):
            break
        elif (knb == "стоп"):
            f = True
            break
        
    if (f):
        break

    if (not god):
        x = random.randint(0, 2)
        x = possible[x]
        if (knb == "камень" and x == "ножницы" or knb == "ножницы" and x == "бумага" or knb == "бумага" and x == "камень"):
            flag = True
        elif (knb == x):
            print(f"PLAYER | {knb} vs. {x} | PC")
            print("Ничья!")
            flag = 2
        else:
            flag = False
        if (flag != 2):
            print(f"PLAYER | {knb} vs. {x} | PC")
            if (flag):
                print("Игрок одержал победу!")
            else:
                print("Компьютер одержал победу!")

    elif (god):
        if (knb == "камень"):
            x = "ножницы"
        elif (knb == "ножницы"):
            x = "бумага"
        else:
            x = "камень"
        print(f"PLAYER | {knb} vs. {x} | PC")
        print("Игрок одержал победу!")