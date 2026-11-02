# kdd.py - Glossário de palavras ordenadas
# Lê documento.txt, separa em palavras, ordena com sort()
# (método de melhor performance nos testes) e grava o resultado.

palavras = list()

# Leitura linha a linha
with open("documento.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        for palavra in linha.split():
            palavras.append(palavra)

# Ordenação
palavras.sort()

# Escrita do glossário (uma palavra por linha)
with open("palavras_ordenadas.txt", "w", encoding="utf-8") as saida:
    for palavra in palavras:
        saida.write(palavra + "\n")

print(f"{len(palavras)} palavras ordenadas gravadas em palavras_ordenadas.txt")