import random

# Criando um array de 15 posições com números inteiros e valores aleatórios
array_inteiros = [random.randint(1, 100) for _ in range(15)]

# Imprimindo o array original
print("Array original de inteiros:\n", array_inteiros)

# Ordenando o array em ordem crescente
array_inteiros.sort()
print("Array de inteiros em ordem crescente:\n", array_inteiros)

# Ordenando o array em ordem decrescente
array_inteiros.sort(reverse=True)
print("Array de inteiros em ordem decrescente:\n", array_inteiros)

# Criando um array de strings
array_strings = ['banana', 'maçã', 'laranja', 'uva', 'abacaxi', 'cereja', 'melancia', 'manga', 'limão', 'morango']

# Imprimindo o array original de strings
print("\nArray original de strings:\n", array_strings)

# Ordenando o array de strings em ordem crescente
array_strings.sort()
print("Array de strings em ordem crescente:\n", array_strings)

# Ordenando o array de strings em ordem decrescente
array_strings.sort(reverse=True)
print("Array de strings em ordem decrescente:\n", array_strings)
