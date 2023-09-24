x = float(input("x = "))
y = float(input("y = "))
R = 3

if x <= 3 and y <= 3 and x >= -3 and y >= 3:
    if (x**2 + y**2) < R**2:
        print ("Нет")
    else:
        print ("Да")
else:
    print ("Нет")

input('Press ENTER to exit')