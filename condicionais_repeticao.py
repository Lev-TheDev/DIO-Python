# identação e blocos em Python
# 4 espaços para cada nível de indentação
# início de bloco: dois pontos (:)
# fim de bloco: recuo (indentação) volta ao nível anterior

# estruturas condicionais
# permitem o desvio do fluxo de execução do programa quando uma condição é verdadeira ou falsa
# if, elif, else
import sys


saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
if saque > saldo:
    print("Saldo insuficiente!")
elif saque <= 0:
    print("Valor de saque inválido!")
else:
    saldo -= saque
    print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")

opcao = int(input("Escolha uma opção: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
    saque = float(input("Informe o valor do saque: "))
    if saque > saldo:
        print("Saldo insuficiente!")
    elif saque <= 0:
        print("Valor de saque inválido!")
    else:
        saldo -= saque
        print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
elif opcao == 2:
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
else:
    sys.exit("Opção inválida!")

# if ternário
# sintaxe: valor_se_verdadeiro if condicao else valor_se_falso
numero = 10
paridade = "Par" if numero % 2 == 0 else "Ímpar"
print(f"O número {numero} é {paridade}.")

# Estruturas de repetição
print("========= Estruturas de repetição =========")
# permitem executar um bloco de código várias vezes
# while, for
# while: executa enquanto a condição for verdadeira
contador = 10
while contador < 20:
    print(f"Contador: {contador}")
    contador += 1
# for: itera sobre uma sequência (lista, tupla, string, etc.)
for i in range(1, contador+1):
    print(f"Iteração: {i}")
# range: função built-in que gera uma sequência de números
# range(início, fim, passo) ou range(fim) para gerar de 0 até fim-1
# exemplo: range(5) gera [0, 1, 2, 3, 4]
# exemplo: range(1, 5) gera [1, 2, 3, 4]
# exemplo: range(1, 10, 2) gera [1, 3, 5, 7, 9]

texto = input("Digite um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end="-")
print()

# tabuada
numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")