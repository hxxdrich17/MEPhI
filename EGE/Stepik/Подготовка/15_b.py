x = float(input("x = "))
y = float(input("y = "))
R = 3
L = 2

if (x**2 + y**2) <= R**2:
    if x <= 0 and y >= 0:
        if (x**2 + y**2) <= R**2 and (x**2 + y**2) >= L**2:
            print ("Да")
        else:
            print ("Нет")  
    elif x >= 0 and y <= 0:
        if (x**2 + y**2) <= L**2:
            print ("Да")
        else:
            print ("Нет") 
    else:
        print ("Нет")

else:
    print ("Нет")
input('Press ENTER to exit')
