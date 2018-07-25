from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
#this script demostrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True

    def startGame(self) :
        pygame.time.set_timer(USEREVENT +1, 600)
        n = 0
        while self.gaming:
            for event in pygame.event.get():        
                if event.type == KEYDOWN:   
                    sense.set_pixel(n-1, 7, (0,255,255))              
                    self.gaming = False
                else:                    
                    sense.set_pixel(n, 7, (0,255,255))
                    time.sleep(.5)                        
                    sense.set_pixel(n, 7, (0,0,0))
                    n += 1
                    if n == 8:
                        n = 0

if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()

