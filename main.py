import pygame as pg
import constantes as c

def inicio():
    pg.init()
    pg.display.set_caption("teste pygame")
    tela = pg.display.set_mode([300, 300])
    sair = False
    ret = pg.Rect(10,10, 45, 45)
    relogio = pg.time.Clock()
    sup = pg.Surface((200, 200))
    sup.fill(c.AZUL)
    sup2 = pg.Surface((100, 100))
    sup2.fill(c.VERDE)
    while sair != True:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                sair = True

            if event.type == pg.MOUSEBUTTONDOWN:
                ret = ret.move(100, 100)

            if event.type == pg.MOUSEMOTION:
                ret = ret.move(-10, -10)

        relogio.tick(30)
        tela.fill(c.FUNDO_BRANCO)
       # tela.blit(sup, [50, 50])
        tela.blit(sup2, [100, 100])
        pg.draw.rect(tela, c.VERMELHO, ret)
        pg.display.update()


    pg.quit()

inicio()


