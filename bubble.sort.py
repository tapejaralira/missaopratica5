# Método para ordenar o array utilizando o algoritmo Bubble Sort
def bubble_sort(array):
    # Primeiro laço for para iterar pelos elementos do array
    for i in range(len(array)):
        # Segundo laço for para comparar elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Se o elemento atual for maior que o próximo
            if array[j] > array[j + 1]:
                # Troca os elementos de posição
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# Declaração do array de números com 15 posições
array_numeros = [64, 34, 25, 12, 22, 11, 90, 55, 45, 78, 23, 89, 37, 6, 99]

# Imprimindo o array desordenado
print("\nArray desordenado:\n", array_numeros)

# Aplicando o método bubbleSort no array
bubble_sort(array_numeros)

# Imprimindo o array ordenado
print("\nArray ordenado:\n", array_numeros)
