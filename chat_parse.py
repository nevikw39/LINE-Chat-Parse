from time import *
from parse import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

y = 0
m = 0
d = 0
h = 0
mi = 0
t = dict()
n = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
     13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0}
root = tk.Tk()
root.withdraw()
try:
    l = open("chat_parse.log", 'r', encoding='UTF-8')
    s = l.readline()
    l.close()
    f = open(s, 'r', encoding='UTF-8-sig')
except:
    try:
        s = filedialog.askopenfilename()
        l = open("chat_parse.log", 'w', encoding='UTF-8')
        l.writelines(s)
        l.close()
        f = open(s, 'r', encoding='UTF-8-sig')
    except:
        exit(1)
f = open("Chat history in -109-.txt", 'r', encoding='UTF-8-sig')
print("讀入聊天紀錄：" + parse('Chat history in "{}"', f.readline())[0])
print("   訖  自   ：" + parse('Saved on: {}', f.readline())[0])
f.readline()
for line in f.readlines():
    try:
        (y, m, d, w) = parse("{:d}/{:d}/{:d}({})", line)
        if not y in t:
            t[y] = {}
            t[y][m] = {}
            t[y][m][d] = {}
        elif not m in t[y]:
            t[y][m] = {}
            t[y][m][d] = {}
        elif not d in t[y][m]:
            t[y][m][d] = {}
        print('\n%s ' % line.splitlines()[0], end="")
    except:
        print('.', end="")
        try:
            (h, mi, s) = parse("{:d}:{:d}\t{}", line)
            if not h in t[y][m][d]:
                t[y][m][d][h] = {}
                t[y][m][d][h][mi] = []
            elif not mi in t[y][m][d][h]:
                t[y][m][d][h][mi] = []
        except:
            "TypeError"
        finally:
            t[y][m][d][h][mi].append(str)
            n[h] += 1
print("\n處理完畢。\n以下是各小時訊息量比率：")
tk.messagebox.showinfo(title='結果', message=str(n))
for i in n:
    print("%2d " % i, end="")
    for j in range(n[i]):
        print('*', end="")
    print("")