#imports pygame
import pygame
                

pygame.init()

#displays pygame screen
screen = pygame.display.set_mode([225, 150])

r = pygame.Color("red")
w = pygame.Colour("white")

#creates the whole image
data = [
    [ w, w, r, r, r, r, r, w, w ],
    [ w, w, r, w, r, w, r, w, w ],
    [ w, w, r, r, r, r, r, w, w ],
    [ w, r, r, r, w, r, r, r, w ],
    [ r, w, w, r, r, r, w, w, r ],
    [ r, r, w, w, w, w, w, r, r ],
    ]

#rectangle
for y, row in enumerate(data):
    for x, colour in enumerate(row):
        rect = pygame.Rect(x*25, y*25, 25, 25)
        screen.fill(colour, rect=rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
