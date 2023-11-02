import random
from random import randint
from tkinter import Tk, Canvas


WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self):
        self.R = randint(10, 50)  
        self.x = randint(self.R, WIDTH - self.R) 
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10)  
        self.color = self.random_color()
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill=self.color)  #меняем на селф калор, чтобы цвет был рандомным

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def random_color(self):
        q = random.randint(0, 200)
        w = random.randint(0, 200)
        e = random.randint(0, 200)
        return f'#{q:02x}{w:02x}{e:02x}'


def click_handler(event):
    balls.append(Ball())  #создаём новый шарик, чтобы он появлялся при тыке на экран и шёл в список шариков
    print('Hello World! x=', event.x, 'y=', event.y)

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for _ in range(5)]
tick()
root.mainloop()