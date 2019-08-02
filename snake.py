import gridcreation as gc
from tkinter import messagebox
import random

class snake:
    def __init__(self):
        self.grid = gc.grid_reverse(20,20)
        self.root = self.grid.root

        self.root.focus_force()
        self.setup()

        self.root.bind("<Right>", self.right)
        self.root.bind("d", self.right)
        self.root.bind("<Left>", self.left)
        self.root.bind("a", self.left)
        self.root.bind("<Up>", self.up)
        self.root.bind("w", self.up)
        self.root.bind("<Down>", self.down)
        self.root.bind("s", self.down)

        self.loop()
        self.root.mainloop()

    def setup(self):
        self.x = 0
        self.y = self.grid.numbery//2
        self.dir = "Right"
        self.length = 10
        self.body = []
        self.need_fruit = True
        self.death_on_wall = True

    def loop(self):
        self.previous_dir = self.dir

        if self.need_fruit:
            while self.need_fruit:
                randcoordsx = random.randint(1, self.grid.numberx)
                randcoordsy = random.randint(1, self.grid.numbery)
                if not self.grid.coords(randcoordsx,randcoordsy) in self.body:
                    self.fruit_place = self.grid.coords(randcoordsx,randcoordsy)
                    box = self.grid.boxlist[
                        self.grid.coords(randcoordsx,randcoordsy)
                    ]
                    box.select()
                    box.configure(bg='red', fg='red')

                    self.need_fruit = False

        if self.dir == 'Right':
            self.x+=1
            if self.x == self.grid.numberx+1:
                if self.death_on_wall:
                    self.dead(self.length)
                    return
                else:
                    self.x = 1
        if self.dir == 'Left':
            self.x-=1
            if self.x == 0:
                if self.death_on_wall:
                    self.dead(self.length)
                    return
                else:
                    self.x = self.grid.numberx
        if self.dir == 'Up':
            self.y-=1
            if self.y == 0:
                if self.death_on_wall:
                    self.dead(self.length)
                    return
                else:
                    self.y = self.grid.numbery
        if self.dir == 'Down':
            self.y+=1
            if self.y == self.grid.numbery+1:
                if self.death_on_wall:
                    self.dead(self.length)
                    return
                else:
                    self.y = 1


        self.grid.boxlist[self.grid.coords(self.x, self.y)].select()
        self.grid.boxlist[self.grid.coords(self.x, self.y)].configure(foreground='green',bg='light gray')

        if len(self.body) >= self.length:
            self.body.insert(0, self.grid.coords(self.x, self.y))
            if not self.body[0] == self.body[-1]:
                body = self.grid.boxlist[self.body[-1]]
                body.deselect()
                body.configure(foreground='black')
            self.body.pop(-1)
        else:
            self.body.insert(0, self.grid.coords(self.x, self.y))

        if len(self.body) >= 1:
            if self.body[0] in self.body[1:]:
                self.dead(self.length)
                return

        if self.body[0] == self.fruit_place:
            self.length += 1
            self.need_fruit = True

        self.root.after(100, self.loop)

    def right(self, event=None):
        if not self.previous_dir == "Left":
            self.dir = "Right"
    def left(self, event=None):
        if not self.previous_dir == "Right":
            self.dir = "Left"
    def up(self, event=None):
        if not self.previous_dir == "Down":
            self.dir = "Up"
    def down(self, event=None):
        if not self.previous_dir == "Up":
            self.dir = "Down"

    def dead(self, length):
        messagebox1 = messagebox.askquestion('Game Over', f'You died with a length of {length}\nWould you like to play again?')
        if messagebox1 == 'yes':
            self.reload()
        else:
            self.grid.root.destroy()

    def reload(self):
        for i in self.grid.boxlist:
            i.deselect()
            i.configure(bg='light gray')

        self.setup()
        self.loop()

if __name__ == "__main__":
    snake()
