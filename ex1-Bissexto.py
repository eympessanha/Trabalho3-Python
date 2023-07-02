# Faça um programa que calcule o número de dias corridos entre duas datas, para vários pares de datas, considerando a possibilidade de ocorrência de anos bissextos, sendo que:
# A primeira data é sempre a mais antiga;
# O ano é fornecido com 4 dígitos;
# A data fornecida com ZERO dias é o sinal para encerrar a entrada de dados.

#função para saber se o ano é bissexto
def bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False


# Função para calcular o número de dias entre duas datas
def contagem(data1, data2):
    """
    Calcula o número de dias corridos entre duas datas.
    """
    dia1, mes1, ano1 = data1
    dia2, mes2, ano2 = data2

    dias = 0

    while data1 != data2:
        dias += 1
        dia1 += 1

        if dia1 > 31:
            dia1 = 1
            mes1 += 1

            if mes1 > 12:
                mes1 = 1
                ano1 += 1

        if mes1 == 2 and dia1 > 28:
            if bissexto(ano1) and dia1 == 29:
                continue
            dia1 = 1
            mes1 += 1

        if mes1 in {4, 6, 9, 11} and dia1 > 30:
            dia1 = 1
            mes1 += 1

        if mes1 > 12:
            mes1 = 1
            ano1 += 1

        data1 = (dia1, mes1, ano1)

    return dias


# Função para receber as datas e calcular o número de dias corridos
def main():
    datas = []
    while True:
        dia = int(input("Digite o dia (0 para sair): "))
        if dia == 0:
            break

        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano (4 digitos): "))

        data = (dia, mes, ano)
        datas.append(data)

    for i in range(len(datas) - 1):
        data1 = datas[i]
        data2 = datas[i + 1]
        dias = contagem(data1, data2)
        print(f"Número de dias corridos entre {data1} e {data2}: {dias}")


# Executa o programa principal
if __name__ == '__main__':
    main()
