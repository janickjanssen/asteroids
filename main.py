# from player import Player
import pygame
from player import *
# import player
from logger import log_state
# import constants
from constants import *#SCREEN_WIDTH, SCREEN_HEIGHT,PLAYER_RADIUS

def main():
	#print("Hello from asteroids!")
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt : float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)
        # player.update(dt)

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


#        print(f"dt:{dt}")



if __name__ == "__main__":
    main()
