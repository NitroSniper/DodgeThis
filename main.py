
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
    K_SPACE
)

SCREEN_WIDTH = 1920*1
SCREEN_HEIGHT = 1080*1
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_SIZE = (1080, 540)  # x, y
WINDOW_SIZE = (1920, 1080)
pygame.display.set_caption("Template")
# Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # True Screen
# Screen to Blit on other Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

P1 = PlayerObject((K_w, K_s, K_a, K_d), K_SPACE, 'Hexagon', (200,200))
PLAYERLOOPORDER = ((KEYDOWN, True), (KEYUP, False))
frame = []


HDMode = True

import pygame.gfxdraw


def DrawImages():
    pass


def Game():
    start = perf_counter()
    PLAYERS = [P1]
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
            player.update(dt)

        #Drawing
        SCREEN.fill((14, 18, 36))


        for player in PLAYERS:
            # RotationBlit(SCREEN, player.image, player.position, player.angle)
            # gfxdraw.aapolygon(SCREEN, player.vertices, (0,255,0))
            gfxdraw.filled_polygon(SCREEN, player.vertices, (0,255,0))
        gfxdraw.filled_polygon(SCREEN, ((150, 150), (200, 200), (250, 150), (200, 100)), (255,0,255))
        
        if not HDMode: DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
        else: DISPLAY.blit(pygame.transform.smoothscale(SCREEN, WINDOW_SIZE), (0, 0))
        pygame.display.update()

        frame.append(1/(perf_counter()-start))
        # programRunning = False
    print (mean(frame))


if __name__ == '__main__':
    Game()
