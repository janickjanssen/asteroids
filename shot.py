import pygame
import circleshape
import constants

class Shot(circleshape.CircleShape):
    def __init__(self,x: float, y:float):
        super().__init__(x,y,constants.SHOT_RADIUS)
    def draw(self,screen: pygame.Surface):
        pygame.draw.circle(screen,"white", self.position,self.radius)
    def update(self, dt: float) -> None:
       self.position += self.velocity * dt
