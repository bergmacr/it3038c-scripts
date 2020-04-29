import pygame, sys
import vars

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((vars.width,vars.height))
pygame.display.update()

lost = False
eat = False
snake = vars.Snake()
food = vars.Food()
screen.fill(vars.BG)
key1 = "0"

def whatkey(event):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return "LEFT"
            if event.key == pygame.K_RIGHT:
                return "RIGHT"
            if event.key == pygame.K_UP:
                return "UP"
            if event.key == pygame.K_DOWN:
                return "DOWN"

while not lost:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        key1 = whatkey(event)
   
    snake.change_mov(key1)
    eat = vars.check_food(snake, food)
    snake.move(eat)
    if eat:
        food = vars.Food()
    lost = vars.loser(snake, food)

    screen.fill(vars.BG)
    for i in snake.body:
        pygame.draw.circle(screen, vars.BODY_C, (i[0], i[1]), vars.sqr_size, 0)
    pygame.draw.circle(screen, vars.FOOD_C, (food.pos[0], food.pos[1]), vars.sqr_size, 0)
    pygame.display.set_caption("Snake. Your score is: {}".format(snake.score()))
    pygame.display.update()

    #Game speed 
    msElapsed = clock.tick(vars.game_speed(snake))            

#this will show the lose screen
pygame.display.update()
screen.fill(vars.BG)
textsurface1 = myfont.render('You lost. Your score is:', False, (0, 0, 0))
textsurface2 = myfont.render("{}".format(snake.score()), False, (0, 0, 0))
screen.blit(textsurface1,(250, 200))
screen.blit(textsurface2,(380,280))
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
