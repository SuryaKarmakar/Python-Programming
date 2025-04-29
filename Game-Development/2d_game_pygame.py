import pygame # type: ignore

# initializing pygame module.
pygame.init()

# setting up the display.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

# drawing on screen.
blue_color = (0, 0, 255)
pygame.draw.rect(screen, blue_color, pygame.Rect(30, 30, 60, 60))

# simple game lop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()