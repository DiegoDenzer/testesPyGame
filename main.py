import pygame as pg
import constantes as c

def inicio():
    pg.init()
    pg.display.set_caption("teste pygame")
    tela = pg.display.set_mode([300, 300])
    sair = False
    ret = pg.Rect(10,10, 45, 45)

    ret2 = pg.Rect(10, 100, 230, 60)

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
                pg.mouse.set_pos(150,150)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    ret.move_ip(5,0)

                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    ret.move_ip(-5,0)

                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    ret.move_ip(0, 5)

                if event.key == pg.K_UP or event.key == pg.K_w:
                    ret.move_ip(0, -5)

        (ret.left, ret.top) = pg.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2

        relogio.tick(30)
        tela.fill(c.FUNDO_BRANCO)
        tela.blit(sup2, [100, 100])
        pg.draw.rect(tela, c.VERMELHO, ret)
        pg.draw.rect(tela, c.AZUL, ret2)
        pg.display.update()


    pg.quit()

inicio()


