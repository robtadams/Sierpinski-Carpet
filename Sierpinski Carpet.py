"""
Sierpinski_Carpet.py
Robin Adams
3/4/2024
"""

import pygame

def main():

    # Initialize Pygame
    pygame.init()

    # sWidth: the width of the user's monitor, in pixels
    sWidth  = pygame.display.Info().current_w

    # sHeight: the height of the user's monitor, in pixels
    sHeight = pygame.display.Info().current_h

    # tempWidth: temporary variable that holds 1/3 of sWidth, rounded 
    tempWidth = sWidth // 3

    # tempHeight: temporary variable that holds 1/3 of sHeight, rounded
    tempHeight = sHeight // 3

    # If tempWidth is greater than tempHeight...
    if tempWidth > tempHeight:

        # ... set the size of the carpet to be 3x the smaller side
        carpetLength = tempHeight * 3

    # If tempHeight is greater than or equal to tempWidth...
    else:

        # ... set the size of the carpet to be 3x the smaller side
        carpetLength = tempWidth * 3

    # screen: the pygame window, set to the monitor's width and height
    screen = pygame.display.set_mode((carpetLength, carpetLength))

    # carpetColor: the color to draw the carpet
    carpetColor = (0, 255, 155)

    # clock: the pygame Clock
    clock = pygame.time.Clock()

    # running: keeps track of whether the program should run
    running = True

    screen.fill("black")
    pygame.display.flip()
    sierpinskiCarpet(screen, carpetColor, carpetLength)

    pygame.quit()

def sierpinskiCarpet(screen, carpetColor, carpetLength):
    recursiveCarpet(screen, carpetColor, [0, 0], [carpetLength, carpetLength])
    
def recursiveCarpet(screen, carpetColor, startCoord, endCoord):

    startX, startY = startCoord
    endX, endY = endCoord

    pygame.draw.rect(screen, carpetColor, pygame.Rect(startX, startY, endX, endY))
    pygame.display.flip()

    oneX, oneY = [endX // 3, endY // 3]
    twoX, twoY = [2 * endX // 3, 2 * endY // 3]

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(oneX, oneY, twoX - oneX, twoY - oneY))
    pygame.display.flip()

main()
