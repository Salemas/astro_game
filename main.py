import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot


def main():

 #   print('Starting asteroids!\nScreen width: 1280\nScreen height: 720')

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    #creating groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #adding player to groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers =(shots)

    #     object init 
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()



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

        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

    # colision detection asteroids with player
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("GAME OVER!!! MUAHA HA HA")
                running = False


        # flip() the display to put your work on screen
        pygame.display.flip()

 #       print(f'{dt} sekundes')
    pygame.quit()



if __name__ == "__main__":
    main()