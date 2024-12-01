import pygame
from constants import *
from circleshape import *
from player import *



def main():

 #   print('Starting asteroids!\nScreen width: 1280\nScreen height: 720')

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

#player init
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        dt = clock.tick(60) /1000  # limits FPS to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("darkslategray")

        # RENDER YOUR GAME HERE

        player.update(dt)
        player.draw(screen)



        # flip() the display to put your work on screen
        pygame.display.flip()

 #       print(f'{dt} sekundes')
    pygame.quit()



if __name__ == "__main__":
    main()