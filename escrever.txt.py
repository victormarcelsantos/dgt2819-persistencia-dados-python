# a) Abre (e cria) o arquivo texto.txt em modo escrita ("w")
arquivo = open("texto.txt", "w", encoding="utf-8")

# b) Cria a lista
texto = list()

# c) Adiciona frases com append (o \n quebra a linha)
texto.append("Python é uma linguagem versátil.\n")
texto.append("Persistência de dados é guardar informações em arquivos.\n")
texto.append("Algoritmos de ordenação organizam dados.\n")

# d) Escreve a lista no arquivo
arquivo.writelines(texto)

arquivo.close()
print("Arquivo texto.txt criado com sucesso!")