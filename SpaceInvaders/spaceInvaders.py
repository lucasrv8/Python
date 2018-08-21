import pygame 
from random import randint

#Global variables
width = 600
height = 500
tam = 20
XBullet = 0
YBullet = 0
listBullet = []
cont = 0

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)

try:
    pygame.init()
except:
    print("Error")

screenGame = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

def SpaceShip(pos_x, pos_y):
    i = pygame.image.load("ship.png")
    i = pygame.transform.scale(i,(47,47))
    screenGame.blit(i, [pos_x - 20,pos_y-20])
    #pygame.draw.rect(screenGame, black, [pos_x,pos_y, tam, tam])

def fire():
    global XBullet
    global YBullet
    #i =  pygame.image.load("bullet.png")
    #i = pygame.transform.scale(i,(15,15))
    #screenGame.blit(i, [XBullet, YBullet])
    pygame.draw.rect(screenGame, yellow, [int(XBullet), YBullet, 2, 5])
    return [XBullet, YBullet]

def moveBullet():
    global cont
    global XBullet
    global YBullet
    for i in range(cont):
        print(listBullet[i])
        print(listBullet[i])
        a, b = listBullet[i]
        b -= 5
        XBullet = a
        YBullet = b
        listBullet[i] = [a,YBullet] 
        fire()

def game():
    #screen = pygame.display.set_mode((width, height))
    gameOn = True
    spaceShipX = width/2
    spaceShipY = height - 50
    speedX = 0
    speedY = 0
    tick = 1
    global XBullet
    global YBullet
    global cont
    i = 0
    cont = 0
    global listBullet
    #bulletX = spaceShipX
    #bulletY = spaceShipY
    fireDispared = 0
    while gameOn:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            spaceShipX -= 5
        if pressed_keys[pygame.K_RIGHT]:
            spaceShipX += 5
        if pressed_keys[pygame.K_SPACE]:
            quant_bullets = 1
            if quant_bullets == 1:
                if not tick:
                    tick = 1 
                    XBullet = (spaceShipX+3)
                    YBullet = spaceShipY
                    listBullet.insert(0,fire())
                    cont += 1
                    fireDispared = 1
                else:
                    tick -= 1
            quant_bullets = 0
            moveBullet()
            pygame.display.update()    
        pygame.display.update()
        if gameOn:
            screenGame.fill(black)    
            if spaceShipX < 0:
                spaceShipX = 0
            if spaceShipX + tam > width:
                spaceShipX = (width - tam)
            moveBullet()
                #pygame.display.flip()
            #fireDispared = 0
            SpaceShip(spaceShipX, spaceShipY)
            
            pygame.display.update()
        clock.tick(30)
        pygame.display.update()
#principal
game()