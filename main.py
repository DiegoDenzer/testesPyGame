from random import randrange

import pygame as pg
import constantes as c

def inicio():
    pg.init()
    pg.display.set_caption("teste pygame")
    tela = pg.display.set_mode([600, 200])
    sair = False
    ret = pg.Rect(10, 10, 10, 10)


    #  posx , posy, largura, altura
    y=0
    x = 50

    listaBarra = []

    for item in range(0, 11):
        item = pg.Rect(x, 0, 10, 20)
        listaBarra.append(item)
                   
        item = pg.Rect(x, x, 10, 200 - x)
        listaBarra.append(item)
        x = x + 50

    relogio = pg.time.Clock()

    #texto
    font_padrao = pg.font.get_default_font()
    font_perdeu = pg.font.SysFont(font_padrao, 45)

    pg.font.init()

    sup = pg.Surface((300, 30))
    sup.fill(c.VERDE)

    while sair != True:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                sair = True

            if event.type == pg.MOUSEBUTTONDOWN:
                pg.mouse.set_pos(150,150)
                ret = ret.inflate(20,20)


        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pg.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2


        for item in listaBarra:


            if ret.colliderect(item):

                (ret.left, ret.top) = (xant, yant)





        relogio.tick(30)
        tela.fill(c.BRANCO)

        titulo = font_perdeu.render('teste', 1, c.AZUL)

        for item in listaBarra:
            pg.draw.rect(tela, c.AZUL, item)

        pg.draw.rect(tela, c.VERMELHO, ret)






        pg.display.update()


    pg.quit()

inicio()


