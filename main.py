import pygame #type: ignore
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)  
      
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        for obj in asteroids:
            if obj.collision(player) == True:
                print("Game over!")
                sys.exit()
                
            for shot in shots:
                if shot.collision(obj) == True:
                    shot.kill()
                    obj.split()
        
        pygame.display.flip()
        
        #limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()