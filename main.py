import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers=(shots,updatable,drawable)
    Player.containers = (updatable, drawable)
    
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers= (updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        player.cooldown-=dt
        for obj in asteroids:
            
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullets in shots:
                if bullets.collides_with(obj):
                    log_event("asteroid_shot")
                    obj.split()
                    bullets.kill()
                    
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
