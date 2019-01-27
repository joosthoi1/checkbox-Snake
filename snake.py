import time
from tkinter import *
import keyboard
from random import randint
from tkinter import messagebox
coordrost = {
'y1': [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],
'y2': [2, 12, 22, 32, 42, 52, 62, 72, 82, 92],
'y3': [3, 13, 23, 33, 43, 53, 63, 73, 83, 93],
'y4': [4, 14, 24, 34, 44, 54, 64, 74, 84, 94],
'y5': [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
'y6': [6, 16, 26, 36, 46, 56, 66, 76, 86, 96],
'y7': [7, 17, 27, 37, 47, 57, 67, 77, 87, 97],
'y8': [8, 18, 28, 38, 48, 58, 68, 78, 88, 98],
'y9': [9, 19, 29, 39, 49, 59, 69, 79, 89, 99],
'y10': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
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
        if x == 10 and dir == 'Right':
            x = 0
        if x == 0 and dir == 'Left':
            x = 10

        if y == 10 and dir == 'Down':
            y = 0
        if y == 1 and dir == 'Up':
            y = 11
        if dir == 'Up':
            y -= 1
        if dir == 'Down':
            y += 1
        if dir == 'Right':
            x += 1
        if dir == 'Left':
            x -= 1
        if isfruit == 0:
            randcoordsx = randint(1, 10)
            randcoordsy = randint(1, 10)
            if coords(randcoordsx, randcoordsy)-1 in mylist2:
                pass
            else:
                mylist[coords(randcoordsx, randcoordsy)-1].set(1)
                fruitplace = coords(randcoordsx, randcoordsy)-1
                isfruit = 1
        if mylist2[0] == fruitplace:
            fruit += 1
            isfruit = 0
        master.update()
        if mylist2[0] in mylist2[1:]:
            messagebox.showinfo('Game Over', 'You died, press Start to try again.')
            master.update()
            break
        time.sleep(0.15)


for i in range(1000):
    mylist.append('v' + str(i))
    mylist[i] = IntVar()
    print(mylist[i])
    Checkbutton(master, text="", variable=mylist[i]).grid(row=a, sticky=W, column=b)
    a +=1
    if a == 10:
        b += 1
        a = 0
    if b == 10:
        break
        master.update()

Button(master, text='Start', command=var_states1).grid(row=100, sticky=W, column=1000)

master.update()
master.mainloop()
print(mylist)
