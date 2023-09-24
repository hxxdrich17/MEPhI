import sys
import json
import yaml
from todoist_api_python.api import TodoistAPI
from colorama import Fore, Back, Style
from termcolor import colored, cprint

api = TodoistAPI("8edab8a380105ed826cacbf0e7eb0b7d62344310")
projectID = '2257609561'
labels = ["Вебинары", "Школа", "Дополнительно"]
colors = ["light_red", "light_blue", "light_yellow", "light_grey", "light_magenta", "light_green", "light_cyan"]

# try:
#     projects = api.get_projects()
#     print(projects)
# except Exception as error:
#     print(error)
for l in labels:
    try:
        tasks = api.get_tasks(label=l)
        # cprint(tasks[0], "blue")
    except Exception as error:
        print(error)

    if (l == "Вебинары"):
        cprint("\n• Вебинары:", colors[1])
        mainc = colors[1]
    elif (l == "Школа"):
        cprint("\n• Школа:", colors[0])
        mainc = colors[0]
    else:
        cprint("\n• Дополнительно:", colors[2])
        mainc = colors[2]

    for i in range(len(tasks)):
        task = str(tasks[i])[5:-1].split(",")
        dict = {}
        arr = ["\n    ⭕"]
        date, content, priority, description, is_completed, string = "","","","","",""
        for t in range(len(task)):
            a = task[t].strip()
            a = a.split("=")
            # print(a)
            dict[a[0]] = a[1]

        try:
            date = dict.get("string")[1:-1]
        except:
            pass
        try:
            content = dict.get("content")[1:-1]
        except:
            pass
        try:
            priority = dict.get("priority")
        except:
            pass
        try:
            description = dict.get("description")[1:-1]
        except:
            pass
        try:
            is_completed = dict.get("is_completed")
        except:
            pass
        if (date != "" and date != None):
            arr.append(colored(f" [{date}]", colors[-1]))
            arr.append(colored(" ➞", colors[3]))
        if (content != "" and content != None):
            xcon = "".join(arr) + content
            if (len(xcon) > 66):
                p = 50
                v = 50
                while True:
                    v += 1
                    p += 1
                    if (p == 65):
                        content = content[:v-1-22] + "\n                  " + content[v-1-22:].strip()
                        v += 20
                        p = 0
                        if (len(content[v:]) < 66):
                            break
            arr.append(colored(f" {content}", mainc))
        if (priority != "" and priority != None and priority != "4"):
            priority = "!" * int(priority)
            if (len(priority) == 3):
                pcol = colors[5]
                priority = "!"
            elif (len(priority) == 2):
                pcol = colors[2]
                priority = "!!"
            else:
                pcol = colors[0]
                priority = "!!!"
            arr.append(colored(f" {priority}", pcol))
        if (description != "" and description != None):
            if ("\n\n" in description):
                description = description.replace("\n\n", " \n ")
            description = "| " + description
            if (len(description) > 61):
                p = 59
                v = 59
                # for i in range(len(description)):
                while True:
                    v += 1
                    p += 1
                    if (p == 60):
                        description = description[:v-1] + "\n       | " + description[v-1:].strip()
                        v += 7
                        p = 0
                        if (len(description[v:]) < 61):
                            break
                    
            arr.append(colored(f"\n       {description}", colors[3]))



        for z in arr:
            string += z
        print(string)
        # print(len("    ⭕ [21 февр. 2024] ➞ История: послушать послание президента выд"))
        
        
    # 43 | 67

