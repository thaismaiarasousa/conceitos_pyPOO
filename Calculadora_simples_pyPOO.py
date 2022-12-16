"""Calculadora simples em Python"""


def somar(elementos):
    soma=0
    for i in elementos:
        soma=soma+i
    return print(soma)


def multiplicar(elementos):
   
    mult = 1
    for i in elementos:
        mult = mult*i
    return print(mult)


def subtrair(a,b):
    return print(f'O resultado da sua subtração é: {a-b}')



def dividir(a,b):

    return print(f'O resultado da sua divisão é: {a/b}')



def main(accion):
    
    if acao == 'som':
        somar(elementos)
    elif acao == 'sub':
        subtrair(a,b)
    elif acao == 'm':
        multiplicar(elementos)
    else:
        dividir(a,b)
    return
   

if __name__ == "__main__":
    #Já que o arquivo fonte está sendo executado como programa principal,
    # se estabelece a variável especial __name__ para que tenha um valor
    # "__main__". Se este arquivo é importado de outro módulo __name__ se estabelecerá
    # no nome do módulo, sendo, este último, valor para a variável __name__.

    print('Somar -------------------->  Som')
    print('Subtrair ----------------->  Sub')
    print('Multiplicar -------------->  M')
    print('Dividir ------------------>  D')

    acao = input('Que operação deseja realizar? : ')
    acao = acao.lower()
    
    if acao =='som'or acao =='m':

        x = int(input('Quantos elementos deseja ingressar: '))

        elementos = []
        for i in range(x):
            X=int(input(f'Ingresse seu {i+1} número: '))
            elementos.append(X)
        print(elementos)
        main(acao)
    elif acao=='sub'or acao=='d':
        a = float(input('Ingresse sua primeira variável: '))
        b = float(input('Ingresse sua segunda variável: '))
        main(acao)
    else:
        print('ERROR: Você ingressou uma opção incorreta')
