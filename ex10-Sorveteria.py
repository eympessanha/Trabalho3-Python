# Uma sorveteria vende cinco produtos diferentes, cada um com um preço de acordo com a tabela abaixo:
#Código  Produto         Preço (R$)
#  A   Refrigerante         3,50
#  B   Casquinha Simples    4,00
#  C   Casquinha Dupla      5,50
#  D   Sundae               7,50
#E Banana Split             9,00
# Faça um programa que processe diversas vendas, lembrando que cada venda efetuada pode ser composta por diversas unidades de diversos produtos. O programa deverá utilizar:
#a. uma função que apresente na tela um menu indicando os preços dos produtos. Esse menu deve ser apresentado no início de cada venda;
#b. uma função que processe cada venda individual e forneça o valor a pagar;
#c. uma terceira função que emita um relatório no final do dia, informando dados gerais das vendas do dia (número total de itens vendidos de cada produto, total pago para cada produto, total arrecadado e valor médio de cada compra).

# Cria um dicionario com as preços
precos = {'A': 3.50, 'B': 4.00, 'C': 5.50, 'D': 7.50, 'E': 9.00}

# Cria um dicionario para ver as infromações da venda
vendas_dia = {'A': {'quantidade': 0, 'total_pago': 0.0},
              'B': {'quantidade': 0, 'total_pago': 0.0},
              'C': {'quantidade': 0, 'total_pago': 0.0},
              'D': {'quantidade': 0, 'total_pago': 0.0},
              'E': {'quantidade': 0, 'total_pago': 0.0}}


# Função para exibir o menu com os preços dos produtos
def exibir_menu():
    print("Código  Produto          Preço (R$)")
    for codigo, preco in precos.items():
        produto = nome_produto(codigo)
        print(f"  {codigo}      {produto}         {preco:.2f}")


# Função para assimilar o codigo com o produto
def nome_produto(codigo):
    if codigo == 'A':
        return 'Refrigerante'
    elif codigo == 'B':
        return 'Casquinha Simples'
    elif codigo == 'C':
        return 'Casquinha Dupla'
    elif codigo == 'D':
        return 'Sundae'
    elif codigo == 'E':
        return 'Banana Split'


# Função para ver cada venda
def processar_venda():
    venda_atual = {}
    valor_total = 0.0

    while True:
        exibir_menu()
        codigo = input("Digite o código do produto ou 'sair' para encerrar: ")

        if codigo.lower() == 'sair':
            break

        if codigo in precos:
            quantidade = int(input("Digite a quantidade: "))
            preco_unitario = precos[codigo]
            total_produto = preco_unitario * quantidade
            venda_atual[codigo] = {'quantidade': quantidade, 'total': total_produto}
            valor_total += total_produto
        else:
            print("Código inválido!")

    # Atualiza os dados gerais das vendas do dia
    for codigo, venda in venda_atual.items():
        vendas_dia[codigo]['quantidade'] += venda['quantidade']
        vendas_dia[codigo]['total_pago'] += venda['total']

    return valor_total


# Função para emitir o relatório no final do dia
def emitir_relatorio():
    total_arrecadado = sum(venda['total_pago'] for venda in vendas_dia.values())
    numero_total_itens = sum(venda['quantidade'] for venda in vendas_dia.values())
    valor_medio_compra = total_arrecadado / numero_total_itens

    print("===== Relatório do Dia =====")
    print("Código  Produto          Quantidade   Total Pago")
    for codigo, venda in vendas_dia.items():
        produto = nome_produto(codigo)
        print(f"  {codigo}      {produto}         {venda['quantidade']:5d}       R${venda['total_pago']:.2f}")
    print("-----------------------------")
    print(f"Total arrecadado: R${total_arrecadado:.2f}")
    print(f"Valor médio de compra: R${valor_medio_compra:.2f}")
    print("============================")


# menu inicial para decidir o que fazer
while True:
    opcao = input("Digite 0 para iniciar uma nova venda ou 1 para emitir o relatório do dia: ")

    if opcao == '0':
        valor_pago = processar_venda()
        print(f"Valor total a pagar: R${valor_pago:.2f}")
    elif opcao == '1':
        emitir_relatorio()
    else:
        print("Opção inválida!")
