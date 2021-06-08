from random import choice

import pygame as pg

pg.font.init()

win = pg.display.set_mode((900, 500))
Ico = pg.image.load('assets/DinoWallpaper.png')
pg.display.set_icon(Ico)
pg.display.set_caption("Dino_Runner 1.0")
large_cactus1 = pg.transform.scale(pg.image.load("Assets/LargeCactus1.png"), (30, 75))
large_cactus2 = pg.transform.scale(pg.image.load("Assets/LargeCactus2.png"), (60, 75))
large_cactus3 = pg.transform.scale(pg.image.load("Assets/LargeCactus3.png"), (75, 75))
small_cactus1 = pg.transform.scale(pg.image.load("Assets/SmallCactus1.png"), (20, 61))
small_cactus2 = pg.transform.scale(pg.image.load("Assets/SmallCactus2.png"), (60, 61))
small_cactus3 = pg.transform.scale(pg.image.load("Assets/SmallCactus3.png"), (75, 61))
starting_dino = pg.transform.scale(pg.image.load("Assets/DinoRun1.png"), (65, 69))
running_dino1 = pg.transform.scale(pg.image.load("Assets/DinoRun1.png"), (65, 69))
running_dino2 = pg.transform.scale(pg.image.load("Assets/DinoRun2.png"), (65, 69))
jumping_dino = pg.transform.scale(pg.image.load("Assets/DinoJump.png"), (65, 69))
dino_duck1 = pg.transform.scale(pg.image.load("Assets/DinoDuck1.png"),(95,45))
dino_duck2 = pg.transform.scale(pg.image.load("Assets/DinoDuck2.png"),(95,45))
bird1 = pg.transform.scale(pg.image.load("Assets/Bird1.png"),(65,30))
bird2 = pg.transform.scale(pg.image.load("Assets/Bird2.png"),(65,30))
starting_text = pg.font.SysFont("Arial", 30, 1).render("Press Up or Down to Start", 1, "#000000")
ending_text = pg.font.SysFont("Arial", 50, 1).render("Game Over", 1, "#000000")
score_text = pg.font.SysFont("Arial", 18, 1)
track = pg.image.load("Assets/Track.png")
reset_button = pg.image.load("Assets/Reset.png")
background = pg.Rect(0, 0, 900, 500)
val = 0
key = 0
val2 = 0
val3 = 0
x_pos_bg = 0
cloud_image = pg.image.load("Assets/Other/Cloud.png")
cactus_lst = [[large_cactus1,large_cactus1]]
cloud_lst = []
small_cactus_image_lst = [small_cactus1, small_cactus2, small_cactus3]
large_cactus_image_lst = [large_cactus1, large_cactus2, large_cactus3]
bird_lst = [bird1, bird2]
cactus_position_lst = [[800, 207]]
cactus_box = pg.Rect(800, 207, 48, 75)
dino_box = pg.Rect(70, 217, 48, 75)
jump_vel = JUMP_VEL = 7.5
cactus_vel = 4.5
score = 0
val4 = 0
val6 = 0
val5 = 0
JUMP = False
RUN = True
DUCK = False

def move_dino():
    global JUMP, RUN, JUMP_VEL, jump_vel,DUCK, dino_duck1,val6,dino_duck2,dino_box,val5, val4,win, cactus_box, cloud_lst, cloud_image, jumping_dino, val2, cactus_lst, cactus_position_lst, cactus_vel
    if jump_vel < (-1 * JUMP_VEL):
        jump_vel = JUMP_VEL
        JUMP = False
        RUN = True
    if JUMP == True:
        dino_box.y -= jump_vel * 4
        jump_vel -= 0.6
        print(cactus_position_lst)
        cactus_lst = cactus_lst[::-1]
        cactus_position_lst = cactus_position_lst[::-1]
        print(cactus_position_lst)
        for e in range(len(cactus_lst)):
            try:
                a = cactus_position_lst[e][0]
                if a < 22:
                    cactus_box.x = cactus_position_lst[e + 1]
                if a < -100:
                    cactus_position_lst.pop(e)
                    cactus_lst.pop(e)
                else:
                    if cactus_lst[e][0] == bird1:
                        cactus_position_lst[e][0] -= (cactus_vel + 1.8)
                        cactus_box.y = 155
                    else:
                        cactus_position_lst[e][0] -= cactus_vel
                        cactus_box.y = 207
                    cactus_box.x = cactus_position_lst[e][0]
                    if val4 == 40:
                        val4 = 0
                    if val4 <= 20:
                        win.blit(cactus_lst[e][0], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                    else:
                        win.blit(cactus_lst[e][1], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                    val4 += 1
            except:
                pass
        cactus_position_lst = cactus_position_lst[::-1]
        cactus_lst = cactus_lst[::-1]
        for f in range(len(cloud_lst)):
            try:
                cloud_lst[f][0] -= cactus_vel
                win.blit(cloud_image, (cloud_lst[f][0], cloud_lst[f][1]))
            except:
                pass
        win.blit(jumping_dino, (dino_box.x, dino_box.y))
        pg.display.update()
    if RUN == True and JUMP == False:
        dino_box.y = 217
        cactus_lst = cactus_lst[::-1]
        cactus_position_lst = cactus_position_lst[::-1]
        for e in range(len(cactus_lst)):
            try:
                a = cactus_position_lst[e][0]
                if a < 22:
                    cactus_box.x = cactus_position_lst[e + 1]
                if a < -100:
                    print(2)
                    cactus_position_lst.pop(e)
                    cactus_lst.pop(e)
                    pg.display.update()
                else:
                    if cactus_lst[e][0] == bird1:
                        cactus_position_lst[e][0] -= (cactus_vel + 2)
                        cactus_box.y = 155
                    else:
                        cactus_position_lst[e][0] -= cactus_vel
                        cactus_box.y = 207
                    cactus_box.x = cactus_position_lst[e][0]
                    if val4 == 40:
                        val4 = 0
                    if val4 <= 20:
                        win.blit(cactus_lst[e][0], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                    else:
                        win.blit(cactus_lst[e][1], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                    val4 += 1
            except:
                pass
        cactus_position_lst = cactus_position_lst[::-1]
        cactus_lst = cactus_lst[::-1]
        for f in range(len(cloud_lst)):
            try:
                cloud_lst[f][0] -= cactus_vel
                win.blit(cloud_image, (cloud_lst[f][0], cloud_lst[f][1]))
            except:
                pass
        if val2 >= 20:
            val2 = 0
        if val2 % 5 <= 2:
            win.blit(running_dino1, (dino_box.x, dino_box.y))
            pg.display.update()
        if val2 % 5 > 2:
            win.blit(running_dino2, (dino_box.x, dino_box.y))
            pg.display.update()
    if DUCK == True and RUN == False:
        print(val6)
        dino_box.y = 237
        if val6 == 17:
            RUN = True
            DUCK = False
            val6 = 0
        cactus_lst = cactus_lst[::-1]
        cactus_position_lst = cactus_position_lst[::-1]
        for e in range(len(cactus_lst)):
            try:
                a = cactus_position_lst[e][0]
                if a < 22:
                    cactus_box.x = cactus_position_lst[e + 1]
                if a < -100:
                    cactus_position_lst.pop(e)
                    cactus_lst.pop(e)
                    pg.display.update()
                else:
                    if cactus_lst[e][0] == bird1:
                        cactus_position_lst[e][0] -= (cactus_vel + 1.8)
                        cactus_box.y = 155
                    else:
                        cactus_position_lst[e][0] -= cactus_vel
                        cactus_box.y = 207
                    cactus_box.x = cactus_position_lst[e][0]
                    if val4 == 40:
                        val4 = 0
                    if val4 <= 20:
                        win.blit(cactus_lst[e][0], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                    else:
                        win.blit(cactus_lst[e][1], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                    val4 += 1
            except:
                pass
        cactus_position_lst = cactus_position_lst[::-1]
        cactus_lst = cactus_lst[::-1]
        for f in range(len(cloud_lst)):
            try:
                cloud_lst[f][0] -= cactus_vel
                win.blit(cloud_image, (cloud_lst[f][0], cloud_lst[f][1]))
            except:
                pass
        if val5 >= 20:
            val5 = 0
        if val5 % 5 <= 2:
            win.blit(dino_duck1,(dino_box.x,dino_box.y))
            pg.display.update()
        if val5 % 5 > 2:
            win.blit(dino_duck2, (dino_box.x, dino_box.y))
            pg.display.update()
        val6 += 1
    val2 += 1
    val5 += 1


def end_game():
    global val, val2, val3, val4, val5, val6, key, score,dino_box,cactus_box, x_pos_bg, cactus_vel, cactus_lst, cactus_position_lst, jump_vel, JUMP_VEL, JUMP, RUN, DUCK
    win.blit(ending_text, (326, 165))
    win.blit(pg.font.SysFont("Arial", 30, 1).render("Score: " + str(int(score)), 1, "#000000"), (370, 230))
    pg.display.update()
    pg.time.delay(2000)
    val = 0
    key = 0
    val2 = 0
    val3 = 0
    x_pos_bg = 0
    cactus_lst = [[large_cactus1, large_cactus1]]
    cloud_lst = []
    cactus_position_lst = [[800, 207]]
    jump_vel = JUMP_VEL = 7.5
    cactus_vel = 4.5
    score = 0
    val4 = 0
    val6 = 0
    cactus_box = pg.Rect(800, 207, 48, 75)
    dino_box = pg.Rect(70, 217, 48, 75)
    val5 = 0
    JUMP = False
    RUN = True
    DUCK = False
    main()


def draw_window():
    global win, track, background, val, x_pos_bg, cactus_vel, cloud_image, cactus_box, dino_box, ending_text, score_text, score
    image_width = track.get_width()
    pg.draw.rect(win, "#ffffff", background)
    if cactus_box.colliderect(dino_box):
        pg.time.delay(1000)
        end_game()
    if val == 0:
        win.blit(track, (0, 270))
        win.blit(starting_dino, (dino_box.x, dino_box.y))
        win.blit(large_cactus1, (cactus_box.x, cactus_box.y))
        win.blit(starting_text, (310, 165))
        win.blit(score_text.render("Score: " + str(score), 1, "#000000"), (760, 15))
    if val != 0:
        win.blit(track, (x_pos_bg, 270))
        win.blit(track, (image_width + x_pos_bg, 270))
        if x_pos_bg <= -image_width:
            win.blit(track, (image_width + x_pos_bg, 270))
            x_pos_bg = 0
        x_pos_bg -= cactus_vel * 2
        move_dino()
        win.blit(score_text.render("Score: " + str(int(score)), 1, "#000000"), (760, 15))
    pg.display.update()


def main():
    global val, cactus_position_lst, DUCK,score,val4, key, val3, cactus_vel, cloud_lst, bird_lst, bird1, bird2, cactus_box, JUMP, RUN, cactus_lst, score, large_cactus_image_lst, small_cactus_image_lst, val2
    run = True
    clock = pg.time.Clock()
    while run:
        clock.tick(20)
        if val == 1:
            if val3 >= 300:
                val3 = 0
            if choice(range(20)) == 2 and val3 > 200:
                new_cactus_lst = choice([large_cactus_image_lst, small_cactus_image_lst, bird_lst])
                if new_cactus_lst == large_cactus_image_lst:
                    new_cactus = choice(large_cactus_image_lst)
                    cactus_lst.append([new_cactus,new_cactus])
                    cactus_position_lst.append([900, 207])
                if new_cactus_lst == small_cactus_image_lst:
                    new_cactus = choice(small_cactus_image_lst)
                    cactus_lst.append([new_cactus,new_cactus])
                    cactus_position_lst.append([900, 221])
                if new_cactus_lst == bird_lst:
                    cactus_lst.append([bird1,bird2])
                    cactus_position_lst.append([900,200])

            if choice(range(40)) == 2:
                for i in range(2):
                    cloud_lst.append([choice(range(100, 800)), choice(range(50, 150))])
            val3 += cactus_vel
            score += cactus_vel / 8
        if int(score % 150) <= 0 and score != 0:
            cactus_vel += 0.5
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and DUCK == False:
                    key = 1
                    val = 1
                if event.key == pg.K_DOWN:
                    key = 2
                    val = 1
        if val == 1:
            cactus_lst = cactus_lst[::-1]
            cactus_position_lst = cactus_position_lst[::-1]
            for e in range(len(cactus_lst)):
                try:
                    a = cactus_position_lst[e][0]
                    if a < 22:
                        cactus_box.x = cactus_position_lst[e+1]
                    if a < -100:
                        cactus_position_lst.pop(e)
                        cactus_lst.pop(e)
                        pg.display.update()
                    else:
                        if cactus_lst[e][0] == bird1:
                            cactus_position_lst[e][0] -= (cactus_vel + 1.8)
                            cactus_box.y = 155

                        else:
                            cactus_position_lst[e][0] -= cactus_vel
                            cactus_box.y = 207
                        cactus_box.x = cactus_position_lst[e][0]
                        if val4 == 40:
                            val4 = 0
                        if val4 <= 20:
                            win.blit(cactus_lst[e][0], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                        else:
                            win.blit(cactus_lst[e][1], (cactus_position_lst[e][0], cactus_position_lst[e][1]))
                        val4 += 1
                except:
                    pass
            cactus_position_lst = cactus_position_lst[::-1]
            cactus_lst = cactus_lst[::-1]
            for f in range(len(cloud_lst)):
                try:
                    cloud_lst[f][0] -= cactus_vel
                    win.blit(cloud_image, (cloud_lst[f][0], cloud_lst[f][1]))
                except:
                    pass
            pg.display.update()
        if key == 2:
            DUCK = True
            RUN = False
            key += 2
        if key == 1:
            JUMP = True
            RUN = False
            key += 2
        draw_window()
    pg.quit()

if __name__ == "__main__":
    main()
