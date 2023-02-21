""" Exercícios - Pense en Python - Arquivos.
"""

from __future__ import print_function, division

import shelve
import sys

from anagram_sets import all_anagrams, signature


def store_anagrams(filename, anagram_map):
    """Armazena os anagramas de um dicionário em uma prateleira(shelf).
     filename: string nome do arquivo da prateleira(shelf).
     anagram_map: dicionário que mapeia strings para uma lista de anagramas.
    """
    
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Procura uma palavra em uma prateleira e retorna uma lista de seus anagramas.
     filename: string nome do arquivo da prateleira.
     word: palavra para procurar.
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


    if __name__ == '__main__':
        main(*sys.argv[0])