# Criar um algoritmo de votação para ps, xbos e nintendo

print("Vote no console preferido:")
print("Digite 1 para Nintendo")
print("Digite 2 para Playstation")
print("Digite 3 para Xbox")

voto1 = int(input("Vote no seu console membro 1: "))
voto2 = int(input("Vote no seu console membro 2: "))
voto3 = int(input("Vote no seu console membro 3: "))
voto4 = int(input("Vote no seu console membro 4: "))
voto5 = int(input("Vote no seu console membro 5: "))

nintendo = int()
playstation = int()
xbox = int()

if voto1 == 1:
    nintendo += 1
elif voto1 == 2:
    playstation += 1
elif voto1 == 3:
    xbox += 1

if voto2 == 1:
    nintendo += 1
elif voto2 == 2:
    playstation += 1
elif voto2 == 3:
    xbox += 1

if voto3 == 1:
    nintendo += 1
elif voto3 == 2:
    playstation += 1
elif voto3 == 3:
    xbox += 1

if voto4 == 1:
    nintendo += 1
elif voto4 == 2:
    playstation += 1
elif voto4 == 3:
    xbox += 1

if voto5 == 1:
    nintendo += 1
elif voto5 == 2:
    playstation += 1
elif voto5 == 3:
    xbox += 1

print("O nintendo recebeu {} votos, ps recebeu {} votos e o xbox recebeu {} votos".format(nintendo, playstation, xbox))

if playstation > nintendo and playstation > xbox:
    print("O console escolhido foi o playstation.")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o nintendo")
elif xbox > nintendo and xbox > playstation:
    print("O console escolhido foi o xbox")
else:
    print("Houve empate deve haver nova votação.")