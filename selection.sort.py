# Função para realizar a ordenação utilizando o algoritmo selection sort
def selection_sort(array):
    # Laço para iterar nos elementos do array
    for i in range(len(array)):
        # Variável que recebe a posição "i"
        min_index = i

        # Laço para iterar a partir da posição i+1 até o final do array
        for j in range(i + 1, len(array)):
            # Verifica se o valor na posição min_index é maior que o valor na posição j
            if array[min_index] > array[j]:
                # Atribui a min_index a posição de j
                min_index = j

        # Trocando os valores das posições i e min_index
        array[i], array[min_index] = array[min_index], array[i]


# Array de 15 números inteiros sem ordenação
array_numeros = [29, 10, 14, 37, 13, 25, 18, 6, 50, 45, 30, 21, 8, 12, 40]

# Imprimindo o array antes da ordenação
print("\nArray não ordenado:", array_numeros)

# Aplicando o algoritmo selection sort
selection_sort(array_numeros)

# Imprimindo o array ordenado
print("\nArray ordenado:", array_numeros)
