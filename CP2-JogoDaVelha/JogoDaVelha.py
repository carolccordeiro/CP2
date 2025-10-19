def exibir_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    # Verificar colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)

def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " "

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida! Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Trocar jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()