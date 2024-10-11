import math
import random

import pygame
from Box2D import b2EdgeShape, Box2D
from pygame import Vector2

from Particle import Explosion
from utils import utils


class Ring:
    def __init__(self, pos, radius,rotateDir,size,hue):
        self.color = (255,255,255)
        self.radius = radius

        self.rotateDir = rotateDir
        self.size = size
        self.vertices = []
        for i in range(self.size):
            angle = i * (2 * math.pi / self.size)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            self.vertices.append((x, y))

        self.body = utils.world.CreateStaticBody(position=utils.from_Pos(pos))
        self.body.userData = self

        self.create_edge_shape()
        self.hue = hue

        self.destroyFlag = False


    def create_edge_shape(self):
        if self.size == 50:
            for i in range(self.size):
                angle = i * (360 / self.size)
                if (0 <= angle <= 320) :
                    v1 = self.vertices[i]
                    v2 = self.vertices[(i + 1) % self.size]
                    edge = b2EdgeShape(vertices=[v1, v2])
                    self.body.CreateEdgeFixture(shape=edge, density=1, friction=0.0, restitution=1.0)
        if self.size == 3 or self.size == 4:
            for i in range(self.size):
                if i == 0:
                    holeSize = 4
                    v1 = Vector2(self.vertices[i])
                    v2 = Vector2(self.vertices[(i + 1) % self.size])
                    length = (v2 - v1).length()
                    dir = (v2 - v1).normalize()
                    mV1 = v1 + dir * (length / 2 - holeSize)
                    mV2 = v1 + dir * (length / 2 + holeSize)

                    edge = b2EdgeShape(vertices=[v1, mV1])
                    self.body.CreateEdgeFixture(shape=edge, density=1, friction=0.0, restitution=1.0)

                    edge = b2EdgeShape(vertices=[mV2, v2])
                    self.body.CreateEdgeFixture(shape=edge, density=1, friction=0.0, restitution=1.0)
                else:
                    v1 = self.vertices[i]
                    v2 = self.vertices[(i + 1) % self.size]
                    edge = b2EdgeShape(vertices=[v1, v2])
                    self.body.CreateEdgeFixture(shape=edge, density=1, friction=0.0, restitution=1.0)


    def draw(self):
        self.hue = (self.hue + utils.deltaTime()/5) % 1
        self.color = utils.hueToRGB(self.hue)

        self.body.angle += self.rotateDir * utils.deltaTime()


        self.draw_edges()

    def draw_edges(self):
        for fixture in self.body.fixtures:
            v1 = utils.to_Pos(self.body.transform * fixture.shape.vertices[0])
            v2 = utils.to_Pos(self.body.transform * fixture.shape.vertices[1])
            pygame.draw.line(utils.screen, self.color, v1, v2, 6)


    def spawParticles(self):
        particles = []
        center = Vector2(utils.width/2,utils.height/2)
        for i in range(0,360,5):
            x = math.cos(math.radians(i)) * self.radius * 10
            y = math.sin(math.radians(i)) * self.radius * 10
            pos = center + Vector2(x,y)
            exp = Explosion(pos.x,pos.y,self.color)
            particles.append(exp)
        return particles