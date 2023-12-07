import pygame
from Network import Network
from Ball import Ball

width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("XtremePingPong")

clientNumber = 0


def redrawWindow(win, player, player2):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    ball.draw(win)
    pygame.display.update()


ball = Ball(width // 2, height // 2, 5, (255, 255, 255))


def main():
    run = True
    netw = Network()
    p = netw.getPlayer()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = netw.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move(height)
        ball.move(width,height, p)
        redrawWindow(win, p, p2)


main()
