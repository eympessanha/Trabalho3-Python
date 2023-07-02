# Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor fazendo um shift para a direita. Além disso, o vetor deve ser considerado circular, ou seja, o valor da última célula passa a ser o valor da primeira.

import random

# Função para realizar o shift circular para a direita
def shift_direita(vetor):
    ultimo_elemento = vetor[-1]
    for i in range(len(vetor)-1, 0, -1):
        vetor[i] = vetor[i-1]
    vetor[0] = ultimo_elemento

# Preenchendo o vetor com números aleatórios entre 0 e 20
vetor = []
for _ in range(10):
    vetor.append(random.randint(0, 20))

print("Vetor original:", vetor)

# Realizando o shift circular para a direita
shift_direita(vetor)

print("Vetor manipulado:", vetor)
