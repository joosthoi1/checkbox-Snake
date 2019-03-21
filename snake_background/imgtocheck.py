from gridcreation_class import grid
import cv2, keyboard, time
from random import randint
from tkinter import messagebox
image=cv2.imread('unknown.png')
y=image.shape[0] #length in first dimension
x=image.shape[1]
maxx, maxy = 69, 41
def downscale(x, y):
    newx,newy =x,y
    while 1:
        if (int(newx) <= maxx and newy < maxy):

            return int(newx), newy
        newy-=1
        newx-=x/y


def colorin():
    x, y =1,1
    for i in grid1.mylist:
        mycolor = '#%02x%02x%02x' % (resized[y-1][x-1][2], resized[y-1][x-1][1], resized[y-1][x-1][0])
        grid1.mylist[grid1.coords(x, grid1.numbery-(y-1))].configure(bg=mycolor,fg=mycolor)
        grid1.mylist[grid1.coords(x, grid1.numbery-(y-1))].configure(state='disabled')
        #grid1.mylist[grid1.coords(x, grid1.numbery-y)].select()
        x+=1
        if x == newx:
            y+=1
            x=1
        if y == newy:
            break
newx, newy = downscale(x,y)
resized = cv2.resize(image,(newx,newy))
grid1 = grid(newx-1, newy-1)
grid1.master.title('art')
master = grid1.master

def reload():
    for i in grid1.mylist:
        i.deselect()

    var_states1()
def dead(bodylength):
    messagebox1 = messagebox.askquestion('Game Over', f'You died with a length of {bodylength}\nWould you like to play again?')
    if messagebox1 == 'yes':
        reload()
    else:
        master.destroy()

def var_states1():
    y, x = int(grid1.numbery/2), 1
    bodylength = 3
    dir = 'Right'
    fruitneeded = False
    snake_body = []
    tick = 0
    needfruit = True
    while 1:
        if (keyboard.is_pressed('w') or keyboard.is_pressed('up')) and dir != 'Down':  # if key 'q' is pressed
            dir = 'Up'
        elif (keyboard.is_pressed('s') or keyboard.is_pressed('down')) and dir != 'Up':  # if key 'q' is pressed
            dir = 'Down'
        elif (keyboard.is_pressed('a') or keyboard.is_pressed('left')) and dir != 'Right':  # if key 'q' is pressed
            dir = 'Left'
        elif (keyboard.is_pressed('d') or keyboard.is_pressed('right')) and dir != 'Left':  # if key 'q' is pressed
            dir = 'Right'

        if tick == 1:


            if needfruit:
                while 1:
                    randcoordsx, randcoordsy = randint(1, grid1.numberx), randint(1, grid1.numbery)
                    if grid1.coords(randcoordsx,randcoordsy) in snake_body:
                        pass
                    else:
                        fruitplace = grid1.coords(randcoordsx,randcoordsy)
                        grid1.mylist[grid1.coords(randcoordsx,randcoordsy)].select()
                        grid1.mylist[grid1.coords(randcoordsx,randcoordsy)].configure(disabledforeground='red')
                        needfruit = False
                        break
            tick = 0

            grid1.mylist[grid1.coords(x, y)].select()
            grid1.mylist[grid1.coords(x, y)].configure(disabledforeground='green')
            if len(snake_body) >= bodylength:
                snake_body.insert(0, grid1.coords(x, y))
                grid1.mylist[snake_body[-1]].deselect()
                grid1.mylist[snake_body[-1]].configure(disabledforeground='black')
                snake_body.pop(-1)
            else:
                snake_body.insert(0, grid1.coords(x, y))
            if snake_body[0] == fruitplace:
                bodylength += 1
                needfruit = True
            if dir == 'Right':
                x+=1
            if dir == 'Left':
                x-=1
            if dir == 'Up':
                y+=1
            if dir == 'Down':
                y-=1

            if x == grid1.numberx+1 and dir == 'Right':
                x= 1
            if x == 0 and dir == 'Left':
                x= grid1.numberx
            if y == grid1.numbery+1 and dir == 'Up':
                y = 1
            if y == 0 and dir == 'Down':
                y = grid1.numbery
            if snake_body[0] in snake_body[1:]:
                dead(bodylength)

        tick += 1
        try:
            master.update()
        except Exception:
            pass
        time.sleep(0.077)
master.after(2,colorin)
master.after(2,var_states1)
master.mainloop()
