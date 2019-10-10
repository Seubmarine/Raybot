import pyxel


def pix(vector2, col):
    pyxel.pix(vector2.x, vector2.y, col)


def line(position_vector2, second_vector2, col):
    pyxel.line(position_vector2.x, position_vector2.y,
               second_vector2.x, second_vector2.y, col)


def rect(position_vector2, second_vector2, col):
    pyxel.rect(position_vector2.x, position_vector2.y,
               second_vector2.x, second_vector2.y, col)


def rectb(position_vector2, second_vector2, col):
    pyxel.rectb(position_vector2.x, position_vector2.y,
                second_vector2.x, second_vector2.y, col)


def circ(position_vector2, r, col):
    pyxel.circ(position_vector2.x, position_vector2.y, r, col)


def circb(position_vector2, r, col):
    pyxel.circb(position_vector2.x, position_vector2.y, r, col)
