# modo interativo
# no terminal digite python3 ou python3 -i (nome-do-arquivo.py)
# para sair do modo interativo, digite exit()

# funções dir() e help()
# dir() lista os atributos e métodos de um objeto
# help() exibe a documentação de um objeto
# sair da documentação help() com q
# sair do modo help com enter

age, name = (23, 'Guilherme')
print(f'Meu nome é {name} e tenho {age} anos.')

age = 27
name = 'Giovana'
print(f'Meu nome é {name} e tenho {age} anos.')

# Python não tem keyword para constantes
# por convenção, usa-se letras maiúsculas
PI = 3.14
print(f'O valor de PI é {PI}')

# lista de estados constantes
STATES = ['SP', 'RJ', 'MG', 'RS', 'SC']
print(f'Os estados são: {STATES}')

# boas práticas:
# nomes compostos de variáveis com underline (snake_case)
# nomes de classes em CamelCase
# nomes de funções em snake_case
# nomes de variáveis em snake_case
# nomes de módulos em snake_case
# nomes de pacotes em snake_case
# nomes de métodos em snake_case
# nomes de atributos em snake_case
# nomes de arquivos em snake_case
# nomes de diretórios em snake_case
# nomes de constantes em UPPER_CASE
# nomes de módulos em letras minúsculas
# nomes de pacotes em letras minúsculas

print("-------- convertendo tipos --------")
# convertendo tipos
preco = 10
print(preco)

preco = float(preco)
print(preco)

# se dividir um int por outro int o resultado é um float
preco = 10 / 2
print(preco)

valor = 10.30
print(valor)
valor = int(valor)
print(valor)

# se dividir um inteiro usando duas barras (//) o resultado é um inteiro
valor = 10 // 3
print(valor)

# concatenar strings com inteiro convertido
age = 28
preco = 10.50
print(str(preco))
print(str(age))
texto = f"idade {age} preço {preco}"
print(texto)

# string para número
preco = "10.50"
age = "28"
preco = float(preco)
age = int(age)
print(preco, age)
print(type(preco), type(age))

# entrada e saída de dados (input e print)
print("-------- entrada e saída de dados --------")
name = input("Digite seu nome: ")
print(f"Olá, {name}!")

age = input("Digite sua idade: ")
print(f"Você tem {age} anos.")

name = "Bernardo"
last_name = "Silva"
print("Olá, " + name + " " + last_name + "!")
print(f"Olá, {name} {last_name}!")
print("Olá, {} {}!".format(name, last_name))
print(name, last_name, sep="-", end=".\n")
# end por padrão é \n, mas pode ser alterado
# ou seja, não é necessário usar \n no final de cada print

