# Faça um programa que percorre uma lista com o seguinte formato: [ [‘Brasil’, ‘Italia’, [10,9] ],[ [ ‘Brasil’, ‘Espanha’, [5,7] ], [ [ ‘Italia’, ‘Espanha’,[7,8] ]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.
# O programa deve exibir na tela:
# a. O total de faltas do campeonato;
# b. O time que fez mais faltas;
# c. O time que fez menos faltas.

def obter_informacoes(lista):
    total_faltas = 0
    faltas_por_time = {}

    for jogo in lista:
        time1, time2, faltas = jogo

        total_faltas += sum(faltas)

        faltas_por_time[time1] = faltas_por_time.get(time1, 0) + faltas[0]
        faltas_por_time[time2] = faltas_por_time.get(time2, 0) + faltas[1]

    time_mais_faltas = max(faltas_por_time, key=faltas_por_time.get)
    time_menos_faltas = min(faltas_por_time, key=faltas_por_time.get)

    print("Total de faltas do campeonato:", total_faltas)
    print("Time com mais faltas:", time_mais_faltas)
    print("Time com menos faltas:", time_menos_faltas)

lista_jogos = [
    ['Brasil', 'Italia', [10, 9]],
    ['Brasil', 'Espanha', [5, 7]],
    ['Italia', 'Espanha', [7, 8]]
]

obter_informacoes(lista_jogos)
