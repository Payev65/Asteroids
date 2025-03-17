import pygame
from constants import *
from circleshape import CircleShape 
from Shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.speed = 0
        self.acceleration = PLAYER_MAX_SPEED/PLAYER_FROM_ZERO_TO_FULLSPEED
        self.drag = PLAYER_MAX_SPEED/PLAYER_FROM_FULLSPEED_TO_ZERO

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x,self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SOOT_COOLDOWN


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update_movment(self,dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed +=  (self.acceleration * dt)
            if self.speed > PLAYER_MAX_SPEED:
                self.speed = PLAYER_MAX_SPEED

        elif keys[pygame.K_s]:
            self.speed -=  (self.acceleration * dt)
            if self.speed < -PLAYER_MAX_SPEED:
                self.speed = -PLAYER_MAX_SPEED

        elif self.speed < 0:
            self.speed += (self.drag * dt)
            if self.speed > 0:
                self.speed = 0

        elif self.speed > 0:
            self.speed -= (self.drag * dt)
            if self.speed < 0:
                self.speed = 0

        self.move(dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.update_movment(dt)

        self.timer -= dt