# // divisão inteira
# % módulo (resto da divisão)
# ** exponenciação

print("-------- operadores aritméticos --------")
# operadores aritméticos
a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
exponenciacao = a ** b

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Módulo: {modulo}")
print(f"Exponenciação: {exponenciacao}")

# precedência dos operadores
print("-------- precedência dos operadores --------")
# A precedência dos operadores determina a ordem em que as operações são realizadas.
# Operadores com maior precedência são executados primeiro.
# A ordem de precedência é a seguinte:
# 1. Parênteses ()
# 2. Exponenciação **
# 3. Multiplicação *, Divisão /, Divisão inteira //, Módulo %
# 4. Adição +, Subtração -

resultado = 2 + 3 * 4 - (5 ** 2) / 2
print(f"Resultado com precedência: {resultado}")

#operadores de comparação
print("-------- operadores de comparação --------")
x = 10
y = 5

igual = x == y
diferente = x != y
maior = x > y
menor = x < y
maior_igual = x >= y
menor_igual = x <= y

print(f"Igual: {igual}")
print(f"Diferente: {diferente}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Maior ou igual: {maior_igual}")
print(f"Menor ou igual: {menor_igual}")

# operadores lógicos
print("-------- operadores lógicos --------")
a = True
b = False

and_op = a and b
or_op = a or b
not_op = not a

print(f"AND: {and_op}")
print(f"OR: {or_op}")
print(f"NOT: {not_op}")

#operadores de identidade
print("-------- operadores de identidade --------")
# Os operadores de identidade são usados para verificar se dois objetos são o mesmo objeto na memória.
# is: verifica se dois objetos são o mesmo objeto.
# is not: verifica se dois objetos não são o mesmo objeto.

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f"x is y: {x is y}")  # True, pois y é uma referência ao mesmo objeto que x
print(f"x is z: {x is z}")  # False, pois z é um novo objeto com o mesmo conteúdo
print(f"x is not z: {x is not z}")  # True, pois x e z não são o mesmo objeto

# operadores de associação
print("-------- operadores de associação --------")
# Os operadores de associação são usados para verificar se um valor está presente em uma sequência (como listas, tuplas ou strings).
# in: verifica se um valor está presente na sequência.
# not in: verifica se um valor não está presente na sequência.

lista = [1, 2, 3, 4, 5]
valor = 3
valor_inexistente = 6

print(f"{valor} in lista: {valor in lista}")  # True
print(f"{valor_inexistente} not in lista: {valor_inexistente not in lista}")  # True