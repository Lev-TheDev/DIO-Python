curso = "pYthon"
# upper() - deixa todas as letras maiúsculas
print(curso.upper())
# lower() - deixa todas as letras minúsculas
print(curso.lower())
# capitalize() - deixa a primeira letra maiúscula e o resto minúsculo
print(curso.capitalize())
# title() - deixa a primeira letra de cada palavra maiúscula
print(curso.title())
# strip() - remove espaços em branco no início e no fim
curso_com_espaco = "   pYthon   "
print(curso_com_espaco.strip() + "!")
# lstrip() - remove espaços em branco no início
print(curso_com_espaco.lstrip() + "!")
# rstrip() - remove espaços em branco no fim
print(curso_com_espaco.rstrip() + "!")
# replace() - substitui uma substring por outra
print(curso.replace("Y", "y"))
# split() - divide a string em uma lista de substrings
curso_dividido = curso.split("t")
print(curso_dividido)
# join() - junta uma lista de substrings em uma única string
curso_junto = ".t".join(curso_dividido)
print(curso_junto)
# center() - centraliza a string em um campo de largura especificada
print(curso.center(20, "-"))