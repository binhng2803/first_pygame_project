import pygame
import os

# create a window of game
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption('My first pygame project!')
COLOR = '#8776FF'
FPS = 60
VEL = 7

BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 50
red_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png')) 
red_spaceship = pygame.transform.rotate(pygame.transform.scale(
    red_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

yellow_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png')) 
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(
    yellow_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def control_red_spaceship(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - VEL > 0: # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + red.height < BORDER.x: # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0: # UP
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + red.width < HEIGHT: # DOWN
        red.y += VEL
        
def control_yellow_spaceship(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + 10 : # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.height < WIDTH: # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.width <HEIGHT: # DOWN
        yellow.y += VEL

def draw_window(red, yellow):
    WIN.fill(COLOR)
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    pygame.display.update()

def main():
    
    red = pygame.Rect(30, 265, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(820, 265, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        control_red_spaceship(keys_pressed, red)
        control_yellow_spaceship(keys_pressed, yellow)
        draw_window(red, yellow)
                
    pygame.quit()
    
if __name__ == '__main__':
    main()