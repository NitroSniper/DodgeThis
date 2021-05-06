
from statistics import mean
from time import perf_counter as perf_counter


from time import time
from Player import *
from engine import *
from pygame import gfxdraw
from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    K_w,
    K_s,
    K_a,
    K_d,
    K_SPACE,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT
)

SCREEN_WIDTH = 1920*1
SCREEN_HEIGHT = 1080*1
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_SIZE = (1080, 540)  # x, y
# WINDOW_SIZE = (1920, 1080)
pygame.display.set_caption("Template")
# Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # True Screen
# Screen to Blit on other Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

P1 = PlayerObject((K_w, K_s, K_a, K_d), K_SPACE, 4, (0,0))
P2 = PlayerObject((K_UP, K_DOWN, K_LEFT, K_RIGHT), K_SPACE, 5, (400,200))
P1.customize({
    'angleIncrement' : -1,
    'angleIncrementMoving' : -4,
    'color' : (110, 1, 95),
    'trailDuration' : 1,
    'trailTimer' : 0.01,
    'MinorChanges' : (0, 150, True),
    'alphaChangeDuration' : (0.5, sinAlpha),
    'numSides' : 5
    
})


P2.customize({
    'angleIncrement' : -1,
    'angleIncrementMoving' : -4,
    'color' : (3, 207, 252),
    'trailDuration' : 2,
    'trailTimer' : 0.01,
    'MinorChanges' : (100, 170, True),
    'alphaChangeDuration' : (0.5, modAlpha),
    'numSides' : 3
    
})



PLAYERLOOPORDER = ((KEYDOWN, True), (KEYUP, False))
frame = []
displayframe = []

HDMode = True

import pygame.gfxdraw


def DrawImages():
    pass


def Game():
    start = perf_counter()
    PLAYERS = [P1, P2]
    TRAILS = []



    programRunning = True
    while programRunning:
        dt = (perf_counter() - start)*120
        start = perf_counter()
        
        for event in pygame.event.get():
            for keyState, value in PLAYERLOOPORDER:
                if event.type == keyState:
                    for player in PLAYERS:
                        for controlKey, direction in zip(player.moveSet, player.movement):
                            if event.key == controlKey:
                                player.movement[direction] = value
            if event.type == QUIT:
                programRunning = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                programRunning = False


        for player in PLAYERS:
            player.update(dt, TRAILS)

        for trail in TRAILS:
            trail.update(dt, TRAILS)

        #Drawing
        SCREENRECT = []
        SCREEN.fill((14, 18, 36))


        for trail in TRAILS:
            SCREEN.blit(trail.image, trail.position)
            SCREENRECT.append(trail.returnScreenRect())
        for player in PLAYERS:
            # RotationBlit(SCREEN, player.image, player.position, player.angle)
            # gfxdraw.aapolygon(SCREEN, player.vertices, (0,255,0))
            # RotationBlit(SCREEN, player.image, player.position, player.angle)
            SCREENRECT.append(player.returnScreenRect())
            SCREEN.blit(player.image, player.position)

       
        frame.append(1/(perf_counter()-start))
       
       
       
        gfxdraw.filled_polygon(SCREEN, ((150, 150), (200, 200), (250, 150), (200, 100)), (255,0,255))
        
        if not HDMode: DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
        else: DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0))
        pygame.display.update(SCREENRECT)
        displayframe.append(1/(perf_counter()-start))
        # programRunning = False
    print (mean(frame))
    print (mean(displayframe))
    print (len(TRAILS))


if __name__ == '__main__':
    Game()
