

from math import sin, cos, degrees, radians, floor
from time import time
import pygame


def Collision(playerInfo, ListofBulletInfo):
    Collide, NearHit = False, False
    for bulletInfo in ListofBulletInfo:
        if playerInfo[0].colliderect(bulletInfo[0]):
            offset = (int(playerInfo[2][0] - bulletInfo[2][0]),
                      int(playerInfo[2][1] - bulletInfo[2][1]))
            if bulletInfo[1].overlap(playerInfo[1], offset):
                Collide = True
    return NearHit, Collide

def RotAngle(angle):
    return angle+90


def RotationBlit(Surface, Image, Position, Angle=0, Alpha=255):
    rotatedIMG = pygame.transform.rotate(Image, Angle)
    rotatedIMG.set_alpha(Alpha)
    Surface.blit(rotatedIMG, (int(Position[0] - rotatedIMG.get_width()/2),
                              int(Position[1] - rotatedIMG.get_height()/2)))


def TimeIt(duration, start, compensation=0):
    return time() - (start+compensation) > duration


# def TrigVectors(angle, velocity, position, dt=1):
#     rounds = floor(angle/90) % 4
#     rad = radians(angle % 90)
#     sinResult = sin(rad)*velocity*dt
#     cosResult = cos(rad)*velocity*dt
#     if AXISTUPLE[rounds][0]:
#         position[0] += sinResult*AXISTUPLE[rounds][1][0]
#         position[1] -= cosResult*AXISTUPLE[rounds][1][1]
#     else:
#         position[1] += sinResult*AXISTUPLE[rounds][1][0]
#         position[0] -= cosResult*AXISTUPLE[rounds][1][1]
#     return position

# AXISTUPLE = ((True, (1, 1)), (False, (1, -1)),
#              (True, (-1, -1)), (False, (-1, 1)))

def TrigVectors(angle, velocity, position, dt=1):
    rad = radians(angle)
    position[0] += cos(rad)*velocity
    position[1] += sin(rad)*velocity
    return position

def RotPosition(Image, Angle, Position):
    rotatedIMG = pygame.transform.rotate(Image, Angle)
    return (int(Position[0] - rotatedIMG.get_width()/2),
            int(Position[1] - rotatedIMG.get_height()/2))


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
#



def OutOfBounds(SCREEN_SIZE, PlayerObject, PlayerRect):
    PlayerObject.position = [clamp(PlayerObject.position[0], 0, SCREEN_SIZE[0]), clamp(PlayerObject.position[1], 0, SCREEN_SIZE[1])]
    return PlayerObject

