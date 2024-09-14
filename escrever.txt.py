# Abrindo (ou criando) um arquivo de texto chamado 'texto.txt' no modo de escrita ('w')
arquivo = open("texto.txt", "w")

# Criando uma lista para armazenar frases
texto = list()

# Usando o método append para adicionar algumas frases
texto.append("O sol brilha intensamente hoje.\n")
texto.append("A casa e azul e tem um jardim.\n")
texto.append("Os gatos gostam de dormir no sofa.\n")
texto.append("A comida estava deliciosa e quente.\n")
texto.append("Vou ao mercado comprar algumas frutas.\n")

# Escrevendo o conteúdo da lista no arquivo
arquivo.writelines(texto)

# Fechando o arquivo
arquivo.close()

print("Conteudo escrito com sucesso no arquivo 'texto.txt'.")
