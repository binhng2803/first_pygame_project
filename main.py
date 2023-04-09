import pygame
import os

# create a window of game
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption('My first pygame project!')
COLOR = '#8776FF'
FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 50
red_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png')) 
red_spaceship = pygame.transform.rotate(pygame.transform.scale(
    red_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

yellow_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png')) 
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(
    yellow_spaceship_image,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(COLOR)
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
        draw_window(red, yellow)
                
    pygame.quit()
    
if __name__ == '__main__':
    main()