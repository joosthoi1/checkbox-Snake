import time
from tkinter import *
import keyboard
from random import randint
from tkinter import messagebox
coordrost = {
'y1':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
'y2':[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
'y3':[41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60],
'y4':[61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
'y5':[81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
'y6':[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120],
'y7':[121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140],
'y8':[141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160],
'y9':[161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180],
'y10':[181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200],
'y11':[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220],
'y12':[221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240],
'y13':[241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260],
'y14':[261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280],
'y15':[281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300],
'y16':[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320],
'y17':[321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340],
'y18':[341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360],
'y19':[361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380],
'y20':[381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400]
}

isfruit = 0
fruit = 3
mylist2=[]
dir = 'Right'
def coords(x, y):
    y = 'y' + str(y)
    print(y, x-1)
    return coordrost[y][x-1]
x = 3
y = 1
def dead():
    messagebox.showinfo('Game Over', f'You died with a length of {fruit}')
    master.update()
    return

master = Tk()
a=0
b=0
mylist=[]
c = IntVar()
d = 0

def var_states1():
    global d

    global x
    global y
    global dir
    global fruit
    global isfruit
    global fruitplace
    fruit = 3
    x = 1
    y = 1
    while 1:
        print(d)

        try:
            if keyboard.is_pressed('up') or keyboard.is_pressed('w'):  # if key 'q' is pressed
                dir = 'Up'
            if keyboard.is_pressed('down') or keyboard.is_pressed('s'):  # if key 'q' is pressed
                dir = 'Down'
            if keyboard.is_pressed('left') or keyboard.is_pressed('a'):  # if key 'q' is pressed
                dir = 'Left'
            if keyboard.is_pressed('right') or keyboard.is_pressed('d'):  # if key 'q' is pressed
                dir = 'Right'
        except Exception as e:
            print(e)
            continue

        mylist[coords(x, y)-1].set(1)

        if d >= fruit:
            mylist2.insert(0, coords(x, y)-1)
            mylist[mylist2[-1]].set(0)
            mylist2.pop(-1)
            print(mylist2)

        else:
            mylist2.insert(0, coords(x, y)-1)
            print(mylist2)
            d += 1
        if x == 20 and dir == 'Right':
            dead()
            break
        if x == 0 and dir == 'Left':
            dead()
            break
        if y == 20 and dir == 'Down':
            dead()
            break
        if y == 1 and dir == 'Up':
            dead()
            break
        if dir == 'Up':
            y -= 1
        if dir == 'Down':
            y += 1
        if dir == 'Right':
            x += 1
        if dir == 'Left':
            x -= 1
        if isfruit == 0:
            randcoordsx = randint(1, 20)
            randcoordsy = randint(1, 20)
            if coords(randcoordsx, randcoordsy)-1 in mylist2:
                pass
            else:
                mylist[coords(randcoordsx, randcoordsy)-1].set(1)


                fruitplace = coords(randcoordsx, randcoordsy)-1
                isfruit = 1
        try:
            if mylist2[0] == fruitplace:
                fruit += 1
                isfruit = 0
            master.update()
            if mylist2[0] in mylist2[1:]:
                dead()
                break

        except Exception:
            pass
        time.sleep(0.125)
    master.destroy()

for i in range(1000):
    mylist.append('v' + str(i))
    mylist[i] = IntVar()
    print(mylist[i])
    Checkbutton(master, text="", variable=mylist[i]).grid(row=a, sticky=W, column=b)
    b +=1
    if b == 20:
        a += 1
        b = 0
    if a == 20:
        break
        master.update()


master.after(1, var_states1)
master.update()
master.mainloop()
print(mylist)
