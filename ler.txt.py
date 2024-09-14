# Abrindo o arquivo 'loremipsum.txt' com o método open
arquivo = open("loremipsum.txt", "r")

# Imprimindo todo o conteúdo do arquivo
conteudo = arquivo.read()
print("Conteúdo completo do arquivo:\n", conteudo)

# Fechando o arquivo
arquivo.close()

# Abrindo o arquivo novamente para ler a primeira linha
arquivo = open("loremipsum.txt", "r")
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:\n", primeira_linha)

# Fechando o arquivo
arquivo.close()

# Abrindo o arquivo novamente para ler os 3 primeiros caracteres
arquivo = open("loremipsum.txt", "r")
tres_primeiros_caracteres = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:\n", tres_primeiros_caracteres)

# Fechando o arquivo
arquivo.close()

# Utilizando a instrução 'with' para abrir o arquivo e ler seu conteúdo
with open("loremipsum.txt", "r") as arquivo:
    conteudo_com_with = arquivo.read()
    print("\nConteúdo lido com 'with':\n", conteudo_com_with)
