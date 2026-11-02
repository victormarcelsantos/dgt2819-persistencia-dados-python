import time

# a) Lista de palavras (classe list())
palavras = list()

# b) Lê o arquivo linha a linha com "with"
with open("documento.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # c) Separa a linha em palavras
        for palavra in linha.split():
            # d) Guarda cada palavra na lista
            palavras.append(palavra)

print(f"Total de palavras lidas: {len(palavras)}\n")


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux


def selectionSort(array):
    for i in range(len(array)):
        menor = i
        for j in range(i + 1, len(array)):
            if array[menor] > array[j]:
                menor = j
        aux = array[i]
        array[i] = array[menor]
        array[menor] = aux


# e) Cada método recebe uma CÓPIA da lista original,
#    para todos partirem da mesma lista desordenada.

# --- Bubble Sort ---
lista_bubble = palavras.copy()
inicio = time.perf_counter()
bubbleSort(lista_bubble)
tempo_bubble = time.perf_counter() - inicio

# --- Selection Sort ---
lista_selection = palavras.copy()
inicio = time.perf_counter()
selectionSort(lista_selection)
tempo_selection = time.perf_counter() - inicio

# --- sort nativo ---
lista_sort = palavras.copy()
inicio = time.perf_counter()
lista_sort.sort()
tempo_sort = time.perf_counter() - inicio

# f) e g) Resultados e tempos
print("=== BUBBLE SORT ===")
print(lista_bubble)
print(f"Tempo: {tempo_bubble:.6f} segundos\n")

print("=== SELECTION SORT ===")
print(lista_selection)
print(f"Tempo: {tempo_selection:.6f} segundos\n")

print("=== SORT NATIVO ===")
print(lista_sort)
print(f"Tempo: {tempo_sort:.6f} segundos\n")

print("=== COMPARATIVO ===")
print(f"Bubble Sort:    {tempo_bubble:.6f} s")
print(f"Selection Sort: {tempo_selection:.6f} s")
print(f"sort nativo:    {tempo_sort:.6f} s")