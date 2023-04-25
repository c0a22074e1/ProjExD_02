import pygame as pg
import random
import sys
import time


delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT:(+1, 0)
}  # 練習4


"""kaiten = {
    pg.K_UP: (0, -1),
    pg.K_UP and pg.K_RIGHT: (+1, -1),
    pg.K_RIGHT: (+1, 0),
    pg.K_DOWN and pg.K_RIGHT: (+1, +1),
    pg.K_DOWN: (0, -1),
    pg.K_DOWN and pg.K_LEFT: (-1, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_UP and pg.K_LEFT: (-1, -1),
}  # 追加課題１"""




def check_bound(scr_rect, obj_rect) -> tuple[bool, bool]:  # 練習5
    """
    オブジェクトが画面内、画面外を判定し、真理値タプルを表す関数
    引数1、画面SurfaceのRect
    引数2、こうかとん、または、爆弾SurfaceのRect
    戻り値:横方向、縦方向のはみ出し判定結果（画面内:True / 画面外；False）
    """
    yoko, tate = True, True
    if obj_rect.left < scr_rect.left or scr_rect.right < obj_rect.right:  # 練習5
        yoko = False  # 練習5
    if obj_rect.top < scr_rect.top or scr_rect.bottom < obj_rect.bottom:  # 練習5
        tate = False  # 練習5
    return yoko, tate  # 練習5


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_lose_img = pg.image.load("ex02/fig/9.png")  # 追加課題３
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()  # 練習4
    kk_rect.center = (900, 400)  # 練習4

    bb_img = pg.Surface((20, 20))  # 練習1
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_img.set_colorkey((0, 0, 0))  # 練習1
    x, y = random.randint(0, 1600), random.randint(0, 900)  # 練習2
    screen.blit(bb_img, [x, y])  # 練習2
    vx, vy = +1, +1  # 練習3
    bb_rect = bb_img.get_rect()  # 練習3
    bb_rect.center = (x, y)  # 練習3
    tmr = 0

    bb_imgs = []  # 追加課題２
    accs = [a for a in range(1, 11)]
    for r in range(1, 11):
        bb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bb_imgs.append(bb_img)
        bb_img.set_colorkey((0, 0, 0))
    

    


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        if kk_rect.colliderect(bb_rect):  # 練習6
            kk_img = kk_lose_img  # 追加課題３
            screen.blit(bg_img, [0, 0])  # 追加課題３
            screen.blit(kk_img, kk_rect)  # 追加課題３
            pg.display.update()  # 追加課題３
            time.sleep(5)  # 追加課題３
            return  # 練習6

        key_list = pg.key.get_pressed()  # 練習4
        for k, mv in delta.items():  # 練習4
            if key_list[k]:  # 練習4
                kk_rect.move_ip(mv)  # 練習4
        if check_bound(screen.get_rect(), kk_rect) != (True, True):  # 練習5
            for k, mv in delta.items():  # 練習5
                if key_list[k]:  # 練習5
                    kk_rect.move_ip(-mv[0], -mv[1])  # 練習5

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bb_rect.move_ip(vx, vy)  # 練習3
        screen.blit(bb_img, bb_rect)  # 練習3
        yoko, tate = check_bound(screen.get_rect(), bb_rect)  # 練習5
        if not yoko:  # 練習5
            vx *= -1  
        if not tate:  # 練習5
            vy *= -1
        screen.blit(bb_img, bb_rect)  # 練習5
        """if kk_rect.colliderect(bb_rect):  # 練習6
            kk_img = kk_lose_img
            screen.blit(kk_img, kk_rect)
            pg.display.update()
            time.sleep(1)
            return  # 練習6
        
        koukaton_list = pg.key.get_pressed()
        if koukaton_list in kaiten:
            dx, dy = kaiten[event.key]
        image_x += dx * 5
        image_y += dy * 5  # 追加課題１"""

        avs, avy = vx*accs[min(tmr//1000, 9)], vy*accs[min(tmr//1000, 9)]
        bb_img = bb_imgs[min(tmr//1000, 9)]
        bb_rect.move_ip(vx + avs, vy + avy)
        

        pg.display.update()
        clock.tick(1000)

        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()