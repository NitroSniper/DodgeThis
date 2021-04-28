import pygame
from math import sin, cos, pi
DEFAULT_SPEED = 5
DEFAULT_LIVES = 3
DEFAULT_ANGLE = 3
SIZE = 20
# https://stackoverflow.com/questions/67168804/how-to-make-a-circular-countdown-timer-in-pygame
# https://stackoverflow.com/questions/3436453/calculate-coordinates-of-a-regular-polygons-vertices

class PlayerObject(object):
    def __init__(self, moveSetKey, dashKey, image, position):
        self.image = pygame.image.load(
            f'Images\{image}.png').convert_alpha()
        self.size = (self.image.get_width(), self.image.get_height())
        self.size = (30, 30)
        print (self.size)
        self.moveSet = moveSetKey

        self.position = list(position)
        self.angle = 200
        self.speed = DEFAULT_SPEED

        # dashing = DashClassObject()

        # moveSetKey should be up, down, left, right, dash
        self.movement = {'UP': False, 'DOWN': False,
                         'LEFT': False, 'RIGHT': False}


        #Customizable
        self.angleIncrement = 2


        # Random Information
        self.numSides = 5
        self.centeralAngle = angle = 2 * pi / self.numSides# numPoints
        self.vertices = updateVertices(self.position, self.size[0]/2, self.centeralAngle, self.numSides)

    def update(self, dt):
        self.angle = self.angleIncrement*dt
        if any(move == True for move in self.movement.values()):
            if self.movement['UP']:
                self.position[1] -= self.speed*dt
            if self.movement['DOWN']:
                self.position[1] += self.speed*dt
            if self.movement['LEFT']:
                self.position[0] -= self.speed*dt
            if self.movement['RIGHT']:
                self.position[0] += self.speed*dt
        
        self.vertices = updateVertices(self.position, self.size[0]/2, self.centeralAngle, self.numSides)
    def customize(self):
        pass

def updateVertices(position, radius, angle, numPoints):
    vertices = []
    for i in range(numPoints):
        vertices.append((position[0] + radius * sin(i * angle), position[1] + radius * cos(i * angle)))
    return vertices









def GFXDrawShape(numPoints, radius): #
    surf = pygame.Surface((2*(radius), 2*(radius)), pygame.SRCALPHA)
    angle = 2 * pi / numPoints
    vertices = []
    for i in range(numPoints):
        vertices.append((radius + radius * sin(i * angle), radius + radius * cos(i * angle)))
    gfxdraw.aapolygon(surf, vertices, (255,255,0))
    gfxdraw.filled_polygon(surf, vertices, (255,255,0))
    pygame.image.save(surf, 'test.png')