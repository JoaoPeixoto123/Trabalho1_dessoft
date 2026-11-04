from funcoes import (
    posicao_valida,
    preenche_frota,
    posiciona_frota,
    faz_jogada,
    afundados
)


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ""
    texto += "   0 1 2 3 4 5 6 7 8 9   0 1 2 3 4 5 6 7 8 9\n"
    texto += "  _____________________ _____________________\n"

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = " ".join(
            [str(item) for item in tabuleiro_jogador[linha]]
        )

        oponente_info = " ".join(
            [
                str(info) if str(info) in "X-" else "0"
                for info in tabuleiro_oponente[linha]
            ]
        )

        texto += (
            f"{linha}| {jogador_info} |"
            f"{linha}| {oponente_info} |\n"
        )

    return texto


# Frota do jogador

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}


ordem_navios = [
    "porta-aviões",
    "navio-tanque",
    "contratorpedeiro",
    "submarino"
]


tamanhos = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1
}


quantidades = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4
}


# Posicionamento dos navios do jogador

for nome_navio in ordem_navios:
    tamanho = tamanhos[nome_navio]
    quantidade = quantidades[nome_navio]

    for i in range(quantidade):
        posicao_aceita = False

        while not posicao_aceita:
            print(
                f"Insira as informações referentes ao navio "
                f"{nome_navio} que possui tamanho {tamanho}"
            )

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome_navio == "submarino":
                orientacao = "vertical"

            else:
                escolha = int(
                    input("[1] Vertical [2] Horizontal >")
                )

                if escolha == 1:
                    orientacao = "vertical"

                else:
                    orientacao = "horizontal"

            posicao_aceita = posicao_valida(
                frota,
                linha,
                coluna,
                orientacao,
                tamanho
            )

            if not posicao_aceita:
                print("Esta posição não está válida!")

        frota = preenche_frota(
            frota,
            nome_navio,
            linha,
            coluna,
            orientacao,
            tamanho
        )


# Frota já definida do oponente

frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],

    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],

    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],

    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


# Criação dos dois tabuleiros

tabuleiro_jogador = posiciona_frota(frota)

tabuleiro_oponente = posiciona_frota(
    frota_oponente
)


# Parte principal do jogo

jogando = True

while jogando:
    print(
        monta_tabuleiros(
            tabuleiro_jogador,
            tabuleiro_oponente
        )
    )

    jogada_valida = False

    while not jogada_valida:
        linha = int(
            input("Jogador, qual linha deseja atacar? ")
        )

        while linha < 0 or linha > 9:
            print("Linha inválida!")

            linha = int(
                input("Jogador, qual linha deseja atacar? ")
            )

        coluna = int(
            input("Jogador, qual coluna deseja atacar? ")
        )

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")

            coluna = int(
                input("Jogador, qual coluna deseja atacar? ")
            )

        if (
            tabuleiro_oponente[linha][coluna] == "X"
            or tabuleiro_oponente[linha][coluna] == "-"
        ):
            print(
                f"A posição linha {linha} e coluna {coluna} "
                "já foi informada anteriormente!"
            )

        else:
            jogada_valida = True

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente,
        linha,
        coluna
    )

    if afundados(tabuleiro_oponente):
        print(
            "Parabéns! Você derrubou todos os navios "
            "do seu oponente!"
        )

        jogando = False
