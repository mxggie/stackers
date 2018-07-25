from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
#this script demostrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()
turqouise = (0, 255, 200)

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True

    def startGame(self) :
        pygame.time.set_timer(USEREVENT +1, 700)
        n = 0
        r = 7
        x = 0
        y = 0
        z = 0
        while self.gaming:
            for event in pygame.event.get():        
                if event.type == KEYDOWN:                   
                    if r == 7:
                        x = n 
                    if r == 5:
                        y = n
                    if r == 3:
                        z = n               
                    if r <= 1:
                        if x == n and y == n and z == n:
                            sense.show_message("You Won!", 0.05, text_colour=turqouise)                      
                            self.gaming = False  
                            exit()
                        else:
                            sense.show_message("You Lost", 0.05, text_colour=turqouise)                     
                            self.gaming = False
                            exit()
                    sense.set_pixel(n, r, (0,255,0))                    
                    r -= 1
                    
                else:                    
                    sense.set_pixel(n, r, (0,255,255))
                    time.sleep(0.25)                        
                    sense.set_pixel(n, r, (0,0,0))
                    n += 1
                    if n == 8:
                        n = 0

if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()

