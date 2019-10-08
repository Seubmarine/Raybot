import pyxel as px
import newpixelmodule as npx
from constants import FPS, WIDTH, HEIGHT, WHITE, BLUE, RED, ORANGE, CYAN, PURPLE
from vector import Vector2 as Vec2
from time import time


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

        # The 4 wall of the entity, it's two vector2
        self.upwall = (self.upperleftcorner, self.upperrightcorner)
        self.rightwall = (self.upperrightcorner, self.downrightcorner)
        self.downwall = (self.downrightcorner, self.downleftcorner)
        self.leftwall = (self.downleftcorner, self.upperleftcorner)
        self.wall = [self.upwall, self.rightwall, self.downwall, self.leftwall]

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

    def update(self, dt, velocity):
        super().update()

        dt_velocity = velocity * dt

        if px.btn(px.KEY_W):
            self.position.up(dt_velocity)
        if px.btn(px.KEY_S):
            self.position.down(dt_velocity)
        if px.btn(px.KEY_A):
            self.position.left(dt_velocity)
        if px.btn(px.KEY_D):
            self.position.right(dt_velocity)


def raycast(ray_origin, ray_direction, corner1, corner2):
    ray_finalpoint = ray_origin + ray_direction
    x1 = corner1.x
    y1 = corner1.y
    x2 = corner2.x
    y2 = corner2.y

    x3 = ray_origin.x
    y3 = ray_origin.y
    x4 = ray_origin.x + ray_direction.x
    y4 = ray_origin.y + ray_direction.y

    npx.line(corner1, corner2, RED)

    npx.line(ray_origin,
             ray_finalpoint, RED)

    denominateur = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if denominateur == 0:
        return None

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominateur
    u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1 - x3)) / denominateur

    print('den: %s t: %s u: %s' % (denominateur, t, u))

    if t > 0 and t < 1 and u > 0:
        return True


class Main:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=60)
        self.starting_time = time()
        self.previous_time = self.starting_time

        self.player = Player(Vec2(WIDTH/2, HEIGHT/2), Vec2(10, 10))
        self.bloc = Entity(Vec2(WIDTH/2, HEIGHT/4*3), Vec2(20, 5), CYAN)

        px.run(self.update, self.draw)

    def update(self):
        px.mouse(True)

        actual_time = time()
        dt = actual_time - self.previous_time
        self.previous_time = actual_time

        self.player.update(dt, 30)
        # print(self.player.upperleftcorner.x, self.player.downleftcorner.x,
        #       self.player.upperrightcorner.x, self.player.upperrightcorner.y)

        self.ray_dir = Vec2(1, 1)
        if raycast(self.player.downleftcorner, self.ray_dir*10,
                   self.bloc.upperleftcorner, self.bloc.upperrightcorner):
            print('WAW')

        if px.btnp(px.KEY_ESCAPE):
            px.quit()

    def draw(self):
        px.cls(0)
        self.bloc.draw()
        self.player.draw()
        # self.player.debug()
        # self.bloc.debug()

        raycast(self.player.downleftcorner, self.ray_dir * 10,
                self.bloc.upperleftcorner, self.bloc.upperrightcorner)


Main()
