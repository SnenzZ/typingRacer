# Typing Racer Game in Python with Pygame!
import pygame, random, copy

# pip install pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Typing Racer in Python!')
# pygame.SRCALPHA is a constant that pygame uses to tell a newly created surface that it needs to have an alpha channel
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60



def draw_screen():
    # screen outlines for background and title bar area
    # rect: ersten zwei Werte sind x und y-Achse und die letzten sind Höhe und Breite
    pygame.draw.rect(screen, (32,42,68), [0, HEIGHT - 100, WIDTH, 100], 100)
    pygame.draw.rect(screen, 'white', [0, 0, WIDTH, HEIGHT], 5)
    pygame.draw.line(screen, 'white', (250, HEIGHT - 100), (250, HEIGHT), 2)
    pygame.draw.line(screen, 'white', (700, HEIGHT - 100), (700, HEIGHT), 2)
    pygame.draw.line(screen, 'white', (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)
    pygame.draw.rect(screen, 'black', [0, 0, WIDTH, HEIGHT], 2)
    # text for showing the current level, player's current input, high score, score, lives and pause



# loads in assets like fonts and sound effects and music
run = True
while run:
    screen.fill('grey')
    timer.tick(fps)
    draw_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()

pygame.display.set_caption('Typing Racer in Python!')
