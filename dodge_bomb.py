import pygame as pg
import random
import sys


delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT:(+1, 0)
}  # 4


def check_bound(scr_rect, obj_rect) -> tuple[bool, bool]:  # 5
    """
    オブジェクトが画面内、画面外を判定し、真理値タプルを表す関数
    引数1、画面SurfaceのRect
    引数2、こうかとん、または、爆弾SurfaceのRect
    戻り値:横方向、縦方向のはみ出し判定結果（画面内:True / 画面外；False）
    """
    yoko, tate = True, True
    if obj_rect.left < scr_rect.left or scr_rect.right < obj_rect.right:
        yoko = False
    if obj_rect.top < scr_rect.top or scr_rect.bottom < obj_rect.bottom:
        tate = False
    return yoko, tate  # 5


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()  # 4
    kk_rect.center = (900, 400)  # 4

    bb_img = pg.Surface((20, 20))  # 練習1
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_img.set_colorkey((0, 0, 0))  # 練習1
    x, y = random.randint(0, 1600), random.randint(0, 900)  # 2
    screen.blit(bb_img, [x, y])  # 2
    vx, vy = +1, +1  # 3
    bb_rect = bb_img.get_rect()  # 3
    bb_rect.center = (x, y)  # 3
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_list = pg.key.get_pressed()
        for k, mv in delta.items():  # 4
            if key_list[k]:  # 4
                kk_rect.move_ip(mv)  # 4
        if check_bound(screen.get_rect(), kk_rect) != (True, True):  # 5
            for k, mv in delta.items():  # 5
                if key_list[k]:  # 5
                    kk_rect.move_ip(-mv[0], -mv[1])  # 5

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bb_rect.move_ip(vx, vy)  # 3
        screen.blit(bb_img, bb_rect)  # 3
        yoko, tate = check_bound(screen.get_rect(), bb_rect)  # 5
        if not yoko:  # 5
            vx *= -1  
        if not tate:  # 5
            vy *= -1
        screen.blit(bb_img, bb_rect)  # 5

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()