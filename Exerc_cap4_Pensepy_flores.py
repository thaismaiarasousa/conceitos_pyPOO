"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle

from Exerc_cap4_Pensepy_formasgeométricas import arc


def petal(t, r, angle):
    """Desenha uma pétala com dois arcos.
    t: Turtle.
    r: raio do arco.
    angle: ângulo (graus) que subentende os arcos.
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Desenha uma flor com n pétalas.
    t: Turtle.
    n: número de pétalas.
    r: radio dos arcos.
    angle: ângulo (graus) que subentende os arcos.
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """Move o Turtle para frente (length) sem deixar rastros.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

# Desenha uma sequência de 3 flores.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
