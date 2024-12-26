from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        a1, a2 = Asteroid(self.position[0], self.position[1], radius), Asteroid(
            self.position[0], self.position[1], radius)

        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
