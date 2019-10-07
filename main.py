import pyxel
from constants import FPS, WIDTH, HEIGHT

pyxel.init(WIDTH, HEIGHT)

def update(FPS=FPS):
    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)