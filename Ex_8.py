# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crie um dicionário com duas chaves: "pares" e "ímpares", onde cada chave terá uma lista com os números correspondentes.


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dicionarios = {
    "pares":[],
    "impares":[]
}

for n in numeros: 
    if n % 2 == 0:
        dicionarios["pares"].append(n)
    else:
        dicionarios["impares"].append(n)
print(dicionarios)