# Foi realizada uma pesquisa em Niterói, com um número indeterminado de pessoas. De cada entrevistado foram colhidos os seguintes dados:
# a. Qual o seu clube de futebol de preferência (1 – Flamengo, 2 – Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros);
# b. Qual o seu salário;
# c. Qual a sua cidade natal (1 – Niterói, 2 – Outra).

import os

print("Ínicio da entrevista!")
f = 1
fla = 0
vas = 0
flu = 0
bot = 0
out = 0
e = 0
n = 0
somafla = 0
somavas = 0
somaflu = 0
somabot = 0
somaout = 0


while f == 1:
    t = int(input("Informe qual é o seu time de futebol de preferência:\n1- Flamengo\n2- Vasco\n3- Fluminense\n4- Botafogo\n5- Outros\n:"))
    s = float(input("Informe qual é seu salário: "))
    c = int(input("Informe qual é sua cidade natal: \n 1 - Niterói \n 2 - Outra \n :"))
    if t == 1:
        fla += 1
        somafla = somafla + s
    elif t == 2:
        vas += 1
        somavas = somavas + s
    elif t == 3:
        flu += 1
        somaflu = somaflu + s
    elif t == 4:
        bot += 1
        somabot = somabot + s
    elif t == 5 and c == 1:
        n += 1
        somaout = somaout + s
    f = int(input("\nPara finalizar as entrevistas, digite 0.\nPara continuar, digite 1: "))
    e += 1
    os.system('cls')

print("\nNúmero de entrevistados que torcem para o Flamengo: ",fla)
print("\nNúmero de entrevistados que torcem para o Vasco: ",vas)
print("\nNúmero de entrevistados que torcem para o Fluminense: ",flu)
print("\nNúmero de entrevistados que torcem para o Botafogo: ",bot)

if fla == 0:
    print("\nMédia salarial dos entrevistados que torcem para o Flamengo: 0")
else:
    medfla = somafla / fla
    print("\nMédia salarial dos entrevistados que torcem para o Flamengo: ", medfla)

if vas == 0:
    print("\nMédia salarial dos entrevistados que torcem para o Vasco: 0")
else:
    medvas = somavas / vas
    print("\nMédia salarial dos entrevistados que torcem para o Vasco: ", medvas)

if flu == 0:
    print("\nMédia salarial dos entrevistados que torcem para o Fluminense: 0")
else:
    medflu = somaflu / flu
    print("\nMédia salarial dos entrevistados que torcem para o Fluminense: ", medflu)

if bot == 0:
    print("\nMédia salarial dos entrevistados que torcem para o Botafogo: 0")
else:
    medbot = somabot / bot
    print("\nMédia salarial dos entrevistados que torcem para o Botafogo: ", medbot)

print("\nNúmero de entrevistados nascidos em Niterói que não torcem para os principais clubes do Rio: ",n)
print("\nNúmero de pessoas entrevistadas: ",e)
