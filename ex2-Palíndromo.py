# Faça um programa que leia um número inteiro de 5 dígitos e indique se ele é palíndromo (ex.: 15451).

s = input("Digite um número inteiro de 5 dígitos:")
i = 0
f = len(s)-1
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print(s," é palíndromo")
else:
    print(s," não é palíndromo")
