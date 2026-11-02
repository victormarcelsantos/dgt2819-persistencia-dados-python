import random

# a) Array de 15 inteiros aleatórios, não ordenados
numeros = [random.randint(1, 100) for _ in range(15)]
print("Original:   ", numeros)

# b) Ordenação crescente com sort()
numeros.sort()

# c) Imprime e confere
print("Crescente:  ", numeros)

# d) Ordenação decrescente
numeros.sort(key=None, reverse=True)

# e) Imprime e confere
print("Decrescente:", numeros)

# f) Arrays de strings
print("\n--- ARRAYS DE STRINGS ---")

nome = ["Carlos", "Ana", "Beatriz", "Daniel", "Eduarda"]
dataNascimento = ["15/03/1990", "02/11/1985", "27/07/2000", "09/01/1978", "30/12/1995"]
cpf = ["529.982.247-25", "111.444.777-35", "390.533.447-05", "123.456.789-09", "987.654.321-00"]
rg = ["MG-12.345.678", "MG-98.765.432", "MG-11.222.333", "MG-44.555.666", "MG-77.888.999"]

listas = {
    "nome": nome,
    "dataNascimento": dataNascimento,
    "cpf": cpf,
    "rg": rg,
}

for titulo, lista in listas.items():
    print(f"\n{titulo}")
    print("Original:   ", lista)

    lista.sort()
    print("Crescente:  ", lista)

    lista.sort(key=None, reverse=True)
    print("Decrescente:", lista)