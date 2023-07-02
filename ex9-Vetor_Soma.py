# Faça um programa que preenche um vetor de 10 posições com números aleatórios entre 0 e 20. Após o preenchimento, o programa deve manipular os valores de cada posição do vetor da seguinte forma: cada célula é a soma dela mesma e das células anteriores. Imprima o vetor antes e depois da manipulação.

import random

lista = [random.randrange(1,20,1) for i in range(10)]
print("Vetor original: ",lista)

for i in range(1,10,1):
    lista[i]= lista[i]+lista[i-1]

print("Vetor manipulado: ",lista)
