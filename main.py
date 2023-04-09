import pygame
import os

# create a window of game
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption('My first pygame project!')
COLOR = '#8776FF'
FPS = 60
VEL = 4
BULLETS_VEL = 6
MAX_BULLETS = 4
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

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

def control_bullet(yellow, red, yellow_bullets, red_bullets):
    for bullet in red_bullets:
        bullet.x += BULLETS_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)
            
    for bullet in yellow_bullets:
        bullet.x -= BULLETS_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)


def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill(COLOR)
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,(255, 0, 0), bullet) 
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,(255, 255, 0), bullet) 
    
    pygame.display.update()



def main():
    
    red = pygame.Rect(30, 265, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(820, 265, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.height, red.y + red.width//2 - 4, 10, 8)
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x - 10, yellow.y + yellow.width//2 - 4, 10, 8)
                    yellow_bullets.append(bullet)            
            
        keys_pressed = pygame.key.get_pressed()
        control_red_spaceship(keys_pressed, red)
        control_yellow_spaceship(keys_pressed, yellow)
        control_bullet(yellow, red, yellow_bullets, red_bullets)
        draw_window(red, yellow, red_bullets, yellow_bullets)
                
    pygame.quit()
    
if __name__ == '__main__':
    main()