import time
from tkinter import *
import keyboard
from random import randint
from tkinter import messagebox

coordrost={}
number = 40
starty = 1
while True:
    coordrost['y'+str(starty)] = []
    for i in range((starty-1)*number, number*starty):
        coordrost['y'+ str(starty)].append(i+1)
    starty +=1
    if starty == number + 1:
        break

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
master = Tk()
a=0
b=0
mylist=[]
c = IntVar()
d = 0

def var_states1():
    global d
    global number
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
            if keyboard.is_pressed('w'):  # if key 'q' is pressed
                dir = 'Up'
            if keyboard.is_pressed('s'):  # if key 'q' is pressed
                dir = 'Down'
            if keyboard.is_pressed('a'):  # if key 'q' is pressed
                dir = 'Left'
            if keyboard.is_pressed('d'):  # if key 'q' is pressed
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
        if x == number and dir == 'Right':
            x = 0
        if x == 0 and dir == 'Left':
            x = number

        if y == number and dir == 'Down':
            y = 0
        if y == 1 and dir == 'Up':
            y = number+1
        if dir == 'Up':
            y -= 1
        if dir == 'Down':
            y += 1
        if dir == 'Right':
            x += 1
        if dir == 'Left':
            x -= 1
        if isfruit == 0:
            randcoordsx = randint(1, number)
            randcoordsy = randint(1, number)
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
                messagebox.showinfo('Game Over', f'You died with a length of {fruit}')
                master.update()
                break
        except Exception:
            pass
        time.sleep(0.125)
    master.destroy()

for i in range(10000):
    mylist.append('v' + str(i))
    mylist[i] = IntVar()
    print(mylist[i])
    Checkbutton(master, text="", variable=mylist[i]).grid(row=a, sticky=W, column=b)
    b +=1
    if b == number:
        a += 1
        b = 0
    if a == number:
        break
        master.update()

Button(master, text='Start', command=var_states1).grid(row=100, sticky=W, column=1000)

master.update()
master.mainloop()
print(mylist)
