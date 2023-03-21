import pygame as pg
import player , enemy
import onScreenCtrl
import asyncio
pg.init()
#DISPLAY
width,height = 1024,620
display = pg.display.set_mode((1024,620))

scInfo = pg.display.Info()
window = pg.Surface((scInfo.current_w //3, scInfo.current_h//3))
icon = pg.image.load("data/bin/ico.png")
pg.display.set_icon(icon)
pg.display.set_caption("RDH")

async def main():

    fps = pg.time.Clock()
    loop = True
    bg = pg.image.load("data/bg.png")

    with open("hacks.txt", "r") as config:
        player.rdh.health = int(config.readline())
        print(config.readline())



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
                #loop = False
                exit()
                #print("AAA")

        surface = pg.transform.scale(window, (width, height))
        display.blit(surface,(0,0))
        show_fps()
        onScreenCtrl.controllClass(pg, window, display).update(pg, window,display)


        pg.display.flip()
        fps.tick(42)
        
    def updateEnemy():
        #keyinput = pg.key.get_pressed()


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


    while True:
        window.fill(0)
        display.fill(0)
        #window.blit(bg,(-250 - player.rdh.camera_x,-250))

        #enemy.slime2.update(pg, window)
        #window.blit(hb,(0,0))

        
        #player_func()
        onScreenCtrl.controllClass(pg, window, display).player_func(pg, window, display)
        updateEnemy()

        event_handler()
        await asyncio.sleep(0)


asyncio.run(main())