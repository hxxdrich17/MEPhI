num, start_notation, end_notation = list(input()), int(input()), int(input())
symbols = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
fracstional_num = False
total_sum, n = 0, 0


# to 10-th notation

if ("," in num):

    fracstional_num = True
    comma_index = num.index(",")
    arr_num = num[:comma_index]
    arr_frac = num[comma_index + 1:]

    for i in range(len(num[:comma_index]) - 1, -1, -1):
        total_sum += symbols.index(arr_num[i]) * (start_notation ** n)
        n += 1

    n = -len(num[comma_index:]) + 1

    for i in range(-1, -len(num[comma_index:]), -1):
        total_sum += symbols.index(arr_frac[i]) * (start_notation ** n)
        n += 1
else:

    n = len(num) - 1

    for i in range(len(num)):
        total_sum += (symbols.index(num[i]) * (start_notation ** n))
        n -= 1
    

# to end-th notation

ints = []
int_num = int(str(total_sum).split(".")[0])
frac_num = float("0." + str(total_sum).split(".")[1])

while True:

    ints.append(str(symbols[int_num % end_notation]))
    int_num = int_num // end_notation

    if (int_num < end_notation):

        ints.append(str(symbols[int_num]))
        break

ints.reverse()

if (fracstional_num):

    fracs = []

    for i in range(4):

        fracs.append(str(symbols[int(frac_num * end_notation)]))
        frac_num = float("0." + str(float(frac_num * end_notation)).split(".")[1])

    print("".join(ints) + "," + "".join(fracs[:4]))

else:

    print("".join(ints))