"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def draw_pie(t, n, r):
    """Desenha uma torta e se move para a posição à direita.
    
    t: Turtle.
    n: número de segmentos.
    r: comprimento dos raios radiais.
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()


def polypie(t, n, r):
    """Desenha uma pizza dividida em segmentos radiais.

    t: Turtle.
    n: número de segmentos.
    r: comprimento dos raios radiais.
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)  #Desenha um triângulo isósceles. 
        # O Turtle começa e termina no pico, voltado para o meio da base.
        t.lt(angle)


def isosceles(t, r, angle):
    """Desenha um triângulo isósceles. 
    O Turtle começa e termina no pico, voltado para o meio da base.
    
    t: Turtle
    r: comprimento das pernas iguais.
    ângulo: ângulo de meio pico em graus.
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

# desenhar pólipos com vários números de lados
size = 40
draw_pie(bob, n=5, r=size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, r=8, angle=size)

bob.hideturtle()
turtle.mainloop()