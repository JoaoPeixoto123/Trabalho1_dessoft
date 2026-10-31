def define_posicoes(linha, coluna, orientacao, tamanho):

    posicoes = []

    for i in range(tamanho):

        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])

        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(
        
        linha,
        coluna,
        orientacao,
        tamanho
    )

    if nome_navio in frota:

        frota[nome_navio].append(posicoes)

    else:

        frota[nome_navio] = [posicoes]

    return frota