import pygame

DEFAULT_SPEED = 5
DEFAULT_LIVES = 3
DEFAULT_ANGLE = 3

# https://stackoverflow.com/questions/67168804/how-to-make-a-circular-countdown-timer-in-pygame

class PlayerObject(object):
    def __init__(self, moveSetKey, dashKey, image, position):
        self.image = pygame.image.load(
            f'Images\{image}.png').convert_alpha()
        self.size = (self.image.get_width(), self.image.get_height())
        
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
    def customize(self):
        pass