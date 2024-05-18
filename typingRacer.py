# Typing Racer Game in Python with Pygame!
import pygame,random, copy
# pip install pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Typing Racer in Python!')
# pygame.SRCALPHA is a constant that pygame uses to tell a newly created surface that it needs to have an alpha channel
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60

# loads in assets like fonts and sound effects and music
run = True
while run:
    screen.fill('seagreen')
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()

