###### IMPORT ######

import pygame

###### SETUP ######

pygame.init()

screenInfo = pygame.display.Info()
screenWidth = screenInfo.current_w
screenHeight = screenInfo.current_h

windowSize = (screenWidth, screenHeight)

pygame.display.set_caption("Visual Autonomous") # Sets title of window
screen = pygame.display.set_mode(windowSize, pygame.FULLSCREEN) # Sets the dimensions of the window to the windowSize

###### INITIALIZE ######

fps = 60
clock = pygame.time.Clock()

###### OBJECTS ######

###### MAINLOOP ######

running = True # Runs the game loop
while running:
    screen.fill((30, 30, 37))

    for event in pygame.event.get(): # checks if program is quit, if so stops the code
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
    # runs framerate wait time
    clock.tick(fps)
    # update the screen
    pygame.display.update()

# quit Pygame
pygame.quit()