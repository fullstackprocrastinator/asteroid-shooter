import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Astroid Shooter")


# Create a surface
test_surface = pygame.Surface((400, 100))


# Input
while True: # Essentially keeps the game running
    for event in pygame.event.get(): # Events such as mouse click, buttons press etc
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit() # Close all


# Updates
display_surface.blit(test_surface, (0,0))
display_surface.fill("yellow")

# Update Display Surface
pygame.display.update()