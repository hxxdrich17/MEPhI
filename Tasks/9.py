char_eng = {
            1: ".,?!",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            "*": "'-+=",
            }
    
char_ru = {
            1: ".,?!",
            2: "абвг",
            3: "деёж",
            4: "зийк",
            5: "лмно",
            6: "прст",
            7: "уфхц",
            8: "чшщъ",
            9: "ыьэюя",
            "*": "'-+=",
            }

def send_message(message, lang="eng"):
    global char_eng, char_ru
    total = ""
    prvmsg = ""
    flag = False
    hashtag = False
    message = list(message)

    char = char_eng if (lang == "eng") else char_ru
    
    for i in range(len(message)):
        if (message[i].isupper()):
            total += "#"
            hashtag = True
            for x in range(1, 10):
                n = char.get(x)
                if (message[i].lower() in n):
                    if (str(x) == prvmsg and not hashtag):
                        total += " "
                    list(n)
                    v = n.index(message[i].lower()) + 1
                    for u in range(v):
                        total += str(x)
                    prvmsg = str(x)
                    flag, hashtag = True, True
                    break

        elif (message[i].islower()):
            if (flag):
                total += "#"
                flag = False
                hashtag = True
            for x in range(1, 10):
                n = char.get(x)
                if (message[i] in n):
                    if (str(x) == prvmsg and not hashtag):
                        total += " "
                    list(n)
                    v = n.index(message[i]) + 1
                    for u in range(v):
                        total += str(x)
                    prvmsg = str(x)
                    hashtag = False
                    break

        elif (message[i].isdigit()):
            total += message[i] + "-"

        elif (message[i] in ".,?!"):
            if (str(1) == prvmsg):
                        total += " "
            n = char.get(1)
            list(n)
            v = n.index(message[i]) + 1
            for u in range(v):
                total += str(1)
            prvmsg = str(1)

        elif (message[i] in "'-+="):
            if ("*" == prvmsg):
                        total += " "
            n = char.get("*")
            list(n)
            v = n.index(message[i]) + 1
            for u in range(v):
                total += "*"
            prvmsg = "*"

        elif (message[i] == " "):
            total += "0"

    # return total
    print(total)
    

def receive_message(message, lang="eng"):
    global char_eng, char_ru
    message = list(message)
    total, t, t1 = "", 0, 0
    flag, flag1, num = False, False, False

    char = char_eng if (lang == "eng") else char_ru

    for i in range(len(message) - 1):
        letter = message[t]
        try: 
            if (message[t + 1] == "-"): num = True
        except: continue
        if (letter == "#"): 
            if flag: flag = False
            else: flag = True
        elif (letter == "0"): total += " "
        elif (num):
            num = False
            total += letter
            t += 1
        elif (letter not in (" ", "0")):
            t1 = 0
            a = list(char.get(int(letter))) if (letter != "*") else list(char.get(letter))
            for i in range(len(a)):
                try:
                    if (letter != message[t + t1]):
                        break
                    t1 += 1
                except:
                    continue
            y = list(a)[t1 - 1]
            y = y.upper() if flag else y.lower()
            t += t1
            total += y
            flag1 = True
        if (not flag1): t += 1
        if (flag1): flag1 = False
        if (t >= len(message) - 1): break

    # return total
    print(total)


send_message("привет.ау", "ru")
receive_message("6 66442223366661277", "ru")

# -------------------------
# |   1   |   2   |   3   |  <-- hold a key to type a number
# |  .,?! |  abc  |  def  |  <-- press a key to type a letter
# -------------------------
# |   4   |   5   |   6   |  <-- Top row
# |  ghi  |  jkl  |  mno  |  <-- Bottom row
# -------------------------
# |   7   |   8   |   9   |
# |  pqrs |  tuv  |  wxyz |
# -------------------------
# |   *   |   0   |   #   |  <-- hold for *, 0 or #
# |  '-+= | space |  case |  <-- press # to switch between upper/lower case
# -------------------------

# -------------------------
# |   1   |   2   |   3   |  <-- hold a key to type a number
# |  .,?! |  абвг |  деёж |  <-- press a key to type a letter
# -------------------------
# |   4   |   5   |   6   |  <-- Top row
# |  зийк |  лмно |  прст |  <-- Bottom row
# -------------------------
# |   7   |   8   |   9   |
# |  уфхц |  чшщъ | ыьэюя |
# -------------------------
# |   *   |   0   |   #   |  <-- hold for *, 0 or #
# |  '-+= | space |  case |  <-- press # to switch between upper/lower case
# -------------------------