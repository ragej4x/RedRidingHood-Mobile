import math
class rdh_class:
    def __init__(self):
        self.x = 0
        self.y = 140
        self.speed = 3
        self.jump = False
        self.jump_vel = 5
        self.move_left = False
        self.move_right = False
        self.left = False
        self.right = True

        #HEALTH
        self.health = 8
        self.death = False
        #COMBAT
        self.player_dmg = 100
        self.player_get_dmg = False
        self.cmb1 = False


        self.camera_x = 0
        self.camera_y = 0
        #=-=
        self.run_left_list = []
        self.run_right_list = []
        self.r_frame_left = 0
        self.r_frame_right = 0
        #=-=
        self.idle_left_list = []
        self.idle_right_list = []
        self.i_frame_left = 0
        self.i_frame_right = 0
        #=-=
        self.jump_left_list = []
        self.jump_right_list = []
        self.j_frame_left = 0
        self.j_frame_right = 0
        #=-=
        self.cmb1_left_list = []
        self.cmb1_right_list = []
        self.c1_frame_left = 0
        self.c1_frame_right = 0
        #=-=
        self.dmg_left_list = []
        self.dmg_right_list = []
        self.d_frame_left = 0
        self.d_frame_right = 0
        #=-=
        self.death_left_list = []
        self.death_right_list = []
        self.death_frame_left = 0
        self.death_frame_right = 0

        self.r,self.g,self.b = (255,0,0),(0,255,0),(0,0,255)
        self.rect = ((self.x - self.camera_x + 2, self.y + 16 , 16,20))

        #self.cmb_rect_left = ((self.x - self.camera_x - 15, self.y + 20 , 15,5))
        #self.cmb_rect_right = ((self.x - self.camera_x + 25, self.y + 20 , 15,5))

        self.show_rect = False
    def update(self, pg, window):
        self.move_left = False
        self.move_right = False


        #RECTS

        self.rect = pg.Rect(self.x - self.camera_x + 2, self.y + 16 , 16,20)
        self.cmb_rect_left = pg.Rect(self.x - self.camera_x - 13, self.y + 20 , 15,5)
        self.cmb_rect_right = pg.Rect(self.x - self.camera_x + 18, self.y + 20 , 15,5)

        if self.show_rect == True:
            self.rect = pg.draw.rect(window, (self.b),(self.rect),1)

            if self.left == True:
                self.cmb_rect_left = pg.draw.rect(window, (self.r),(self.cmb_rect_left),1)

            if self.right == True:
                self.cmb_rect_right = pg.draw.rect(window, (self.r),(self.cmb_rect_right),1)


        self.keyinput = pg.key.get_pressed()
        #X,Y MOVEMENT
        if self.keyinput[pg.K_a] and self.cmb1 == False and self.player_get_dmg == False and self.death == False:
            self.x -= self.speed
            self.move_left = True
            self.left = True
            self.right = False
            self.camera_x -= 2

        if self.keyinput[pg.K_d] and self.cmb1 == False and self.player_get_dmg == False and self.death == False:
            self.x += self.speed
            self.move_right = True
            self.right = True
            self.left = False
            self.camera_x += 2


        #CAMERA SMOOTH SCROLLING
        if self.camera_x + 120 <= self.x:
            self.camera_x += 0.8

        if self.camera_x + 120 >= self.x:
            self.camera_x -= 0.8

        #JUMP
        if self.keyinput[pg.K_w] and self.cmb1 == False and self.player_get_dmg == False and self.death == False:
            self.jump = True

        if self.jump == True and self.left == True and self.right == False and self.j_frame_left >= 2:
            self.right = False
            self.speed = 1
            self.y -= self.jump_vel *1.5
            self.jump_vel -= 0.4
            self.x -= 1.5
            if self.jump_vel <-5:
                self.speed = 3
                self.jump = False
                self.jump_vel = 5
                self.y = 140
                self.j_frame_left = 0

        if self.jump == True and self.right == True and self.left == False and self.j_frame_right >= 2:
            self.left = False
            self.speed = 1
            self.y -= self.jump_vel *1.5
            self.jump_vel -= 0.4
            self.x += 1.5
            if self.jump_vel <-5:
                self.speed = 3
                self.jump = False
                self.jump_vel = 5
                self.y = 140
                self.j_frame_right = 0

        #COMBO 1
        if self.keyinput[pg.K_u] and self.player_get_dmg == False and self.death == False:
            self.cmb1 = True

        if self.c1_frame_right >= 22:
            self.cmb1 = False
            self.c1_frame_right = 0


        if self.c1_frame_left >= 22:
            self.cmb1 = False
            self.c1_frame_left = 0

        #PHYSICS
        if self.c1_frame_left == 1.8:
            self.x = self.x - 20
        if self.c1_frame_left == 8.399999999999999:
            self.x = self.x - 20
        if self.c1_frame_left == 15.900000000000016:
            self.x = self.x - 20

        if self.c1_frame_right == 1.8:
            self.x = self.x + 20
        if self.c1_frame_right == 8.399999999999999:
            self.x = self.x + 20
        if self.c1_frame_right == 15.900000000000016:
            self.x = self.x + 20

        #print(self.c1_frame_right)
        #print(self.x,self.speed)

    #RUN ANIMATION
    def run_left_anim(self, pg, window):
        for num in range(1,24 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_run{num}.png")
            image.set_colorkey((255,0,255))
            self.run_left_list.append(image)
            window.blit(self.run_left_list[int(self.r_frame_left)], (self.x - self.camera_x, self.y))
        self.r_frame_left += 00.5

    def run_right_anim(self, pg, window):
        for num in range(1,24 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_run{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.run_right_list.append(image)
            window.blit(self.run_right_list[int(self.r_frame_right)], (self.x - self.camera_x, self.y))
        self.r_frame_right += 00.5

    #IDLE ANIMATION
    def idle_left_anim(self, pg, window):
        for num in range(1,18 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_idle{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.idle_left_list.append(image)
            window.blit(self.idle_left_list[int(self.i_frame_left)],(self.x - self.camera_x, self.y))
        self.i_frame_left += 00.3

    def idle_right_anim(self, pg, window):
        for num in range(1,18 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_idle{num}.png")
            image.set_colorkey((255,0,255))
            self.idle_right_list.append(image)
            window.blit(self.idle_right_list[int(self.i_frame_right)],(self.x - self.camera_x, self.y))
        self.i_frame_right += 00.3

    #JUMP ANIMATION
    def jump_left_anim(self, pg,window):
        for num in range(1,18 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_jump{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.jump_left_list.append(image)
            window.blit(self.jump_left_list[int(self.j_frame_left)],(self.x - self.camera_x, self.y))
        self.j_frame_left += 00.60


    def jump_right_anim(self, pg,window):
        for num in range(1,18 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_jump{num}.png")
            image.set_colorkey((255,0,255))
            self.jump_right_list.append(image)
            window.blit(self.jump_right_list[int(self.j_frame_right)],(self.x - self.camera_x, self.y))
        self.j_frame_right += 00.60

    #COMBO 1 ANIMATION
    def cmb1_left_anim(self, pg,window):
        for num in range(1,22 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_firstcmb{num}.png")
            image.set_colorkey((255,0,255))
            self.cmb1_left_list.append(image)
            window.blit(self.cmb1_left_list[int(self.c1_frame_left)],(self.x - self.camera_x - 10, self.y))
        self.c1_frame_left += 00.3

    def cmb1_right_anim(self, pg,window):
        for num in range(1,22 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_firstcmb{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.cmb1_right_list.append(image)
            window.blit(self.cmb1_right_list[int(self.c1_frame_right)],(self.x - self.camera_x - 10, self.y))
        self.c1_frame_right += 00.3

    #DAMAGE ANIMATION
    def dmg_left_anim(self, pg,window):
        for num in range(1,6 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_getdmg{num}.png")
            image.set_colorkey((255,0,255))
            self.dmg_left_list.append(image)
            window.blit(self.dmg_left_list[int(self.d_frame_left)],(self.x - self.camera_x, self.y))
        self.d_frame_left += 00.3

    def dmg_right_anim(self, pg,window):
        for num in range(1,6 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_getdmg{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.dmg_right_list.append(image)
            window.blit(self.dmg_right_list[int(self.d_frame_right)],(self.x - self.camera_x, self.y))
        self.d_frame_right += 00.3

    #DEATH ANIMATION
    def death_left_anim(self, pg,window):
        for num in range(1,21 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_death{num}.png")
            image = pg.transform.flip(image, True, False)
            image.set_colorkey((255,0,255))
            self.death_left_list.append(image)
            window.blit(self.death_left_list[int(self.death_frame_left)],(self.x - self.camera_x, self.y + 15))
        self.death_frame_left += 00.4

    def death_right_anim(self, pg,window):
        for num in range(1,21 + 1):
            image = pg.image.load(f"data/rdh_anim/rdh_death{num}.png")
            image.set_colorkey((255,0,255))
            self.death_right_list.append(image)
            window.blit(self.death_right_list[int(self.death_frame_right)],(self.x - self.camera_x, self.y + 15))
        self.death_frame_right += 00.4


rdh = rdh_class()


class healthbar_class():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

        #ANIMATION
        self.bar_list_animation = []
        self.hb_frame = 0

        self.heart_list = []
        self.heart_frame = 0


    def hb_animation(self, pg, window):
        for i in range(1, 17 + 1):
            image = pg.image.load(f"data/bin/hb_animation/healthbar{i}.png")
            self.bar_list_animation.append(image)
            window.blit(self.bar_list_animation[int(self.hb_frame)], (self.pos_x, self.pos_y))
        self.hb_frame += 0.5
        #print(rdh.health)


    def heart_animation(self, pg, window):
        for i in range(1, 7 + 1):
            image = pg.image.load(f"data/bin/hb_animation/heart_anim{i}.png")
            self.heart_list.append(image)

            for j in range(rdh.health):
                window.blit(self.heart_list[int(self.heart_frame)], (self.pos_x + j * 9 + 24, self.pos_y + 19))

        self.heart_frame += 0.2

healthbar = healthbar_class(5,5)
