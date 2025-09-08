nome = "Guilherme"
idade = 28
profissao = "Desenvolvedor"
linguagem = "Python"

# Usando %
print("O %s tem %d anos, trabalha como %s e usa a linguagem %s." % (nome, idade, profissao, linguagem))

# Usando .format()
print("O {} tem {} anos, trabalha como {} e usa a linguagem {}.".format(nome, idade, profissao, linguagem))
print("O {0} tem {1} anos, trabalha como {2} e usa a linguagem {3}.".format(nome, idade, profissao, linguagem))

# Usando format com nomes
print("O {nome} tem {idade} anos, trabalha como {profissao} e usa a linguagem {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
#print("O {nome} tem {idade} anos, trabalha como {profissao} e usa a linguagem {linguagem}.".format(**pessoa))

# Usando f-strings (Python 3.6+)
print(f"O {nome} tem {idade} anos, trabalha como {profissao} e usa a linguagem {linguagem}.")

# .2f e espaçamento
PI = 3.14159
print(f"{PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

# fatiamento
print(f"Primeira letra do nome: {nome[0]}")
print(f"Última letra do nome: {nome[-1]}")
print(f"Terceira letra do nome: {nome[2]}")
print(f"Cinco letras do nome: {nome[:5]}")
print(f"A partir da quarta letra do nome: {nome[3:]}")
print(f"Nome com passo 2: {nome[3:8:2]}")
print(f"Nome trás para frente: {nome[::-1]}")

# strings de múltiplas linhas com 3 aspas simples ou duplas
mensagem = f"""
    Olá, meu nome é {nome},
tenho {idade} anos,
trabalho como {profissao}
e uso a linguagem {linguagem}.
"""

print(mensagem)

print(
    '''
    =========== MENU ===========
    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair
    ============================
    
    Obrigado por usar nosso sistema!
    '''
)



