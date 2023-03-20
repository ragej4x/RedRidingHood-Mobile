import pygame as pg
import player , enemy
import onScreenCtrl

pg.init()
#DISPLAY
width,height = 1024,620
display = pg.display.set_mode()

scInfo = pg.display.Info()
window = pg.Surface((scInfo.current_w //3, scInfo.current_h//3))
icon = pg.image.load("data/bin/ico.png")
pg.display.set_icon(icon)
pg.display.set_caption("RDH")

fps = pg.time.Clock()
loop = True
bg = pg.image.load("data/bg.png")

with open("hacks.txt", "r") as config:
    player.rdh.health = int(config.readline())
    print(config.readline())


#MEMMNG
#OI

#PLAYER
def player_func():
    

    keyinput = pg.key.get_pressed()


    player.rdh.update(pg, window)
    player.healthbar.hb_animation(pg, window)
    player.healthbar.heart_animation(pg, window)

    if enemy.slime.health > 0:
        enemy.slime.update(window)
        #ENEMY PHYSICS AND DAMAGE LOGIC
        if player.rdh.rect.colliderect(enemy.slime.rect) and enemy.slime.jump == True and enemy.slime.death == False:
            if enemy.slime.left == True:
                player.rdh.x = player.rdh.x - 20
                player.rdh.player_get_dmg = True
                player.rdh.cmb1 = False
                player.rdh.c1_frame_left = 0
                player.rdh.health = player.rdh.health -1
                print("DMG")


            if enemy.slime.right == True:
                player.rdh.x = player.rdh.x + 20
                player.rdh.player_get_dmg = True
                player.rdh.cmb1 = False
                player.rdh.c1_frame_left = 0
                player.rdh.health = player.rdh.health -1
                print("DMG")

    #SLIMEJUMP ANIMATION:
        if enemy.slime.j_count >= 0 and enemy.slime.left == True and enemy.slime.death == False and player.rdh.death == False:
            enemy.slime.jump_left_anim(window)

        if enemy.slime.j_count >= 0 and enemy.slime.right == True and enemy.slime.death == False and player.rdh.death == False:
            enemy.slime.jump_right_anim(window)

        if enemy.slime.left == False and enemy.slime.right == False and enemy.slime.death == False:
            window.blit(enemy.slime.slime_idle_image,(enemy.slime.x - player.rdh.camera_x, enemy.slime.y))

        #EFFECTS GUSH
        enemy.slime.fx(window)

        #BUGFIX
        if player.rdh.death == True:
            window.blit(enemy.slime.slime_idle_image,(enemy.slime.x - player.rdh.camera_x, enemy.slime.y))
            enemy.slime.y = 160
#SLIME DEATH ANIMATION

    #LEFT

    if enemy.slime.health <= 1  and enemy.slime.left == True:
        enemy.slime.death = True

    if enemy.slime.death == True and not enemy.slime.death_frame >= 15 and enemy.slime.left == True:
        enemy.slime.y = 160 - 7
        enemy.slime.death_left_anim(window)

    if enemy.slime.death_frame >= 15:
        enemy.slime.death_frame = 0
        enemy.slime.death = False
        enemy.slime.health = 24


    #RIGHT

    if enemy.slime.health <= 1  and enemy.slime.right == True:
        enemy.slime.death = True

    if enemy.slime.death == True and not enemy.slime.death_frame >= 15  and enemy.slime.right == True:
        enemy.slime.y = 160 -7
        enemy.slime.death_right_anim(window)

    if enemy.slime.death_frame >= 15:
        enemy.slime.death_frame = 0
        enemy.slime.death = False
        enemy.slime.health = 24
        enemy.slime.y = 160
#RUN

    if player.rdh.move_left == True and player.rdh.move_right == False and player.rdh.jump == False:
        player.rdh.run_left_anim(pg, window)

    if player.rdh.move_right == True and player.rdh.move_left == False and player.rdh.jump == False:
        player.rdh.run_right_anim(pg, window)

#IDLE
    if player.rdh.left == True and player.rdh.move_right == False and player.rdh.move_left == False and player.rdh.jump == False and player.rdh.cmb1 == False and player.rdh.player_get_dmg == False and player.rdh.death == False:
        player.rdh.idle_left_anim(pg, window)

    if player.rdh.right == True and player.rdh.move_right == False and player.rdh.move_left == False and player.rdh.jump == False and player.rdh.cmb1 == False and player.rdh.player_get_dmg == False and player.rdh.death == False:
        player.rdh.idle_right_anim(pg, window)
#JUMP
    if player.rdh.jump == True and player.rdh.left == True and player.rdh.player_get_dmg == False:
        player.rdh.jump_left_anim(pg, window)

    if player.rdh.jump == True and player.rdh.right == True and player.rdh.player_get_dmg == False:
        player.rdh.jump_right_anim(pg, window)

#COMBAT 1
    if player.rdh.cmb1 == True and player.rdh.right == True and player.rdh.jump == False and player.rdh.player_get_dmg == False:
        player.rdh.cmb1_right_anim(pg, window)

    if player.rdh.cmb1 == True and player.rdh.left == True and player.rdh.jump == False and player.rdh.player_get_dmg == False:
        player.rdh.cmb1_left_anim(pg, window)

#fIX BUG IF "a" and "d" is helding
    if keyinput[pg.K_a] == True and keyinput[pg.K_d] == True and player.rdh.jump == False and player.rdh.cmb1 == False and player.rdh.death == False:
        player.rdh.idle_right_anim(pg, window)
        player.move_right = True
        player.rdh.right = True
        player.rdh.left = False


    #print(enemy.slime.left,enemy.slime.right)

#DAMAGE ANIMATION
    if player.rdh.player_get_dmg == True and player.rdh.left == True and player.rdh.death == False:
        player.rdh.dmg_left_anim(pg, window)
    if player.rdh.d_frame_left >= 6:
        player.rdh.player_get_dmg = False
        player.rdh.d_frame_left = 0

    if player.rdh.player_get_dmg == True and player.rdh.right == True and player.rdh.death == False:
        player.rdh.dmg_right_anim(pg, window)
    if player.rdh.d_frame_right >= 6:
        player.rdh.player_get_dmg = False
        player.rdh.d_frame_right = 0

#DEATH ANIMATION
    #LEFT
    if player.rdh.left == True and player.rdh.health < 1:
        player.rdh.death = True

    if player.rdh.left == True and player.rdh.death == True:
        player.rdh.death_left_anim(pg, window)
    if player.rdh.death_frame_left >= 21:
        player.rdh.death_frame_left = 20

    #RIGHT
    if player.rdh.right == True and player.rdh.health < 1:
        player.rdh.death = True

    if player.rdh.right == True and player.rdh.death == True:
        player.rdh.death_right_anim(pg, window)
    if player.rdh.death_frame_right >= 21:
        player.rdh.death_frame_right = 20


    #print(player.rdh.player_get_dmg)
    #UPDATE


#SHOW FPS
def show_fps():
    font = pg.font.SysFont("Arial",18)
    get_fps = str(int(fps.get_fps()))
    fps_txt = font.render(get_fps, True , (255,255,255))
    display.blit(fps_txt,(5,5))

#EVENT HANDLER
def event_handler():
    global loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False

    surface = pg.transform.scale(window, (width, height))
    display.blit(surface,(0,0))
    show_fps()

    pg.display.flip()
    fps.tick(42)



while loop == True:
    window.fill(0)
    display.fill(0)
    #window.blit(bg,(-250 - player.rdh.camera_x,-250))

    #enemy.slime2.update(pg, window)
    #window.blit(hb,(0,0))

    onScreenCtrl.controllClass(pg).update(pg,display)

    player_func()

    event_handler()


