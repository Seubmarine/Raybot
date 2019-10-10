from vector import Vector2 as Vec2
from constants import *
import pyxel as px
import newpixelmodule as npx

class Entity:
    def __init__(self, position_x_y, lenght_x_y, color):
        #
        self.position = position_x_y
        self.oldlenght = lenght_x_y

        self.lenght = self.oldlenght + self.position

        # All Entity corner, it's a vector2 position on screen
        self.upperleftcorner = self.position
        self.downleftcorner = self.position + Vec2(0, self.oldlenght.y)
        self.upperrightcorner = self.position + Vec2(self.oldlenght.x, 0)
        self.downrightcorner = self.position + \
            Vec2(self.oldlenght.x, self.oldlenght.y)
        self.corners = [self.upperleftcorner, self.upperrightcorner,
                        self.downleftcorner, self.downrightcorner]

        # The 4 wall of the entity, it's two vector2
        self.upwall = (self.upperleftcorner, self.upperrightcorner)
        self.rightwall = (self.upperrightcorner, self.downrightcorner)
        self.downwall = (self.downrightcorner, self.downleftcorner)
        self.leftwall = (self.downleftcorner, self.upperleftcorner)
        self.walls = [self.upwall, self.rightwall, self.downwall, self.leftwall]

        self.color = color

    def update(self):
        self.lenght = self.oldlenght + self.position
        self.upperleftcorner = self.position
        self.upperrightcorner = self.position + Vec2(self.oldlenght.x, 0)
        self.downleftcorner = self.position + Vec2(0, self.oldlenght.y)
        self.downrightcorner = self.position + \
            Vec2(self.oldlenght.x, self.oldlenght.y)

        # All Entity corner, it's a vector2 position on screen
        self.upperleftcorner = self.position
        self.downleftcorner = self.position + Vec2(0, self.oldlenght.y)
        self.upperrightcorner = self.position + Vec2(self.oldlenght.x, 0)
        self.downrightcorner = self.position + \
            Vec2(self.oldlenght.x, self.oldlenght.y)
        self.corners = [self.upperleftcorner, self.upperrightcorner,
                        self.downleftcorner, self.downrightcorner]

        # The 4 wall of the entity, it's two vector2
        self.upwall = (self.upperleftcorner, self.upperrightcorner)
        self.rightwall = (self.upperrightcorner, self.downrightcorner)
        self.downwall = (self.downrightcorner, self.downleftcorner)
        self.leftwall = (self.downleftcorner, self.upperleftcorner)
        self.walls = [self.upwall, self.rightwall,
                      self.downwall, self.leftwall]

    def debug(self):
        for i in self.walls:
            npx.line(i[0], i[1], RED)

        for i in self.corners:
            npx.pix(i, PURPLE)

    def draw(self):
        npx.rect(self.position, self.lenght, self.color)


class Player(Entity):
    def __init__(self, position_x_y, lenght_x_y):
        super().__init__(position_x_y, lenght_x_y, ORANGE)
        self.velocity = 55
    def update(self, dt):
        super().update()

        dt_velocity = self.velocity * dt

        if px.btn(px.KEY_W):
            self.position.up(dt_velocity)
        if px.btn(px.KEY_S):
            self.position.down(dt_velocity)
        if px.btn(px.KEY_A):
            self.position.left(dt_velocity)
        if px.btn(px.KEY_D):
            self.position.right(dt_velocity)

