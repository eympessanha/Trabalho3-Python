# Faça um programa que preenche um cubo de 50 x 50 x 50 com valores aleatórios entre 0 e 100 e encontre:
#a. a soma dos valores armazenados no cubo;
#b. o número de ocorrências do valor 90;
#c. o maior valor armazenado no cubo;
#d. as posições onde aparecem o maior valor encontrado em (c) – notar que aqui o programa possivelmente imprimirá mais de uma posição.

import random

# Definindo os valores do cubo com o random
cubo = [[[random.randint(0, 100) for _ in range(50)] for _ in range(50)] for _ in range(50)]

# Criação de variaveis
soma = 0
n90 = 0
valorm = 0
posicoesvalorm = []

# Percorrendo o cubo
for i in range(50):
    for j in range(50):
        for k in range(50):
            v = cubo[i][j][k]
            soma += v
            if v == 90:
                n90 += 1
            elif v >= valorm:
                valorm = v
                posicoesvalorm = [(i, j, k)]
                posicoesvalorm.append((i, j, k))

# Exibindo os resultados
print("Soma dos valores no cubo:", soma)
print("Ocorrências do valor 90:", n90)
print("Maior valor armazenado no cubo:", valorm)
print("Posições com o maior valor:")
for p in posicoesvalorm:
    print(p)
