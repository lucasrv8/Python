import pygame
from random import randrange
from pygame.mixer import Sound

#Tamanho da janela
tamLargura = 320
tamAltura = 240
tam = 10
mode = 0


#cores 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
lightGray = (205,205,205)
pink = (255,0,255)
lightblue = (8,178,232)
gold = (217,217,25)
purple = (180,12,232)

try: 
    pygame.init() #Inicia a janela
except:
    print("Erro ao iniciar o pygame")
tela = pygame.display.set_mode((tamLargura, tamAltura)) #Desenha a caixa de visualização
pygame.display.set_caption("Snake", "icon2.") #Serve para dar nome a janela e o icone
clock = pygame.time.Clock() #É um relogio que vai ajudar na limitação de FPS devido ao fato da velocidade estar alta
pygame.mixer.init() #inicia o mixer
#pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.init()
playSound = pygame.mixer.Sound("mordida.wav") #Carrega a musica
playSoundGameOver = pygame.mixer.Sound("GameOver.wav")

def text(msg, color, tamTxt, widthX, heightY):
    font = pygame.font.SysFont(None, tamTxt) #Atribui a uma variavel uma determinada font e tamanho dela 
    textmsg = font.render(msg, True, color) #Função render aplica a cor, o antialising e o background a menssagem
    tela.blit(textmsg, [widthX, heightY]) #Função blit coloca a menssagem no lugar em que deseja aparecer passando a menssagem e a posição

def snake(snakeBody):
    for i in snakeBody:
        pygame.draw.rect(tela,lightblue, [i[0],i[1],tam,tam]) #Desenha no display, primeiro argumento é onde vai ser desenhado, segundo é a cor, e depois as posições sendo um conjudo em um terceiro argumento só
        pygame.draw.rect(tela,black, [i[0],i[1],1,tam])
        pygame.draw.rect(tela,black, [i[0],i[1],tam,1])

def apple(appleX, appleY):
    pygame.draw.rect(tela, red, [appleX,appleY, tam, tam])

def appleDeath(appleOverX, appleOverY):
    pygame.draw.rect(tela, green, [appleOverX,appleOverY, tam, tam])

def appleBonus(appleBonusX, appleBonusY):
    pygame.draw.rect(tela, gold, [appleBonusX, appleBonusY, tam*2, tam*2])

def appleRandom(appleRandomX, appleRandomY):
    pygame.draw.rect(tela, purple, [appleRandomX, appleRandomY, tam, tam])        

def selectMode():
    typeMode = True
    screenMode = pygame.display.set_mode((tamLargura, tamAltura))
    screenMode.fill(lightGray)
    text("Select mode", black, 50, 50, 30)
    pygame.draw.rect(tela, black, [80, 70, 135, 40])
    text("Easy(E)", white, 45, 95, 75)
    pygame.draw.rect(tela, black, [80, 130, 135, 40])
    text("Medium(M)", white, 35, 85, 138)
    pygame.draw.rect(tela, black, [80, 190, 135, 40])
    text("Hard(H)", white, 45, 95, 195)
    while typeMode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1 = pygame.mouse.get_pos()[0]
                y1 = pygame.mouse.get_pos()[1]
                if x1 > 80 and y1 > 70 and x1 < 215 and y1 < 110:
                    return 0
                if x1 > 80 and y1 > 130 and x1 < 215 and y1 < 170:
                    return 1
                if x1 > 80 and y1 > 190 and x1 < 215 and y1 < 230:
                    return 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return 0
                if event.key == pygame.K_m:
                    return 1
                if event.key == pyame.K_h:
                    return 2
        pygame.display.update()

def game():
    snakeX = randrange(10,(tamLargura - 10) - tam,10) #Posição no eixo X de onde a cobra está
    snakeY = randrange(30,(tamAltura - 10) - tam,10) #Posição no eixo Y de onde a cobra está
    appleX = randrange(10,(tamLargura - 10) - tam,10) #Posição no eixo X de onde a maça está
    appleY = randrange(30,(tamAltura - 10) - tam,10) #Posição no eixo y de onde a maça está
    appleOverX = randrange(10,(tamLargura - 10) - tam,10)
    appleOverY = randrange(30,(tamAltura - 10) - tam,10)
    appleBonusX = randrange(10,(tamLargura - 10) - tam,10)
    applebonusY = randrange(30,(tamAltura - 10) - tam,10)
    appleRandomX = randrange(10,(tamLargura - 10) - tam,10)
    appleRandomY = randrange(30,(tamAltura - 10) - tam,10)
    speedX = 0
    speedY = 0
    snakeBody = [] #Corpo da cobra
    snakeLen = 1 #Tamanho da cobra
    score = 0
    listAppleDeath = []
    listAppleGold = []
    listAppleRandom = []
    global mode

    for value in range(7): #Escolhe números aleatórios iniciais para a maça verde
        valueRand = randrange(0, 100)
        listAppleDeath.insert(0,valueRand)
        valueRand = randrange(0, 100)
        listAppleGold.insert(0,valueRand)
        valueRand = randrange(0,100)
        listAppleRandom.insert(0,valueRand)
        #print(valueRand)
    jogoOn = True
    gameOver = False
    gameWin = 0
    while jogoOn:
        while gameOver:
            for event in pygame.event.get(): #Pega os eventos da tela
                if event.type == pygame.QUIT:
                    jogoOn = False
                    gameOver = False
                #Interação com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 90 and y > 115 and x < 235 and y < 142:
                        snakeX = randrange(10,(tamLargura - 10) - tam,10)
                        snakeY = randrange(30,(tamAltura - 10) - tam,10)
                        appleX = randrange(10,(tamLargura - 10) - tam,10)
                        appleY = randrange(30,(tamAltura - 10) - tam,10)
                        speedX = 0
                        speedY = 0
                        snakeBody = []  #Corpo da cobra
                        snakeLen = 1
                        score = 0
                        gameWin = 0
                        for value in range(7): #Escolhe outros números aleatórios para a maça verde
                            valueRand = randrange(0, 100)
                            listAppleDeath[value] = valueRand
                            valueRand = randrange(0, 100)
                            listAppleGold[value] = valueRand
                            valueRand = randrange(0,100)
                            listAppleRandom.insert(0,valueRand)
                        jogoOn = True
                        gameOver = False
                    if x > 110 and y > 150 and x < 205 and y < 177:
                        mode = selectMode()
                    if x > 120 and y > 190 and x < 195 and y < 217:
                        jogoOn = False
                        gameOver = False
                #Interação com o teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c or event.key == pygame.K_n:
                        snakeX = randrange(10,(tamLargura -10)- tam,10)
                        snakeY = randrange(30,(tamAltura - 10) - tam,10)
                        appleX = randrange(10,(tamLargura -10) - tam,10)
                        appleY = randrange(30,(tamAltura - 10) - tam,10)
                        speedX = 0
                        speedY = 0
                        snakeBody = []  #Corpo da cobra
                        snakeLen = 1
                        score = 0
                        gameWin = 0
                        for value in range(7): #Escolhe outros números aleatórios para a maça verde
                            valueRand = randrange(0, 100)
                            listAppleDeath[value] = valueRand
                            valueRand = randrange(0, 100)
                            listAppleGold[value] = valueRand
                            valueRand = randrange(0,100)
                            listAppleRandom.insert(0,valueRand)
                        jogoOn = True
                        gameOver = False  
                    if event.key == pygame.K_m:
                        mode = selectMode()
                    if event.key == pygame.K_e:
                        jogoOn = False
                        gameOver = False
            if gameWin == 0:
                tela.fill(red)
                text("GAME OVER", black, 50, 60, 30)
                text("Score: " + str(score), black, 30, 120, 80)
                pygame.draw.rect(tela, black, [90,115,135,27])
                text("Continue(C)", white, 30, 98, 120)
                pygame.draw.rect(tela, black, [110, 150, 95, 27])
                text("Mode(M)", white, 30, 115, 155)
                pygame.draw.rect(tela, black, [120, 190, 75, 27])
                text("Exit(E)", white, 30, 125, 195)
            else:
                tela.fill(green)
                text("CONGRATULATIONS!", black, 40, 10, 30)
                text("Score: 100", black, 30, 120, 80)
                pygame.draw.rect(tela, black, [90,115,145,27])
                text("New Game(N)", white, 30, 98, 120)
                pygame.draw.rect(tela, black, [110, 150, 95, 27])
                text("Mode(M)", white, 30, 115, 155)
                pygame.draw.rect(tela, black, [120, 190, 75, 27])
                text("Exit(E)", white, 30, 125, 195)
            pygame.display.update()
        for event in pygame.event.get(): #Pega os eventos da tela
            if event.type == pygame.QUIT: #Fechar o jogo caso o x seja apertado
                jogoOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and speedX != tam:
                    speedY = 0
                    speedX = - tam
                    break
                if event.key == pygame.K_RIGHT and speedX != -tam:
                    speedY = 0
                    speedX = tam
                    break
                if event.key == pygame.K_UP and speedY != tam:
                    speedY = - tam
                    speedX = 0
                    break
                if event.key == pygame.K_DOWN and speedY != -tam:
                    speedY = tam
                    speedX = 0
                    break
                if event.key == pygame.K_p:
                    gameOver = True
                if event.key == pygame.K_o:
                    score += 49
                    snakeLen += 49
                if event.key == pygame.K_k:
                    half = int(snakeLen / 2)
                    for valueRm in range(half):
                        rm = snakeBody[valueRm]
                        snakeBody.remove(rm)
                    snakeLen -= half
                    if (snakeLen - 1) <= 0:
                        snakeLen = 1
                if event.key == pygame.K_a:
                    print("-----")
                    print(snakeX)
                    print(snakeY)
                    print("a")
                    print(appleX)
                    print(appleY)
                    print("-----")
                #Problema com o botão de pause, só funcianda quando existe apenas a cabeça da cobra
                if event.key == pygame.K_m:
                    pause = snakeLen-1 
                    ini = 0
                    while ini != pause:
                        speedX = 0
                        speedY = 0
                        ini += 1
                        print(ini)
            #print(event)
        #Loop principal de funcionamento do jogo
        if jogoOn:  #Serve para não executar nada caso o jogo termine
            tela.fill(black) #Fill serve para dar cor
            pygame.mixer.music.set_volume(1)
            pygame.draw.rect(tela, lightblue, [10,27, 300, 3]) #Barra superior
            pygame.draw.rect(tela, lightblue, [7,27, 3, 205]) #Barra esquerda
            pygame.draw.rect(tela, lightblue, [7,230, 306, 3]) #Barra inferior
            pygame.draw.rect(tela, lightblue, [310,27, 3, 205]) #Barra direita
            snakeX = snakeX + speedX
            snakeY = snakeY + speedY
            text("Score: " + str(score), white, 30, 5,5)
            #Dificuldades
            #Fácil
            if mode == 0:
                if snakeX + tam > tamLargura-10:
                    snakeX = 10
                if snakeX < 10:
                    snakeX = (tamLargura - 10)- tam
                if snakeY + tam > (tamAltura - 10):
                    snakeY = 30
                if snakeY < 30:
                    snakeY = (tamAltura - 10) - tam
            #Médio e dificíl
            if mode == 1 or mode == 2:
                if snakeX + tam > (tamLargura - 10):
                    playSoundGameOver.play()
                    gameOver = True
                if snakeX < 10:
                    playSoundGameOver.play()
                    gameOver = True
                if snakeY + tam > tamAltura - 10:
                    playSoundGameOver.play()
                    gameOver = True
                if snakeY < 30:
                    playSoundGameOver.play()
                    gameOver = True
            #Maçãs que pontuam e tbm redefinem as posições das outras maçãs
            if snakeX == appleX and snakeY == appleY:
                playSound.play()
                possibleX = randrange(10,(tamLargura - 10) - tam,10)
                possibleY = randrange(30,(tamAltura - 10) - tam,10)
                possibleXY = [possibleX, possibleY]
                i = snakeLen -1
                while i >= 0:
                    if possibleXY == snakeBody[i]:
                        possibleX = randrange(10,(tamLargura - 10) - tam,10)
                        possibleY = randrange(30,(tamAltura - 10) - tam,10)
                        possibleXY = [possibleX, possibleY]
                        i = snakeLen - 1
                    i -= 1
                appleX = possibleX
                appleY = possibleY
                snakeLen += 1
                score += 1
                #pygame.mixer.music.play(1, 0.1)
                appleOverX = randrange(10,(tamLargura - 10) - tam,10)
                appleOverY = randrange(30,(tamAltura - 10) - tam,10) 
                appleBonusX = randrange(10,(tamLargura - 10) - tam,10)
                applebonusY = randrange(30,(tamAltura - 10) - tam,10)
                appleRandomX = randrange(10,(tamLargura - 10) - tam,10)
                appleRandomY = randrange(30,(tamAltura - 10) - tam,10)
            #Maçãs que causam o fim do jogo
            if score == listAppleDeath[0] or score == listAppleDeath[1] or score == listAppleDeath[2] or score == listAppleDeath[3] or score == listAppleDeath[4] or score == listAppleDeath[5] or score == listAppleDeath[6]:
                if snakeX == appleOverX and snakeY == appleOverY:
                    #pygame.mixer.music.play() #Inicia a reprodução da musica carregada
                    playSoundGameOver.play()
                    gameOver = True
            #Maçãs que dão um bonus de crescimento de + 3
            if score == listAppleGold[0] or score == listAppleGold[1] or score == listAppleGold[2] or score == listAppleGold[3] or score == listAppleGold[4] or score == listAppleGold[5] or score == listAppleGold[6]:
                if (snakeX == appleBonusX and snakeY == applebonusY) or (snakeX == (appleBonusX + 10) and snakeY == (applebonusY + 10)) or (snakeX == (appleBonusX) and snakeY == (applebonusY + 10)) or (snakeX == (appleBonusX + 10) and snakeY == (applebonusY)):
                    #pygame.mixer.music.play()
                    playSound.play()                    
                    snakeLen += 3
                    score += 3
            #Maças random
            if score == listAppleRandom[0] or score == listAppleRandom[1] or score == listAppleRandom[2] or score == listAppleRandom[3] or score == listAppleRandom[4] or score == listAppleRandom[5] or score == listAppleRandom[6]:
                if snakeX == appleRandomX and snakeY == appleRandomY:
                    #pygame.mixer.music.play()
                    playSound.play()
                    whatApple = randrange(0,100)
                    #print(whatApple)
                    if whatApple >= 0 and whatApple < 55: #55% de chance ganhar 6 pontos. obs: aumenta a cobra
                        snakeLen += 6
                        score += 6
                    elif whatApple >= 55 and whatApple < 75: #20% de chance perder 8 pontos, mas não diminui a cobra
                        score -= 8
                        if score <= 0:
                            score = 0
                    elif whatApple >= 75 and whatApple < 90: #15% de chance para diminuir a cobra ao meio, e não a pontuação
                        half = int(snakeLen / 2)
                        for valueRm in range(half):
                            rm = snakeBody[valueRm]
                            snakeBody.remove(rm)
                        snakeLen -= half
                        if (snakeLen - 1) <= 0:
                            snakeLen = 1
                    elif whatApple >= 90 and whatApple <= 99: #9% de chance de perder o jogo
                        gameOver = True
                    elif whatApple == 100: #1% de chance de ganhar o jogo
                        gameOver = True
                        gameWin = 1
                    else:
                        print("erro" + str(whatApple))   
            snakeHead = []  #cabeça da cobra
            snakeHead.append(snakeX)
            snakeHead.append(snakeY)
            snakeBody.append(snakeHead)
            if len(snakeBody) > snakeLen: #Condição para a cobra não crescer infinitamente
                    del snakeBody[0]
            if any(Bloc == snakeHead for Bloc in snakeBody[:-1]): #Condição para dar game over quando a cobra bater nela mesmo
                playSoundGameOver.play()
                gameOver = True
            snake(snakeBody)
            apple(appleX, appleY)
            if score == listAppleDeath[0] or score == listAppleDeath[1] or score == listAppleDeath[2] or score == listAppleDeath[3] or score == listAppleDeath[4] or score == listAppleDeath[5] or score == listAppleDeath[6]:
                appleDeath(appleOverX, appleOverY)
            if score == listAppleGold[0] or score == listAppleGold[1] or score == listAppleGold[2] or score == listAppleGold[3] or score == listAppleGold[4] or score == listAppleGold[5] or score == listAppleGold[6]:
                appleBonus(appleBonusX, applebonusY)
            if score == listAppleRandom[0] or score == listAppleRandom[1] or score == listAppleRandom[2] or score == listAppleRandom[3] or score == listAppleRandom[4] or score == listAppleRandom[5] or score == listAppleRandom[6]:
                appleRandom(appleRandomX, appleRandomY)
            if score >= 100:
                gameOver = True
                gameWin = 1
            if mode == 0 or mode == 1:
                clock.tick(15)
            else:
                clock.tick(25)
            pygame.display.update() #Atualiza o display todo, mas tbm pode atualizar somente pontos especificos se passar os paramentros corretos

#Função Principal
#Tela inicial
start = True
inicio = pygame.display.set_mode((tamLargura, tamAltura))
inicio.fill(black)
pygame.draw.rect(tela, blue, [70,100,180,60])
text("Start", white, 60, 105, 110)
text("Snake Game", green, 50, 60, 30)
while start:
    for event in pygame.event.get(): #Pega os eventos da tela
        if event.type == pygame.QUIT:
                pygame.quit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                start = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if x > 80 and y > 80 and x < 230 and y < 160:
                start = False
    pygame.display.update()
#Chama a tela de escolha de dificuldades
mode = selectMode()
#Chama o jogo
game()
#Fecha a janela
pygame.quit() 