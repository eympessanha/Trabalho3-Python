# Faça um programa que leia um número inteiro e informe se ele é um número perfeito. Um número n é perfeito se for igual a soma de seus divisores positivos diferentes de n.

print("Verificando se o número é perfeito! \n")

n = int(input("Informe o número: "))
c = n - 1
soma = 0

while c != 0:
    if n % c == 0:
        soma = soma + c
    c -= 1

if soma == n:
    print(n," é um número perfeito!")
else:
    print(n," não é um número perfeito!")

