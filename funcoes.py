# 1: transformar a posicao inicial, a orientacao e o tamanho em uma lista com todas as posicoes do navio.

def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = [] # lista vazia para receber as posicoes do navio


    for i in range(tamanho):

        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])

        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])

    return posicoes

# 2: adiciona um navio ao dicionario frota.

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

# aqui a variavel posicoes guarda os valores devolvidos pela funcao da questao 1 (define_posicoes)

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
# exemplo: define_posicoes vai devolver [ [2,4], [2,5], [2,6] ] e a variavel posicoes vai armazenar esse valor

    if nome_navio in frota:

# verifica se o navio esta presente no dicionario frota
# se estiver, o navio sera adicionado na variavel posicoes

        frota[nome_navio].append(posicoes)

    else:
# caso contrario, ele cria a chave e adiciona o primeiro navio nela
        frota[nome_navio] = [posicoes]

    return frota

# 3: verifica se existe um navio na posicao escolhida

def faz_jogada(tabuleiro, linha, coluna):

# significado dos simbolos -> 0: posicao vazia / 1: existe um navio / x: o jogador acertou um navio / - : o jogador atirou na agua

    if tabuleiro[linha][coluna] == 1:
# caso o jogador acerte
        tabuleiro[linha][coluna] = "X"

    else:
# caso o jogador erre
        tabuleiro[linha][coluna] = "-"

    return tabuleiro

# 4: 

def posiciona_frota(frota):

    tabuleiro = []

    for i in range(10):
        linha = []

        for j in range(10):
            linha.append(0)

        tabuleiro.append(linha)

    for nome_navio in frota:

        for navio in frota[nome_navio]:

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    quantidade = 0

    for tipo in frota:
        for navio in frota[tipo]:
            afundou = True

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundou = False

            if afundou:
                quantidade += 1

    return quantidade

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9:
            return False

        if posicao[1] < 0 or posicao[1] > 9:
            return False

    for tipo in frota:
        for navio in frota[tipo]:
            for posicao_ocupada in navio:
                if posicao_ocupada in posicoes:
                    return False
    return True