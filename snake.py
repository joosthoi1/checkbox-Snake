import sys, keyboard, time
from random import randint
from tkinter import messagebox
sys.path.append(sys.path[0]+'\\..')
from gridcreation_class import grid
grid1 = grid(20, 20)
master = grid1.master

def reload():
    for i in grid1.mylist:
        i.deselect()
        i.configure(bg='light gray')

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

        print(tick)

        if tick == 1:


            if needfruit:
                while 1:
                    randcoordsx, randcoordsy = randint(1, grid1.numberx), randint(1, grid1.numbery)
                    if grid1.coords(randcoordsx,randcoordsy) in snake_body:
                        pass
                    else:
                        fruitplace = grid1.coords(randcoordsx,randcoordsy)
                        grid1.mylist[grid1.coords(randcoordsx,randcoordsy)].select()
                        grid1.mylist[grid1.coords(randcoordsx,randcoordsy)].configure(bg='red', fg='red')
                        needfruit = False
                        break
            tick = 0

            grid1.mylist[grid1.coords(x, y)].select()
            grid1.mylist[grid1.coords(x, y)].configure(foreground='green',bg='light gray')
            print(x)
            if len(snake_body) >= bodylength:
                snake_body.insert(0, grid1.coords(x, y))
                grid1.mylist[snake_body[-1]].deselect()
                grid1.mylist[snake_body[-1]].configure(foreground='black')
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

            if x == 21 and dir == 'Right':
                x= 1
            if x == 0 and dir == 'Left':
                x= 20
            if y == 21 and dir == 'Up':
                y = 1
            if y == 0 and dir == 'Down':
                y = 20
            if snake_body[0] in snake_body[1:]:
                dead(bodylength)

        print(tick)
        tick += 1
        try:
            master.update()
        except Exception:
            pass
        time.sleep(0.077)

master.after(2,var_states1)
master.mainloop()
