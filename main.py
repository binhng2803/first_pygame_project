import pygame
import os
pygame.font.init()
pygame.mixer.init()

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
HEALTH_FONT = pygame.font.SysFont('comicsans', 44)
WINNER_FONT = pygame.font.SysFont('comicsans', 144)
BULLETS_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets\Grenade+1.mp3'))
BULLETS_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets\Gun+Silencer.mp3'))

BORDER = pygame.Rect(WIDTH//2-5, 0, 10, 500)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 50
red_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png')) 
red_spaceship = pygame.transform.rotate(pygame.transform.scale(
    red_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

yellow_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png')) 
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(
    yellow_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

space = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'space-earth.png')), (WIDTH, HEIGHT))


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


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(space, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    
    red_health_text = HEALTH_FONT.render(f'Health: {red_health}', 1, (255, 255, 255))
    WIN.blit(red_health_text, (10, 10))
    yellow_health_text = HEALTH_FONT.render(f'Health: {yellow_health}', 1, (255, 255, 255))
    WIN.blit(yellow_health_text,( WIDTH - yellow_health_text.get_width() - 10, 10))
    
    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,(255, 0, 0), bullet) 
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,(255, 255, 0), bullet) 
    
    pygame.display.update()

def draw_winner(winner_text):
    text = WINNER_FONT.render(winner_text, 1, (255, 255, 255))
    WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()) )
    pygame.display.update()
    pygame.time.delay(4000)
    
def main():
    
    red = pygame.Rect(30, 265, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(820, 265, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + red.height, red.y + red.width//2 - 4, 10, 8)
                    red_bullets.append(bullet)
                    BULLETS_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x - 10, yellow.y + yellow.width//2 - 4, 10, 8)
                    yellow_bullets.append(bullet)  
                    BULLETS_FIRE_SOUND.play()          
            
            if event.type == RED_HIT:
                red_health -= 1
                BULLETS_HIT_SOUND.play()
                
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLETS_HIT_SOUND.play()
            
        winner_text = ''
        if red_health == 0:
            winner_text = 'Yellow Wins!'
        if yellow_health == 0:
            winner_text = 'Red Wins!'  
        
            
        keys_pressed = pygame.key.get_pressed()
        control_red_spaceship(keys_pressed, red)
        control_yellow_spaceship(keys_pressed, yellow)
        control_bullet(yellow, red, yellow_bullets, red_bullets)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
        if winner_text != '':
            draw_winner(winner_text)
            break       
    main()
    
if __name__ == '__main__':
    main()