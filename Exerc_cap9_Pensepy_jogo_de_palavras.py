""" 
Exercício cap. 9 - Pense em Python (jogo de palavras).

"""

# Importo as variáveis print_function e division do módulo __future__ para 
# garantir a compatibilidade com outras versões de python.
from __future__ import print_function, division


def true_triple_doble(word):
    """Testa se uma palavra contém três letras duplas consecutivas.
    
    word: string
    returns: boolean
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def buscar_triple_doble():
    """Lê uma lista de palavras e imprime palavras com letras duplas triplas."""
    buscar = open('words.txt', encoding="utf-8")
   
    for line in buscar:
        word = line.strip() # retorna a lista das strings s usando os 
        # caracteres em BRANCO como separadores.
        if true_triple_doble(word):
            print(word)


print('Aqui estão todas as palavras da lista que')
print('têm três letras duplas consecutivas.')
buscar_triple_doble()
print('')

