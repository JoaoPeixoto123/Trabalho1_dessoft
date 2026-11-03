from funcoes import posicao_valida, preenche_frota


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
                escolha = int(input("[1] Vertical [2] Horizontal >"))

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


print(frota)
