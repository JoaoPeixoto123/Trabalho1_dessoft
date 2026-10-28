def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []

    for i in range(tamanho):

        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])

        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])

    return posicoes