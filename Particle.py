
import math
import random

import pygame

from utils import utils


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.uniform(0.5, 2)
        angle = random.uniform(0,360)
        speed = random.uniform(0.1,1)
        self.vel_x = math.cos(math.radians(angle)) * speed
        self.vel_y = math.sin(math.radians(angle)) * speed
        self.life = random.randint(100, 1000)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.life -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Explosion:
    def __init__(self,x,y,color):
        # Create particles
        self.particles = []
        COLORS = [color]
        for _ in range(20):
            color = random.choice(COLORS)
            particle = Particle(x,y, color)
            self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.update()
        self.particles = [particle for particle in self.particles if particle.life > 0]

    def draw(self):
        for particle in self.particles:
            particle.draw(utils.screen)