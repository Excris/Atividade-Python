# for i in range(5):
#     print(f"Repetição número {i}")
# # Saída: imprime de 0 a 4



#Lista = estrutura de dados 
frutas = ['maça','laranja','banana','melão']
numeros = [1, 2, 3, 4]
lista_geral = [ 1, 'test', 3.5]
desordem = [5, 2, 8, 3, 1, 4, 7, 6]

# Como inserir informações na lista
numeros.insert(3, "maça")
# Adiciona valore no final da lista
numeros.append("10")
# Remove os valores internos dentro da lista
frutas.remove("banana")
# Pop seria uma garra de variaveis pega os valores e aplicar em outros lugares.
valor = numeros.pop(1)
#sort ordenar a lista. 
desordem.sort()
print(desordem)
# Saida de Dados
print(frutas)
print(numeros)
print(lista_geral)
# Variavel pop Garra
print(valor)
##
print()