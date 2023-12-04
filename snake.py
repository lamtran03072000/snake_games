import pygame
import random
#khởi tạo

pygame.init()

#set display window 

WINDOWN_WIDTH = 800
WINDOWN_HEIGHT = 800

display_surface = pygame.display.set_mode((WINDOWN_WIDTH,WINDOWN_HEIGHT))
pygame.display.set_caption("~snake~")

#set fsp and clock
FPS = 20
clock = pygame.time.Clock()
#set game values

SNAKE_SIZE  = 20

head_x = WINDOWN_WIDTH /2
head_y = WINDOWN_HEIGHT /2 + 100

snake_dx = 0
snake_dy = 0


score = 0



#set colors 
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
RED = (255,0,0)
DARKRED = (150,0,0)
WHITE= (255,255,255)
#set fonts
font = pygame.font.SysFont("gabriola",48)
#set text
title_text = font.render("~snake",True,GREEN,DARKGREEN)
title_react = title_text.get_rect()
title_react.center = (WINDOWN_WIDTH/2,WINDOWN_HEIGHT/2)


score_text = font.render("Score : " + str(score),True,GREEN,DARKGREEN)
score_react = score_text.get_rect()
score_react.topleft = (10,10)

game_over_text = font.render("Game over",True,RED,DARKGREEN)
game_over_react = game_over_text.get_rect()
game_over_react.center = (WINDOWN_WIDTH//2,WINDOWN_HEIGHT//2)

continue_text = font.render("press any key to play agin", True,RED,DARKGREEN)
continue_react = continue_text.get_rect()
continue_react.center = (WINDOWN_WIDTH//2,WINDOWN_HEIGHT//2)
# set sound
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")
#set images
# 
apple_coord = (500,500,SNAKE_SIZE,SNAKE_SIZE) 
apple_react = pygame.draw.rect(display_surface,RED,apple_coord)

head_coord = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
body_coord = []
head_react = pygame.draw.rect(display_surface,RED,head_coord)
#
background = pygame.image.load('assets/images/bg.jpg')
background = pygame.transform.scale(background, (WINDOWN_WIDTH, WINDOWN_HEIGHT))
# khi chạy
running = True
while running:
    #check xem user muốn quit không ?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

        #move snake
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_dx = -1* SNAKE_SIZE
                    snake_dy = 0
                if event.key == pygame.K_RIGHT:
                    snake_dx =  SNAKE_SIZE
                    snake_dy = 0
                if event.key == pygame.K_UP:
                    snake_dy = -1* SNAKE_SIZE
                    snake_dx = 0
                if event.key == pygame.K_DOWN:
                    snake_dy = 1* SNAKE_SIZE
                    snake_dx = 0    
    

   
    # /////////

    body_coord.insert(0,head_coord)
    body_coord.pop()
     #update lại vị trí rắn
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)

    #check for game over
    if head_react.left < 0 or head_react.right > WINDOWN_WIDTH or head_react.top < 0 or head_react.bottom >WINDOWN_HEIGHT or head_coord in body_coord:
        display_surface.blit(game_over_text,game_over_react)
        display_surface.blit(continue_text,continue_react)
        pygame.display.update()
        #pause game khi player press a key , then reset the game
        is_pause = True
        while is_pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    score_text = font.render("Score : " + str(score),True,GREEN,DARKGREEN)
                    head_x =WINDOWN_WIDTH/2
                    head_y = WINDOWN_HEIGHT /2 + 100
                    head_coord = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
                    body_coord = []
                    snake_dx = 0
                    snake_dy = 0 
                    is_pause = False
                if event.type == pygame.QUIT:
                    is_pause = False
                    running = False


    # check khi va trạm
    if head_react.colliderect(apple_react):
        score += 1
        pick_up_sound.play()    
        apple_x = random.randint(0,WINDOWN_WIDTH )
        apple_y = random.randint(0,WINDOWN_HEIGHT )
        apple_coord = (apple_x,apple_y,SNAKE_SIZE,SNAKE_SIZE)
        body_coord.append(head_coord)
    #update điểm số
        score_text = font.render("Score : " + str(score),True,GREEN,DARKGREEN)
    display_surface.fill(WHITE)
    display_surface.blit(background, (0, 0)) # <-- Đặt dòng này ở đây

    #Blit HUD
    display_surface.blit(title_text,title_react)
    display_surface.blit(score_text,score_react)

    #Blit assets
    #Still need to do the body
    for body in body_coord:
        pygame.draw.rect(display_surface,DARKGREEN,body)
    head_react=  pygame.draw.rect(display_surface,GREEN,head_coord)
    apple_react= pygame.draw.rect(display_surface,DARKRED,apple_coord)
    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)
    #x


pygame.quit()


