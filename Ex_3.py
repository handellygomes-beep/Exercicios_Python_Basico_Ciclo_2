# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
qnt_filmes = int(input('quantos filmes deseja adicionar?: '))

cont = 1
while cont <= qnt_filmes:
    nome = input(f' Qual o nome do {cont}º filmes: ')
    filmes.append(nome)
    cont = cont +1

print(filmes)





# LOOP FOR
for i in range(qnt_filmes):
    input("quantos filmes deseja adicionar?:  ")
    filmes.append(nome)
    print(i)