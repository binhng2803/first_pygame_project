import pygame

# create a window of game
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
COLOR = '#8776FF'

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(COLOR)
        pygame.display.update()
                
    pygame.quit()
    
if __name__ == '__main__':
    main()