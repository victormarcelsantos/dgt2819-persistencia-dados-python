# Variável recebendo o arquivo aberto com open()
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

# Todo o conteúdo
print("=== CONTEÚDO COMPLETO ===")
print(arquivo.read())

# read() leva o cursor ao final; seek(0) volta ao início
arquivo.seek(0)

# Apenas a primeira linha
print("\n=== PRIMEIRA LINHA ===")
print(arquivo.readline())

arquivo.seek(0)

# Apenas os 3 primeiros caracteres
print("=== 3 PRIMEIROS CARACTERES ===")
print(arquivo.read(3))

# Sempre feche o arquivo aberto com open()
arquivo.close()

# Usando "with": fecha o arquivo automaticamente
print("\n=== USANDO WITH ===")
with open("loremipsum.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

print(conteudo)