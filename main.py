from random import randrange

import pygame as pg
import constantes as c

def inicio():
    pg.init()
    pg.display.set_caption("teste pygame")
    tela = pg.display.set_mode([300, 300])
    sair = False
    ret = pg.Rect(10,10, 30, 30)

    #                posx , posy, largura, altura
    barra1 = pg.Rect(100, 250, randrange(0, 100), randrange(0, 150))
    barra2 = pg.Rect(200, 200, randrange(0, 100), randrange(0, 150))

    relogio = pg.time.Clock()

    #texto
    font_padrao = pg.font.get_default_font()
    font_perdeu = pg.font.SysFont(font_padrao, 45)

    pg.font.init()

    sup = pg.Surface((300, 30))
    sup.fill(c.VERDE)
    #sup2 = pg.Surface((100, 100))
    #sup2.fill(c.VERDE)

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

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pg.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2



        if ret.colliderect(barra1):
            print('barra1')
            titulo = font_perdeu.render('teste', 1, c.AZUL)
            tela.blit(titulo, (120, 0))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(barra2):
            print('barra2')
            text = font_perdeu.render('bateu', 1, c.VERMELHO)
            tela.blit(text, (100, 100))
            (ret.left, ret.top) = (xant, yant)

        relogio.tick(30)
        tela.fill(c.BRANCO)
        tela.blit(sup, [0, 0])
        titulo = font_perdeu.render('teste', 1, c.AZUL)
        tela.blit(titulo, (120, 0))
        sup.blit(titulo, (120,0))
        pg.draw.rect(tela, c.VERMELHO, ret)
        pg.draw.rect(tela, c.AZUL, barra1)
        pg.draw.rect(tela, c.VERDE, barra2)
        pg.display.update()


    pg.quit()

inicio()


