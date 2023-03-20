import player
import enemy
class fx_class():
    def __init__(self):
        self.x = 0
        self.y = 0

        #SLIME
        self.slime_gush_left = []
        self.slime_gush_right = []
        self.slime_gush_frame = 0
        self.gush_left = False
        self.gush_right = False


    def slime_gush_left_anim(self, pg, window):
        self.x = player.rdh.x
        self.y = player.rdh.y
        for i in range(1, 10 + 1):
            image = pg.image.load(f"data/bin/fx/slime_gush{i}.png")
            image = pg.transform.flip(image, True, False)
            self.slime_gush_left.append(image)
            window.blit(self.slime_gush_left[int(self.slime_gush_frame)], (self.x - player.rdh.camera_x - 25, self.y - 10))
        self.slime_gush_frame += 0.5

    def slime_gush_right_anim(self, pg, window):
        self.x = player.rdh.x
        self.y = player.rdh.y
        for i in range(1, 10 + 1):
            image = pg.image.load(f"data/bin/fx/slime_gush{i}.png")
            self.slime_gush_right.append(image)
            window.blit(self.slime_gush_right[int(self.slime_gush_frame)], (self.x - player.rdh.camera_x, self.y - 10))
        self.slime_gush_frame += 0.5



fx = fx_class()
