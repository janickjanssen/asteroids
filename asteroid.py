import pygame
import constants
import logger
import random
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen: pygame.Surface):
        pygame.draw.circle(screen,"white", self.position,self.radius)#self.radius,constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        logger.log_event("asteroid_split")
        random_number = random.uniform(20,50)

        vel_1 = self.velocity.rotate(random_number)
        vel_2 = self.velocity.rotate(-random_number)
        rad_new = self.radius - constants.ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x,self.position.y,rad_new)
        ast_1.velocity = vel_1 * 1.2
        ast_2 = Asteroid(self.position.x,self.position.y,rad_new)
        ast_2.velocity = vel_2 * 1.2
