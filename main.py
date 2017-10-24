import pygame as pg


def inicio():
    pg.init()
    pg.display.set_caption("teste pygame")
    tela = pg.display.set_mode([300, 300])
    sair = False
    cor = (255, 255, 255)
    azul = (0, 0, 255)
    verde = (0, 255, 0)
    relogio = pg.time.Clock()
    sup = pg.Surface((200, 200))
    sup.fill(azul)

    sup2 = pg.Surface((100, 100))
    sup2.fill(verde)
    while sair != True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sair = True
        relogio.tick(30)
        tela.fill(cor)
        tela.blit(sup, [50, 50])
        tela.blit(sup2, [100, 100])
        pg.display.update()


    pg.quit()

inicio()


