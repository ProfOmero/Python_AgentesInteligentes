from Geral import cls, parada

while True:
    cls()

    nomeDoArquivo = input("Digite o nome do arquivo (ou 'FIM' para encerrar) = ")
    if (nomeDoArquivo.upper() == "FIM"):
        break

    print()

    try:
        arquivo = open(nomeDoArquivo, "r")
        linhas = arquivo.readlines()
        print("*** Conteúdo do arquivo ***")
        for linha in linhas:
            print(linha, end="")

        parada()
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não encontrado:", nomeDoArquivo)
        parada()