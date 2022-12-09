""" Exercícios cap.4 - Pense em Python"""

from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Desenha um quadrado com os lados do comprimento por definir.
    Aplicando a generalização do comprimento de lado o quadrado pode passar
    a ter qualquer tamanho. O turtle volta para a posição inicial.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def arc(t, r, angle):
    """Desenha um arco com o raio e o ângulo dados.
     t: Turtle.
     r: raio.
     angle: ângulo subtendido pelo arco, em graus.
     Como não podemos usar polygon ou circle para desenhar 
     um arco, uma alternativa é começar com uma cópia de polygon 
     e transformá-la em arc.
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    
    # fazer uma ligeira curva à esquerda antes de começar reduz
    # o erro causado pela aproximação linear do arco.
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


    # Como não podemos usar polygon ou circle para desenhar 
    # um arco, uma alternativa é começar com uma cópia de polygon 
    # e transformá-la em arc. Neste caso, notamos que houve código 
    # semelhante em arc e polygon, então este é fatorado no polyline.


def polyline(t, n, length, angle):
    """Desenha n segmentos de linha.
     t: Objeto Turtle.
     n: número de segmentos de linha.
     length: comprimento de cada segmento.
     angle: graus entre os segmentos.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Desenha um polígono com n lados.
     t: Turtle.
     n: número de lados.
     comprimento: comprimento de cada lado.
     Se refatora polyline 
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


# Finalmente torna-se possível reenscrever circle para usar arc.
def circle(t, r):
    """Desenha um círculo com o raio dado.
     t: Turtle.
     r: raio.

    """
    arc(t, r, 360)


# a seguinte condição verifica se estamos
# executando como um script (executa o código de teste, nesse caso),
# ou sendo importado, caso contrário.

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