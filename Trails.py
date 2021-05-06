from math import sin, pi
from engine import GFXDrawShape, TimeIt, clamp
from time import perf_counter
import pygame


#alpha limit 100-170
# if alpha goes above 170 then difference starts at 100
# if given alpha
# if lowerbound + alpha%upperbound



def sinAlpha(alpha, *args):
    mid = (args[1]+args[0])/2
    return sin(alpha*pi/mid)*mid+mid

def modAlpha(alpha, *args): #arg0 = lower arg1 = upper
    return args[0] + alpha%(args[1]-args[0])


class TrailTemplate(object):
    def __init__(self, position, startingAngle, whenKill, angleIncrement=0, PolyInfo=None, MinorChanges=(0, 255, True), alphaChangeDuration=None):
        self.position = position[::]
        self.angleMomentum = angleIncrement
        self.angle = startingAngle
        self.whenKill = whenKill
        self.start = perf_counter()
        self.alpha = 255
        self.MinorChanges = MinorChanges #Alpha min, alpha max, 
        self.PolyInfo = PolyInfo
        self.alphaChangeDuration = alphaChangeDuration if alphaChangeDuration else (whenKill, modAlpha)
    def isItTimeToKill(self, start, whenKill):
        if TimeIt(whenKill, start):
            return True
        return False
    def returnScreenRect(self):
        return pygame.Rect((self.position), (2*self.PolyInfo[1], 2*self.PolyInfo[1]))



class MotionBlurEffectTrail(TrailTemplate):
    def update(self, dt, TRAILS):
        if self.MinorChanges[2]:
            self.alpha = self.MinorChanges[0] + (perf_counter() - self.start)/self.alphaChangeDuration[0]*(self.MinorChanges[1] - self.MinorChanges[0])
        else: self.alpha = self.MinorChanges[1] - (perf_counter() - self.start)/self.alphaChangeDuration[0]*(self.MinorChanges[1] - self.MinorChanges[0])
        
        
        if not self.isItTimeToKill(self.start, self.whenKill):
            self.angle += self.angleMomentum*dt
            self.image = GFXDrawShape(*self.PolyInfo, self.angle, alpha=self.alphaChangeDuration[1](self.alpha, self.MinorChanges[0], self.MinorChanges[1]))
            
            return  # Kill or not
        TRAILS.remove(self)
    
class SpriteCircleRadiusTrail(object):
    def __init__(self, position, startingAngle, whenKill, angleIncrement=0, PolyInfo=None, MinorChanges=(0, 255, True), alphaChangeDuration=None):
        self.position = position
        self.angleMomentum = angleIncrement
        self.angle = 0
        self.whenKill = 1000000000
        self.start = perf_counter()
        self.alpha = 255
        self.MinorChanges = MinorChanges