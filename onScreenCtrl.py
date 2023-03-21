import player, enemy
class controllClass():

    def __init__(self, pg, window, display) -> None:
        #self.Right = pg.Rect(())
        self.scInfo = pg.display.Info()


        self.jumpBtn = pg.Rect((self.scInfo.current_w - 1024 + 100, self.scInfo.current_h - 680 + 500, 40 ,40))
        self.rightBtn = pg.Rect((self.scInfo.current_w - 1024 + 150, self.scInfo.current_h - 620 + 500, 40 ,40))
        self.leftBtn = pg.Rect((self.scInfo.current_w - 1024 + 50, self.scInfo.current_h - 620 + 500, 40 ,40))

        self.atkBtn = pg.Rect((self.scInfo.current_w - 1024 + 800, self.scInfo.current_h - 620 + 500, 40 ,40))


    
    def update(self, pg, window, display):
        

        
        
        print(self.scInfo.current_w, self.scInfo.current_h)
        self.jumpBtn = pg.draw.rect(display, (255,255,255), self.jumpBtn)
        self.rightBtn = pg.draw.rect(display, (255,255,255), self.rightBtn)
        self.leftBtn = pg.draw.rect(display, (255,255,255), self.leftBtn)
        self.atkBtn = pg.draw.rect(display, (255,255,255), self.atkBtn)
        """
        if self.leftBtn.colliderect(touch) and player.rdh.cmb1 == False and player.rdh.player_get_dmg == False and player.rdh.death == False:
            player.rdh.x -= player.rdh.speed
            player.rdh.move_left = True
            player.rdh.left = True
            player.rdh.right = False
            player.rdh.camera_x -= 2
        """

    #MEMMNG
    #OI

    #PLAYER
    def player_func(self, pg, window, display):
        mx,my = pg.mouse.get_pos()

        self.touch = pg.draw.rect(display, (255,255,255), (mx,my, 2,2))
        player.rdh.keyinput = pg.key.get_pressed()
        




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

#MOVEMENT

        if self.leftBtn.colliderect(self.touch) == True and player.rdh.cmb1 == False and player.rdh.player_get_dmg == False and player.rdh.death == False:
            player.rdh.x -= player.rdh.speed
            player.rdh.move_left = True
            player.rdh.left = True
            player.rdh.right = False
            player.rdh.camera_x -= 2

        if self.rightBtn.colliderect(self.touch) == True and player.rdh.cmb1 == False and player.rdh.player_get_dmg == False and player.rdh.death == False:
            player.rdh.x += player.rdh.speed
            player.rdh.move_right = True
            player.rdh.right = True
            player.rdh.left = False
            player.rdh.camera_x += 2


        #CAMERA SMOOTH SCROLLING
        if player.rdh.camera_x + 120 <= player.rdh.x:
            player.rdh.camera_x += 0.8

        if player.rdh.camera_x + 120 >= player.rdh.x:
            player.rdh.camera_x -= 0.8

        #JUMP
        if self.jumpBtn.colliderect(self.touch) and player.rdh.cmb1 == False and player.rdh.player_get_dmg == False and player.rdh.death == False:
            player.rdh.jump = True

        if player.rdh.jump == True and player.rdh.left == True and player.rdh.right == False and player.rdh.j_frame_left >= 2:
            player.rdh.right = False
            player.rdh.speed = 1
            player.rdh.y -= player.rdh.jump_vel *1.5
            player.rdh.jump_vel -= 0.4
            player.rdh.x -= 1.5
            if player.rdh.jump_vel <-5:
                player.rdh.speed = 3
                player.rdh.jump = False
                player.rdh.jump_vel = 5
                player.rdh.y = 140
                player.rdh.j_frame_left = 0

        if player.rdh.jump == True and player.rdh.right == True and player.rdh.left == False and player.rdh.j_frame_right >= 2:
            player.rdh.left = False
            player.rdh.speed = 1
            player.rdh.y -= player.rdh.jump_vel *1.5
            player.rdh.jump_vel -= 0.4
            player.rdh.x += 1.5
            if player.rdh.jump_vel <-5:
                player.rdh.speed = 3
                player.rdh.jump = False
                player.rdh.jump_vel = 5
                player.rdh.y = 140
                player.rdh.j_frame_right = 0

        #COMBO 1
        if self.atkBtn.colliderect(self.touch) and player.rdh.player_get_dmg == False and player.rdh.death == False:
            player.rdh.cmb1 = True

        if player.rdh.c1_frame_right >= 22:
            player.rdh.cmb1 = False
            player.rdh.c1_frame_right = 0


        if player.rdh.c1_frame_left >= 22:
            player.rdh.cmb1 = False
            player.rdh.c1_frame_left = 0

        #PHYSICS
        if player.rdh.c1_frame_left == 1.8:
            player.rdh.x = player.rdh.x - 20
        if player.rdh.c1_frame_left == 8.399999999999999:
            player.rdh.x = player.rdh.x - 20
        if player.rdh.c1_frame_left == 15.900000000000016:
            player.rdh.x = player.rdh.x - 20

        if player.rdh.c1_frame_right == 1.8:
            player.rdh.x = player.rdh.x + 20
        if player.rdh.c1_frame_right == 8.399999999999999:
            player.rdh.x = player.rdh.x + 20
        if player.rdh.c1_frame_right == 15.900000000000016:
            player.rdh.x = player.rdh.x + 20



        #ANIMATION

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

