# a) Array com 15 inteiros sem ordenação
array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 41, 3, 58, 19, 86, 30]

print("Antes: ", array)

# b) Primeiro laço
for i in range(len(array)):
    # c) 'menor' guarda a POSIÇÃO do menor valor encontrado (começa em i)
    menor = i

    # d) Segundo laço: percorre o restante do array
    for j in range(i + 1, len(array)):
        # e) Compara o valor na posição 'menor' com o da posição j
        if array[menor] > array[j]:
            # f) Achou um valor menor: atualiza a posição
            menor = j

    # g) Troca o elemento da posição i pelo menor encontrado
    aux = array[i]
    array[i] = array[menor]
    array[menor] = aux

# h) Imprime
print("Depois:", array)