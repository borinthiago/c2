# uma empresa de viagem oferecerá desconto para pessoas que viajam
# juntas. O desconto é sobre o VALOR BRUTO, CATEGORIA DE ASSENTOS e
# QUANTIDADE DE VIAJANTES.

# Economica 2 (3%) 3 (4%) 4 (5%)
# Executiva 2 (5%) 3 (7%) 4 (8%)
# Primeira 2 (10%) 3 (15%) 4 (20%)

# Input e apresentação das variáveis:
print("Bem vindos a companhia de viagem, por favor digite:")
viajantes = int(input("Digite a quantidade de viajantes: "))
classe = int(input("Digite 1-[Economica] 2-[Executiva] 3-[Primeira Classe]: "))
valor = float(input("Digite o valor bruto do pacote: "))
print("Você selecionou {} viajantes na classe {} pelo valor de R${}, vamos calcular o desconto.".format(viajantes, classe, valor))

# calculando para classe economica:
if classe == 1:
    if viajantes == 2:
        valor_desconto = valor * 0.97
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    elif viajantes == 3:
        valor_desconto = valor * 0.96
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    elif viajantes == 4:
        valor_desconto = valor * 0.95
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    else:
        print("O desconto é concedido no máximo em grupos de 4 viajantes")

elif classe == 2:
    if viajantes == 2:
        valor_desconto = valor * 0.95
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    elif viajantes == 3:
        valor_desconto = valor * 0.93
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    elif viajantes == 4:
        valor_desconto = valor * 0.92
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    else:
        print("O desconto é concedido no máximo em grupos de 4 viajantes")


elif classe == 3:
    if viajantes == 2:
        valor_desconto = valor * 0.90
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    elif viajantes == 3:
        valor_desconto = valor * 0.85
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    elif viajantes == 4:
        valor_desconto = valor * 0.80
        valor_medio = valor_desconto / viajantes
        print("O valor com desconto será R$ {}.".format(valor_desconto))
        print("O valor médio por viajante é de R${}.".format(valor_medio))
    else:
        print("O desconto é concedido no máximo em grupos de 4 viajantes")
else:
    print("Você selecionou uma classe que não existe, favor verificar.")