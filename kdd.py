import time


# Função para ordenar a lista usando Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Função para ordenar a lista usando Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Criação da lista para armazenar as palavras
palavras = []

# Lendo o conteúdo do arquivo 'exemplo.txt' e armazenando as palavras na lista
with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        palavras.extend(linha.strip().split())


# Função para medir o tempo de execução de uma função de ordenação
def medir_tempo(funcao_ordenacao, lista):
    lista_copia = lista[:]
    inicio = time.time()
    funcao_ordenacao(lista_copia)
    fim = time.time()
    return fim - inicio, lista_copia


# Ordenando com Bubble Sort
tempo_bubble_sort, palavras_bubble_sorted = medir_tempo(bubble_sort, palavras)
print("Bubble Sort:")
print("Tempo de execução:", tempo_bubble_sort)
print("Palavras ordenadas:", palavras_bubble_sorted)

# Ordenando com Selection Sort
tempo_selection_sort, palavras_selection_sorted = medir_tempo(selection_sort, palavras)
print("\nSelection Sort:")
print("Tempo de execução:", tempo_selection_sort)
print("Palavras ordenadas:", palavras_selection_sorted)

# Ordenando com o método nativo sort()
tempo_sort, palavras_sorted = medir_tempo(lambda x: x.sort(), palavras)
print("\nMétodo nativo sort():")
print("Tempo de execução:", tempo_sort)
print("Palavras ordenadas:", palavras_sorted)

# Salvando as palavras ordenadas com o método mais rápido em um novo arquivo
# Escolha o método mais rápido com base no tempo de execução
metodo_mais_rapido = min(
    (("Bubble Sort", tempo_bubble_sort, palavras_bubble_sorted),
     ("Selection Sort", tempo_selection_sort, palavras_selection_sorted),
     ("Método nativo sort()", tempo_sort, palavras_sorted)),
    key=lambda x: x[1]
)

arquivo_saida = "ordenado_por_" + metodo_mais_rapido[0].replace(" ", "_").lower() + ".txt"

with open(arquivo_saida, "w") as f:
    f.write("\n".join(metodo_mais_rapido[2]))

print(f"\nPalavras ordenadas salvas em '{arquivo_saida}'.")
