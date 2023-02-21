""" Exercício Pense en Python - Arquivos - Anagramas.
"""

from __future__ import print_function, division


def signature(s):
    """Retorna a assinatura desta string.
    Assinatura é uma string que contém todas as letras em ordem.
    s: string
    """
    # TODO: reescrever usando sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Localiza todos os anagramas em uma lista de palavras.
    filename: string nome do arquivo da lista de palavras.
    Retorna: um mapa de cada palavra para uma lista de seus anagramas.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: reescrever usando defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Imprime os conjuntos de anagramas em d.
    d: mapa de palavras para lista de seus anagramas.
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Imprime os conjuntos de anagramas em d em ordem decrescente de tamanho.
    d: mapa de palavras para lista de seus anagramas.
    """
    # faz uma lista de (length, pares de palavras).
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # classificar em ordem crescente de comprimento.
    t.sort()

    # imprimir a lista ordenada.
    for x in t:
        print(x)


def filter_length(d, n):
    """Selecione apenas as palavras em d que possuem n letras.
     d: mapa da palavra para a lista de anagramas.
     n: número inteiro de letras.
     retorna: novo mapa da palavra para a lista de anagramas.
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
    
