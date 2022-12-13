""" Exercício cap4 - Pense em Python.
Desenhar uma função que desenhe, com um turtle, um espiral."""

import math
import turtle

def espiral(t):
    """ Desenha um espiral."""
    for i in range(1300):
        vt = i / 20 * math.pi
        y = (vt * 5 + 5) * math.sin(vt)
        x = (vt * 5 + 5) * math.cos(vt)
        turtle.goto(x, y) # Move o turtle para uma posição absoluta. 
        # Um objeto com posicionamento absoluto é removido do fluxo normal 
        # do documento. É posicionado automaticamente com relação ao ponto 
        # inicial (canto superior esquerdo) de seu elemento pai.
    bob.exitonclick()

bob=turtle.Turtle()
espiral(bob)
turtle.mainloop()
    
    