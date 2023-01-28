import tkinter as tk
from random import randint

Width = 300
Height = 240

score = 0

class Ball:
    def __init__(self):
        self.r = randint(5,25)
        self.x = randint(self.r, Width - self.r)
        self.y = randint(self.r, Height - self.r)
        self.vx = randint(4, 5)
        self.vy = randint(-7, -5)  
        self.creating()


    def creating(self):
        self.ball_id = canvas.create_oval(self.x - self.r, self.y - self.r, 
                                        self.x + self.r, self.y + self.r, 
                                        fill='yellow')


    def show(self):
        canvas.move(self.ball_id, self.vx, self.vy)


    def gollkeeper_save(self):
        if self.x - self.r  <= gollkeeper_coords_x2 and self.x + self.r >= gollkeeper_coords_x:
            if self.y + self.r >= gollkeeper_coords_y:
                self.vy *= -1
                return self.vy
        else:
            if self.y + self.r >= Height:
                return self.Goal()
    

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= Width or self.x - self.r <= 0:
            self.vx = -self.vx
        if  self.y - self.r <= 0:
            return self.change_direct()
            

    
    

    def change_direct(self):
        self.vy *= -1


    def Goal(self):
        self.destroy()
        print("GOAL")


    def  destroy(self):
        canvas.delete(self.ball_id)
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0


class Gollkeeper:
    def __init__(self, master):
        self.master = master
        self.x = 100
        self.y = 230
        self.x2 = 190
        self.y2 = 240
        self.vx = 0
        self.vy = 0
        self.gollkeeper_id = canvas.create_rectangle(self.x, self.y, 
                                               self.x2, self.y2, fill='Red')
        self.bind_all()
    
    def show(self):
        canvas.move(self.gollkeeper_id, self.vx, self.vy)

    def move(self):
        self.x += self.vx
        self.x2 += self.vx
        self.y += self.vy
        if self.x <= 0 or self.x2 >=  Width:
            self.vx = 0
    
    def move_right(self):
        if self.x2 <= Width:
            self.vx = 9
            return


    def move_left(self):
        if self.x >= 0:
            self.vx = 4
            return

    def get_coords(self):
        global gollkeeper_coords_x, gollkeeper_coords_x2, gollkeeper_coords_y
        gollkeeper_coords_x = self.x
        gollkeeper_coords_x2 = self.x2
        gollkeeper_coords_y = self.y

    def bind_all(self):
        root.bind('<a>', lambda x: self.move_left())
        root.bind('<d>', lambda y: self.move_right())        



def tick():
    gollkeeper.show()
    gollkeeper.move()
    gollkeeper.get_coords()
    for ball in balls:
        ball.gollkeeper_save()
        ball.move()
        ball.show()
    root.after(30, tick)




def main():
    global root, canvas, balls, gollkeeper
    root = tk.Tk(className='Game')
    root.geometry(str(Width) + 'x' + str(Height))
    canvas = tk.Canvas(root)
    canvas.pack(anchor= 'nw' )
    balls = [Ball() for i in range (5)]
    gollkeeper = Gollkeeper(master= 'Me')
    tick()



main()
root.mainloop()