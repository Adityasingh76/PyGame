import pygame as pg
import random as rd
import math

pg.font.init()

WIDTH,HEIGHT = 900,600
win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Pong Game")
starting_text = pg.font.SysFont("Arial",35,1).render("Press Space to Start",1,"#ffffff")
game_mode_text = pg.font.SysFont("Arial",27,1)
score = 0
bg = "#00124d"
y_speed = rd.randint(3,8)
x_speed = rd.randint(3,8)
x_speed1 = x_speed
y_speed1 = y_speed
mode = "Ai"
ball_x = 460
ball_y = 300
x_pos = 0
y_pos = 0
val3 = 0
ball_radius = 10
box_vel = 7
left_score = 15
right_score = 15
scores = pg.font.SysFont("Arial",30,1)
ball_box = pg.Rect(ball_x - ball_radius,ball_y - ball_radius,20,20)
game_mode_text_rect = pg.Rect(840,9,23,23)
destination_finder = pg.Rect(ball_box.x,ball_box.y,25,25)
left_box = pg.Rect(5,300,15,90)
score_box = pg.Rect(395,0,130,40)
right_box = pg.Rect(WIDTH-left_box.width - 5,300,15,90)
MOVE_RIGHT_BOX = 0
MOVE_LEFT_BOX = 0
ai_play = 1
collide_tolerence = 10
val = 0
val2 = 0

def collide_ball():
    global x_speed,y_speed,x_pos,y_pos,x_speed1,y_speed1
    if ball_box.right - right_box.left < collide_tolerence or ball_box.left - left_box.right < collide_tolerence:
        x_speed *= -1
    x_speed1 = x_speed
    y_speed1 = y_speed
    z = 0
    while True:
        if z == 0:
            destination_finder.x = ball_box.x
            destination_finder.y = ball_box.y
        destination_finder.x += x_speed1
        destination_finder.y += y_speed1
        if HEIGHT - destination_finder.bottom < collide_tolerence or destination_finder.top < collide_tolerence:
            y_speed1 *= -1
        if WIDTH - destination_finder.right < collide_tolerence or destination_finder.left < collide_tolerence:
            x_pos = destination_finder.x
            y_pos = destination_finder.y
            break
        z += 1


def end_game(side):
    global score,x_speed,y_speed,ball_y,ball_x,left_score,right_score,MOVE_LEFT_BOX,MOVE_RIGHT_BOX,val,val2
    if side == 0:
        win.blit(pg.font.SysFont("Arial",50,1).render("Its a Tie!",1,"#ffffff"),(WIDTH // 2 - 100,HEIGHT // 2))
    if side == 1:
        win.blit(pg.font.SysFont("Arial",50,1).render("Right Won!",1,"#ffffff"),(WIDTH // 2 - 100,HEIGHT // 2))
    if side == 2:
        win.blit(pg.font.SysFont("Arial",50,1).render("Left Won!",1,"#ffffff"),(WIDTH // 2 - 100,HEIGHT // 2))
    pg.display.update()
    pg.time.delay(2000)
    score = 0
    y_speed = rd.randint(3, 8)
    x_speed = rd.randint(3, 8)
    ball_x = 460
    ball_y = 300
    ball_radius = 10
    box_vel = 7
    left_score = 15
    right_score = 15
    MOVE_RIGHT_BOX = 0
    MOVE_LEFT_BOX = 0
    val = 0
    val2 = 0
    try:
        main()
    except:
        pass

def reset_game(side):
    global val,val2,ball_x,ball_y,box_vel,x_speed,y_speed,MOVE_LEFT_BOX,MOVE_RIGHT_BOX,x_speed1,y_speed1
    val = 0
    val2 = 0
    ball_x = 460
    ball_y = 300
    y_speed = rd.randint(3, 8)
    x_speed = rd.randint(3, 8)
    MOVE_RIGHT_BOX = 0
    MOVE_LEFT_BOX = 0
    main()

def draw_window():
    global ball_x,ball_y,y_speed,val2,left_score,right_score,val3
    win.fill(bg)
    ball_box.x = ball_x - ball_radius
    ball_box.y = ball_y - ball_radius
    if right_score == 0:
        end_game(1)
    if left_score == 0:
        end_game(0)
    if WIDTH - ball_box.left < collide_tolerence:
        right_score -= 1
        reset_game(1)
    if ball_box.right < 3:
        left_score -= 1
        reset_game(1)
    if HEIGHT - ball_box.bottom < collide_tolerence or ball_box.top < collide_tolerence:
        y_speed *= -1
    if right_box.colliderect(ball_box) or left_box.colliderect(ball_box):
        collide_ball()
        val2 += 1
    pg.draw.rect(win, bg, ball_box)
    pg.draw.rect(win,bg,game_mode_text_rect)
    win.blit(game_mode_text.render(mode,1,"#ffffff"),(840,9))
    pg.draw.rect(win,bg,destination_finder)
    pg.draw.rect(win,"#ffffff",right_box)
    pg.draw.rect(win,"#ffffff",left_box)
    pg.draw.rect(win,"#ffffff",score_box)
    pg.draw.line(win,"#000000",(460,0),(460,40),3)
    pg.draw.line(win,"#000000",(460,0),(460,HEIGHT),5)
    win.blit(scores.render(str(left_score),1,"#000000"),(405,3))
    win.blit(scores.render(str(right_score),1,"#000000"),(480,3))
    pg.draw.circle(win,"#ffffff",(ball_x,ball_y),ball_radius)
    if ball_box.x < 750 and val3 == 1:
        left_box.y += 70
        val3 = 3
    if ball_box.x < 100 and val3 == 2:
        left_box.y -= 30
        val3 = 3
    if ai_play == 1 and destination_finder.top not in range(left_box.top,left_box.bottom) and destination_finder.x < 250:
        if destination_finder.centery > left_box.centery:
            left_box.y += box_vel
            val3 = 1
        if destination_finder.centery < left_box.centery:
            left_box.y -= box_vel
            val3 = 2
    if val == 0:
        win.blit(starting_text, (300, 100))
    pg.display.update()

def main():
    global MOVE_LEFT_BOX,MOVE_RIGHT_BOX,right_box,left_box,ball_x,ball_y,x_speed,y_speed,val,box_vel,val2,mode,ai_play
    clock = pg.time.Clock()
    move_lst = [0,box_vel,-box_vel]
    c = 0
    run = True
    while run:
        move_lst = [0, box_vel, -box_vel]
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if game_mode_text_rect.collidepoint(mouse_pos):
                    if mode == "Ai":
                        mode = "PVP"
                        ai_play = 0
                    elif mode == "PVP":
                        mode = "Ai"
                        ai_play = 1
                    if left_score > right_score:
                        end_game(2)
                    if left_score < right_score:
                        end_game(1)
                    else:
                        end_game(0)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    val = 1
                if event.key == pg.K_UP:
                    MOVE_RIGHT_BOX = 1
                if event.key == pg.K_DOWN:
                    MOVE_RIGHT_BOX = 2
                if event.key == pg.K_w and ai_play == 0:
                    MOVE_LEFT_BOX = 1
                if event.key == pg.K_s and ai_play == 0:
                    MOVE_LEFT_BOX = 2
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    MOVE_RIGHT_BOX = 0
                if event.key == pg.K_w or event.key == pg.K_s:
                    MOVE_LEFT_BOX = 0
        if right_box.y <= 0:
            right_box.y = 1
        if right_box.y >= 600 - right_box.height:
            right_box.y = 600 - right_box.height - 1
        if MOVE_RIGHT_BOX != 0 :
            right_box.y -= move_lst[MOVE_RIGHT_BOX]
            val = 1
        if left_box.y <= 0:
            left_box.y = 1
        if left_box.y >= 600 - left_box.height:
            left_box.y = 600 - left_box.height - 1
        if MOVE_LEFT_BOX != 0 :
            left_box.y -= move_lst[MOVE_LEFT_BOX]
            val = 1
        if val != 0:
            ball_x += x_speed
            ball_y += y_speed
        draw_window()


    pg.quit()

if __name__ == "__main__":
    main()
