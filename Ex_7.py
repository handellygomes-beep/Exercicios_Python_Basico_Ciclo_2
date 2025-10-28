# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
listas = [
{"Nome" : 'Monsherra',
  "Idade" : 17,
"Cidade" : "New Work"
},

{"Nome" : "Benjamin",
 "Idade" : 10,
 "Cidade" : "Fortaleza"
},

{"Nome" : "Maria Cecilía",
 "Idade" : 7,
 "Cidade" : "Itapevi"
}

]

for lista in listas:
    print(lista["Nome"])
