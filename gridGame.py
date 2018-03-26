"""
    gridGame.py
    November 2nd, 2016

    Program which records player's
    mouse position and reacts accordingly
"""

import pygame, random

def drawGrid(background, screen):
    """Draw grid in which the player will be able to click"""
    x = 0
    y = 0
    while x <= 400:
        pygame.draw.line(background, (0,0,0), (x, y), (x, 400))
        x += 40
    x = 0
    while y <= 400:
        pygame.draw.line(background, (0,0,0), (x, y), (400, y))
        y += 40

def clickedItem(mouseX, mouseY, pos, characters):
    names = ["Archibald", "Wesley", "Renald", "Leonard", "Simmons", "Magic Cauldron"]
    descriptions = ["Always has been seen as unstable but wit.",
                    "Good leader, but terrible friend.",
                    "Village's farmer.",
                    "Dedicated salesman.",
                    "Keeper of the magic cauldron.",
                    "It's magic. Need I say more?"]
    myFont = pygame.font.SysFont("None", 20)
    x = ((mouseX / 40) * 40) + 1
    y = ((mouseY / 40) * 40) + 1
    selected = False
    nameLabel = myFont.render("", 1, (0, 0, 0))
    descriptionLabel = myFont.render("", 1, (0, 0, 0))
    image = characters[0]

    i = 0
    while i < 6:
        if(x, y) == pos[i]:
            image = characters[i + 6]
            nameLabel = myFont.render(names[i], 1, (0, 0, 0))
            descriptionLabel = myFont.render(descriptions[i], 1, (0, 0, 0))
            selected = True           
        i += 1

    return image, nameLabel, descriptionLabel, selected

def main():
    """Game in which player gets to click in a grid and
       get information back if object is in square"""
    pygame.init()
    screen = pygame.display.set_mode((401, 640))
    pygame.display.set_caption("Grid Game")

    #Create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    #create elements
    highlight = pygame.Surface((39, 39))
    highlight = highlight.convert()
    highlight.fill((255, 255, 153))

    sign = pygame.image.load("woodenSign.jpg")
    sign = sign.convert()

    characters = []
    characters.append(pygame.image.load("archibaldSmall.png"))
    characters.append(pygame.image.load("wesleySmall.png"))
    characters.append(pygame.image.load("renaldSmall.png"))
    characters.append(pygame.image.load("leonardSmall.png"))
    characters.append(pygame.image.load("simmonsSmall.png"))
    characters.append(pygame.image.load("magicCauldronSmall.png"))
    characters.append(pygame.image.load("archibaldBig.png"))
    characters.append(pygame.image.load("wesleyBig.png"))
    characters.append(pygame.image.load("renaldBig.png"))
    characters.append(pygame.image.load("leonardBig.png"))
    characters.append(pygame.image.load("simmonsBig.png"))
    characters.append(pygame.image.load("magicCauldronBig.png"))
    i = 0
    while i < 12:
        characters[i] = characters[i].convert()
        characters[i].set_colorkey((255, 255, 255))
        i += 1

    labels = []

    #create variables
    mouseX = 0
    mouseY = 0
    selected = False

    pos = []
    i = 0
    while i < 6:
        pos.append((((random.randrange(0, 400) / 40) * 40) + 1, ((random.randrange(0, 400) / 40) * 40) + 1))
        i += 1

    clock = pygame.time.Clock()
    keepGoing = True
    #game loop
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            #close window
            if event.type == pygame.QUIT:
                keepGoing = False
            #record mouse position
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = pygame.mouse.get_pos()
                #record mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                profile, nameLabel, descrLabel, selected = clickedItem(mouseX, mouseY, pos, characters)
                
                
        drawGrid(background, screen)

        #reset screen
        screen.blit(background, (0, 0))
        if mouseY < 400:
            screen.blit(highlight, ((mouseX/40 * 40) + 1, (mouseY/40 * 40) + 1))
        i = 0
        while i < 6:
            screen.blit(characters[i], (pos[i]))
            i += 1
        screen.blit(sign, (0, 401))
        if selected == True:
            screen.blit(profile, (250, 480))
            screen.blit(nameLabel, (110, 410))
            screen.blit(descrLabel, (110, 430))
        pygame.display.flip()
        
    pygame.quit()

#starts game
if __name__ == "__main__":
    main()
