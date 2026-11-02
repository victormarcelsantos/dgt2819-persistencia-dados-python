def bubbleSort(array):
    # Laço externo: repete o processo para cada elemento
    for i in range(len(array)):
        # Laço interno: compara pares vizinhos
        # O "- i - 1" evita comparar o que já foi ordenado no fim
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                # Troca os valores de posição
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux


# Array de 15 posições, fora do método
numeros = [64, 34, 25, 12, 22, 11, 90, 5, 77, 41, 3, 58, 19, 86, 30]

print("Antes: ", numeros)
bubbleSort(numeros)
print("Depois:", numeros)