#Colocar pra rodar Grupo.

import turtle as tur
import colorsys as cs
tur.setup(765,765)
tur.speed(0)
tur.tracer(8)
tur.width(2)
tur.bgcolor('black')
for j in range(50):
    for i in range (15):
        tur.color(cs.hsv_to_rgb(i/15,j/50,1))
        tur.right(90)
        tur.circle(50+j*8,90)
        tur.left(90)
        tur.circle(50+j*8,90)
        tur.right(180)
        tur.circle(1,24)
tur.hideturtle()
tur.done()