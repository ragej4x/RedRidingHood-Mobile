
class controllClass():

    def __init__(self, pg) -> None:
        #self.Right = pg.Rect(())
        self.scInfo = pg.display.Info()

        self.rightBtn = pg.Rect((int(self.scInfo.current_w//3), 700, 70 ,30))

    def update(self, pg, window):
        #print(self.scInfo.current_w, self.scInfo.current_h)
        pg.draw.rect(window, (255,255,255), self.rightBtn)

        pass
