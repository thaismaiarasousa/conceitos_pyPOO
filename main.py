from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Desenha um quadrado com os lados do comprimento dado.
    Retorna o turtle para a posição inicial.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Desenha n segmentos de linha.
     t: Objeto Turtle.
     n: número de segmentos de linha.
     comprimento: comprimento de cada segmento.
     ângulo: graus entre os segmentos.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Desenha um polígono com n lados.
     t: Turtle.
     n: número de lados.
     comprimento: comprimento de cada lado.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Desenha um arco com o raio e o ângulo dados.
     t: Turtle.
     r: raio
     ângulo: ângulo subtendido pelo arco, em graus
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # fazer uma ligeira curva à esquerda antes de começar reduz
    # o erro causado pela aproximação linear do arco
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Desenha um círculo com o raio dado.
     t: Turtle
     r: raio
    """
    arc(t, r, 360)


# a seguinte condição verifica se estamos
# executando como um script, nesse caso, execute o código de teste,
# ou sendo importado, caso em que não.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # desenha um circulo centrado no centro.
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)

    # para aguardar o usuário fechar a janela
    turtle.mainloop()