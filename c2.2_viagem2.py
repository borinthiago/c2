# uma empresa de viagem oferecerá desconto para pessoas que viajam
# juntas. O desconto é sobre o VALOR BRUTO, CATEGORIA DE ASSENTOS e
# QUANTIDADE DE VIAJANTES.

# Economica 2 (3%) 3 (4%) 4 (5%)
# Executiva 2 (5%) 3 (7%) 4 (8%)
# Primeira 2 (10%) 3 (15%) 4 (20%)

# Input e apresentação das variáveis:
import null as null

print("Bem vindos a companhia de viagem, por favor digite:")
viajantes = int(input("Digite a quantidade de viajantes: "))
classe = int(input("Digite 1-[Economica] 2-[Executiva] 3-[Primeira Classe]: "))
valor = float(input("Digite o valor bruto do pacote: "))
print("Você selecionou {} viajantes na classe {} pelo valor de R${}, vamos calcular o desconto.".format(viajantes, classe, valor))

# calculando para classe economica:
if classe == 1:
    if viajantes <= 2:
        valor_desconto = valor * 0.97
    elif viajantes == 3:
        valor_desconto = valor * 0.96
    else:
        valor_desconto = valor * 0.95

# calculando para classe executiva:
elif classe == 2:
    if viajantes <= 2:
        valor_desconto = valor * 0.95
    elif viajantes == 3:
        valor_desconto = valor * 0.93
    else:
        valor_desconto = valor * 0.92

# calculando para primeira classe:
elif classe == 3:
    if viajantes <= 2:
        valor_desconto = valor * 0.90
    elif viajantes == 3:
        valor_desconto = valor * 0.85
    else:
        valor_desconto = valor * 0.80
else:
    print("Categoria inexistente, por favor selecionar outra categoria.")

valor_medio = valor_desconto / viajantes

print("O valor bruto é R${}".format(valor))
print("O valor com desconto é R${}".format(valor_desconto))
print("O valor médio por viajante é de R${}".format(valor_medio))
