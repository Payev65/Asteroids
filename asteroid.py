import pygame
import random
from constants import *
from circleshape import CircleShape 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            rand_vector1 = self.velocity.rotate(-rand_angle)
            rand_vector2 = self.velocity.rotate(rand_angle) 
            new_r = self.radius - ASTEROID_MIN_RADIUS

            half1 = Asteroid(self.position.x, self.position.y,new_r)
            half1.velocity = rand_vector1 * 1.2

            half2 = Asteroid(self.position.x, self.position.y,new_r)
            half2.velocity = rand_vector2 * 1.2
