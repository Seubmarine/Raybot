import pyxel as px
import newpixelmodule as npx
from constants import FPS, WIDTH, HEIGHT, WHITE, BLUE, RED, ORANGE, CYAN, PURPLE
from vector import Vector2 as Vec2
from time import time
import math
import os
from gameobjects import Entity, Player


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

    if t > 0 and t < 1 and u > 0:
        return Vec2(x1 + t*(x2 - x1), y1 + t*(y2 - y1))


class Ray:
    """Ray Object that find the point of intersection of a ray and a given 2 points(A 2D wall have 2 point)"""

    def __init__(self, ray_position, ray_direction, wallpoint_a, wallpoint_b):
        self.ray_position = ray_position
        self.ray_direction = ray_direction
        self.wallpoint_a = wallpoint_a
        self.wallpoint_b = wallpoint_b
        self.ray_intersection = raycast(
            self.ray_position, self.ray_direction, self.wallpoint_a, self.wallpoint_b)

    def update(self):
        self.ray_intersection = raycast(
            self.ray_position, self.ray_direction, self.wallpoint_a, self.wallpoint_b)

    def draw(self):
        if self.ray_intersection != None:
            npx.line(self.ray_intersection, self.ray_position, WHITE)


class Main:
    def __init__(self):
        px.init(WIDTH, HEIGHT, fps=60)

        px.load(os.getcwd() + "/assets/Raybot.pyxel")

        self.starting_time = time()
        self.previous_time = self.starting_time

        self.player = Player(Vec2(WIDTH/8*7, HEIGHT/6), Vec2(10, 10))
        self.bloc = Entity(Vec2(100, 38), Vec2(80, 68), CYAN)
        self.rayslist = []
        self.number_of_ray = 36
        self.i = 0
        for _ray in range(self.number_of_ray):  # Number of Rays
            self.ray_dir = Vec2(math.cos(self.i), math.sin(self.i))
            self.rayslist.append(Ray(self.player.downleftcorner, self.ray_dir,
                                     self.bloc.upperleftcorner, self.bloc.downrightcorner))
            self.i += math.radians(360/self.number_of_ray)

        px.run(self.update, self.draw)

    def update(self):
        px.mouse(True)

        actual_time = time()
        dt = actual_time - self.previous_time
        self.previous_time = actual_time

        self.player.update(dt)

        self.mouse = Vec2(px.mouse_x, px.mouse_y)

        for ray in self.rayslist:  # Number of Rays
            ray.ray_position = self.player.downleftcorner
            ray.update()

        if px.btnp(px.KEY_ESCAPE):
            px.quit()

    def draw(self):
        px.cls(0)
        self.bloc.draw()
        self.player.draw()
        self.player.debug()
        for ray in self.rayslist:
            ray.draw()
        self.bloc.debug()

        npx.line(self.bloc.upperleftcorner, self.bloc.downrightcorner, WHITE)


Main()
