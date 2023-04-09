import pygame

# create a window of game
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption('My first pygame project!')
COLOR = '#8776FF'
FPS = 60

def draw_window():
    WIN.fill(COLOR)
    pygame.display.update()

def main():
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
                
    pygame.quit()
    
if __name__ == '__main__':
    main()