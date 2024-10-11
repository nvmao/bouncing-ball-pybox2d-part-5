import colorsys

import pygame
from Box2D import b2World
from pygame import DOUBLEBUF

from MyContactListener import MyContactListener


class Utils():

    def __init__(self):

        pygame.init()
        self.width = 600
        self.height = 600

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)

        self.dt = 0
        self.clock = pygame.time.Clock()


        self.PPM = 10.0  # Pixels per meter
        self.world = b2World(gravity=(0, -20), doSleep=True)

        self.contactListener = MyContactListener()
        self.world.contactListener = self.contactListener


    def to_Pos(self,pos):
        """Convert from Box2D to Pygame coordinates."""
        return (pos[0] * self.PPM, self.height - (pos[1] * self.PPM))

    def from_Pos(self,pos):
        """Convert from Pygame to Box2D coordinates."""
        return (pos[0] / self.PPM, (self.height - pos[1]) / self.PPM)

    def calDeltaTime(self):  # calculate deltaTime
        t = self.clock.tick(60 * 2)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt

    def hueToRGB(self,hue):
        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        # Scale RGB values to 0-255 range
        return (int(r * 255), int(g * 255), int(b * 255))

utils = Utils()  # util is global object
