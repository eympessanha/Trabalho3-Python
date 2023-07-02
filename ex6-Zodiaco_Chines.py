# a. Crie uma lista com os signos do zodiaco;
# b. Crie uma lista com a data de aniversário dos membros de sua família;
# c. Faça um programa que, usando as listas criadas nos itens a e b, mostre o signo de cada membro de sua família.

signos = ['macaco','galo','cao','porco','rato','boi','tigre','coelho','dragao','serpente','cavalo','carneiro']
aniversario = []
q = int(input("Informe a quantidade de datas a serem armazenadas: "))

for c in range(0,q,1):
    a = int(input("Informe o ano do nascimento: "))
    aniversario.append(a)

for a in aniversario:
    i = (a % 12)
    s = signos[i]
    print("Data de nascimento: ",a," - Signo: ",s)
