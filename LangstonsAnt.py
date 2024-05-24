import pygame as pg 
import numpy as np

# Initialize Pygame
pg.init()

#WINDOW SETUP
DIMESIONS = WIDTH, HEIGHT = 1440, 720
screen = pg.display.set_mode(DIMESIONS)
pg.display.set_caption("Langston's Ant")

YELLOW = (255,255, 135)
WHITE = (255, 255, 255)
pg.draw.rect(screen, YELLOW, (1440, 720, 5,5))
def Main():
    clock = pg.time.Clock()

    fwd = 100
    lft = 100
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False

        pg.draw.rect(screen, YELLOW, (fwd, lft, 5, 5))
        pg.draw.rect(screen, WHITE, (fwd, lft, 5, 5))
        fwd=fwd+1
        lft=lft+1


        pg.display.flip()
        clock.tick(30)  # Set FPS

    pg.quit()


if __name__ == "__main__":
    Main()