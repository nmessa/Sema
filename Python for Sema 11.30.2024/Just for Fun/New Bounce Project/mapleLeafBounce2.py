import pygame, sys
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

#create sound
theSound = pygame.mixer.Sound("COW_BELL.ogg")

dots = [[221,432], [225,331], [133,342], [141,310],
        [51,230], [74,217], [58,153], [114,164],
        [123,135], [176,190], [159,77], [193,93],
        [230,28], [267,93], [301,77], [284,190],
        [327,135], [336,164], [402,153], [386,217],
        [409,230], [319,310], [327,342], [233,331],
        [237,432]]

dx = 1
dy = 1

screen = pygame.display.set_mode([800,650])
screen.fill([255,255,255])

pygame.draw.lines(screen, [255,0,0], True, dots, 2)
pygame.display.flip()

while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    for i in range(len(dots)):
        if dots[i][0] > screen.get_width() or dots[i][0] < 0:
            dx = -dx
            theSound.play()
            break

        if dots[i][1] > screen.get_height() or dots[i][1] < 0:
            dy = -dy
            theSound.play()
            break
    for i in range(len(dots)):
        dots[i][0] += dx
        dots[i][1] += dy

    screen.fill([255,255,255])
    pygame.draw.lines(screen, [255,0,0], True, dots, 2)
    pygame.display.flip()
    
