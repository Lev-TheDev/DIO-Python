frutas = ["maçã", "banana", "laranja"]
print(frutas[2])
print(frutas[-1]) # último item
print(frutas[-2]) # penúltimo item

fruits = []
letras = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
print(letras[0:3:2]) # ['p', 't']
numeros = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
carro = ["Ferrari", "F8 Tributo", 2020, 3400000.00, True] # marca, modelo, ano, preço, usado

#lista aninhada = lista de listas
listas = [frutas, numeros, carro]

matriz = [
    [1, "x", 3],
    [4, 5, "y"],
    ["z", 8, 9]
]

print(matriz[0]) # toda a linha 0
print(matriz[0][2]) # elemento da linha 0, coluna 2

veiculos = ["gol", "celta", "uno"]
for v in veiculos:
    print(v)
    
for indice, v in enumerate(veiculos):
    print(f"{indice}: {v}")
    
# criar nova lista com base em uma lista existente
numeros = [1, 2, 32, 4, 5, 98, 7, 12, 44, 3]
pares = []
# versão 1
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # aqui pode-se modificar o valor antes = pares.append(numero*2)
print(pares)
# versão 2
par = [numero for numero in numeros if numero % 2 == 0] # [numero*2 for numero in numeros if numero % 2 == 0]
print(par)

# MÉTODOS DA CLASSE LIST
# append, insert, extend, pop, del, clear, index, count, sort, reverse, copy
linguagens = ["python", "java", "csharp"]
linguagens.append("golang") # adiciona ao final
linguagens.insert(1, "javascript") # adiciona na posição 1
outra = ["ruby", "php", "java"]
linguagens.extend(outra) # adiciona os elementos de outra lista, mesmo que repita
print(linguagens)
linguagens.pop() # remove o último elemento
linguagens.pop(1) # remove o elemento da posição 1
print(linguagens.index("java")) # retorna o índice do elemento na última vez que apareceu
print(linguagens.count("java")) # conta quantas vezes o elemento aparece na lista

linguagens.sort() # ordena a lista em ordem alfabética
linguagens.sort(reverse=True) # ordena a lista em ordem alfabética reversa
linguagens.reverse() # inverte a ordem da lista
linguagens.sort(key=lambda x: len(x)) # ordena pela quantidade de letras
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True) # ordena pela quantidade de letras ao contrário
print(linguagens)

nova = linguagens.copy() # cria uma cópia da lista, com outra instância
print(nova)
nova.remove("java") # remove a primeira ocorrência do elemento
print(nova)
linguagens.clear() # limpa a lista
print(linguagens)
print(len(nova)) # tamanho da lista
print(len(linguagens)) # tamanho da lista
print(type(nova)) # tipo da variável

