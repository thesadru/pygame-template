import os
os.makedirs('bin')
with open('main.py','w') as f_main:
    f_main.write("""import pygame
from pygame.locals import *

import resources


class Main():
    def __init__(self, resolution=(512, 512), maxfps=0, background=(255, 255, 255)):
        self.screen = pygame.display.set_mode(resolution)
        self.w, self.h = resolution
        self.clock = pygame.time.Clock()
        self.maxfps = maxfps
        self.loop = 0
        self.background = background

        self.mainloop = 1

    def stop(self):
        self.mainloop = 0

    def tick(self):
        self.dt = self.clock.tick(self.maxfps)
        self.fps = self.clock.get_fps()
        self.loop += 1

    def logic(self):
        pass

    def keys(self):
        key = pygame.key.get_pressed()
        if key[K_ESCAPE]:
            self.stop()
        if key[K_LALT] and key[K_F4]:
            self.stop()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stop()

    def draw(self):
        self.screen.fill(self.background)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    main = Main()
    while main.mainloop:
        main.tick()
        main.logic()
        main.keys()
        main.events()
        main.draw()
    pygame.quit()
            """)
with open('resources.py','w') as f_res:
    f_res.write("""import pygame
pygame.init()
def image(filename,resolution=None):
    image = pygame.image.load('bin/'+filename)
    if type(resolution) in (tuple,list):
        return pygame.transform.scale(image,resolution)
    return image

def sound(filename):
    return pygame.mixer.Sound('bin/'+filename)
            """)