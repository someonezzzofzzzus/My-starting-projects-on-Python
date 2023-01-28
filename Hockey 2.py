import tkinter as tk
from tkinter import ttk
from random import randint

Width = 300
Height = 250

    


class Ball:
    def __init__(self):
        self.r = randint(5,20)
        self.x = randint(self.r, Width - self.r)
        self.y = randint(self.r, Height - self.r)
        self.vx, self.vy = (+9, +5)
        self.ball_id = canvas.create_oval(self.x - self.r, self.y - self.r, 
                                        self.x + self.r, self.y + self.r, 
                                        fill='green')
    
    def show(self):
        canvas.move(self.ball_id, self.vx, self.vy)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= Width or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r >= Height or self.y - self.r <= 0:
            self.vy = -self.vy

    
    def set_coords():
        pass
        



class Gollkeeper:
    def __init__(self, vx, vy):
        self.x = randint(20,50)
        self.y = randint(20,50)
        self.vx = vx
        self.vy = vy
        self.gollkeeper_id = canvas.create_rectangle(self.x, self.y, 
                                               self.x + 20, self.y -10, fill='Red')
        print("Gollkeeper created")
    
    def show(self):
        self.x = self.move
        canvas.move(self.gollkeeper_id)
        
    
    def move(self):
        pass



    
    
    

class Field():
    def __init__(self):
        self.Gollkeeper = 1
    



def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)



def main():
    global root, canvas, balls
    root = tk.Tk(className='Game')
    root.geometry(str(Width) + 'x' + str(Height))
    canvas = tk.Canvas(root)
    canvas.pack(anchor= 'nw' )
    balls = ([Ball() for i in range (6)])
    tick()
    root.mainloop()


main()
