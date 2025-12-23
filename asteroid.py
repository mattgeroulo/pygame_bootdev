from circleshape import CircleShape
import constants
import pygame
import random
from logger import log_state,log_event
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,surface):
        pygame.draw.circle(surface,"white",self.position,self.radius,constants.LINE_WIDTH)
        
    def update(self,dt):
        self.position+= self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")   
        angle = random.uniform(20,50) 
        turd1 = self.velocity.rotate(angle)
        turd2= self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        Assturd1 = Asteroid(self.position.x,self.position.y,new_radius)
        Assturd2 = Asteroid(self.position.x,self.position.y,new_radius)
        Assturd1.velocity=turd1*1.2
        Assturd2.velocity=turd2
        
        