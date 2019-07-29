import utils
import json
from random import randint, uniform

kvutzot = ['anakim','galim','cochavim','iareach','shavitim','guesher','shemesh','lochamim','gamadim','machar','madrichim']

pontos = {}
with open("pontos_kvutzot.json") as json_file:
	data = json.load(json_file)
	for p in data:
		pontos[p] = data[p]

vizinhos = {}
with open("vizinhos.json") as json_file:
	data = json.load(json_file)
	for p in data:
		vizinhos[p] = data[p]

rodada = 1
grupos = len(kvutzot) - 1
while rodada < grupos+1:
    print("\nRODADA: {}".format(rodada))
    n1 = randint(0,len(kvutzot)-1)
    kvutza_ataq = kvutzot[n1]
    pts_ataque = pontos[kvutza_ataq]["ataque"]
    
    kvutza_def = utils.choose_def(vizinhos[kvutza_ataq])
    pts_defesa = pontos[kvutza_def]["defesa"]

    atacante, defensor = utils.calc_prob(pts_ataque,pts_defesa)

    sorteio = uniform(0,100)

    if (sorteio <= atacante):
        # print("Probabilidade de ataque: {0}\nProbabilidade de defesa: {1}\nNúmero escolhido: {2}\n".format(atacante,defensor,sorteio))
        print("A kvutza de {0} ganhou!".format(kvutza_ataq))
        print("A kvutza de {0} perdeu!".format(kvutza_def))
        vizinhos, kvutzot = utils.update_war(kvutza_ataq, kvutza_def, vizinhos, kvutzot)
    else:
        # print("Probabilidade de ataque: {0}\nProbabilidade de defesa: {1}\nNúmero escolhido: {2}\n".format(atacante,defensor,sorteio))
        print("A kvutza de {0} ganhou!".format(kvutza_def))
        print("A kvutza de {0} perdeu!".format(kvutza_ataq))
        vizinhos, kvutzot = utils.update_war(kvutza_def, kvutza_ataq, vizinhos, kvutzot)

    print("#######################################################")
    rodada += 1

print("\n\n\n")
print("            A kvutzá vencedorá foi:")
print("\n\n\n")
print("                 {}".format(kvutzot[0].upper()))
print("\n\n\n")