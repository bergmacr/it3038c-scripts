import random
import math

width = 800
height = 600
BG = 255, 255, 255
FOOD_C = 128, 0, 0
BODY_C = 0, 0, 0
sqr_size = 10
SPEED = sqr_size

def dist(a, b):
    return math.sqrt((b.pos[0] - a.pos[0])**2 + (b.pos[1] - a.pos[1])**2)

def check_food(snake, food): 
    if dist(snake, food) > sqr_size:
        return False
    else:
        return True

def loser(snake, food):
    if snake.pos[0]<sqr_size or snake.pos[0]>width-sqr_size:
        return True
    if snake.pos[1]<sqr_size or snake.pos[1]>height-sqr_size:
        return True
    for i in snake.body[1:]:
        if i == snake.pos:
            return True

def game_speed(snake):
    if (10 + snake.score()//2)  < 30:
        return 10 + snake.score()//2
    else:
        return 30          

class Snake(object):
    def __init__(self):
        self.pos = [random.randint(1, (width-sqr_size)/10)*10,
                    random.randint(1, (height-sqr_size)/10)*10]
        self.mov = "UP"
        self.body = [self.pos[:]]

    def change_mov(self, key): #Decide where you are going to move
        if key == "UP" and self.mov != "DOWN":
            self.mov = key
        if key == "DOWN" and self.mov != "UP":
            self.mov = key
        if key == "RIGHT" and self.mov != "LEFT":
            self.mov = key
        if key == "LEFT" and self.mov != "RIGHT":
            self.mov = key

    def score(self):
        return len(self.body)

    def move(self, eat): #This is the snake's movement
        if self.mov == "UP": self.pos[1] = self.pos[1] - SPEED
        if self.mov == "DOWN": self.pos[1] = self.pos[1] + SPEED
        if self.mov == "LEFT": self.pos[0] = self.pos[0] - SPEED
        if self.mov == "RIGHT": self.pos[0] = self.pos[0] + SPEED
        self.body.insert(0, self.pos[:])
        if not eat:
           self.body.pop()


class Food(object):
    def __init__(self):
        self.pos = [random.randint(1, (width-sqr_size)/10)*10,
                    random.randint(1, (height-sqr_size)/10)*10]
