from random import randint, uniform

# Calcula probabilidade de ganhar e de perder
# Recebe:
# Pts de ataque do atacante
# Pts de defesa do defensor
# Devolve:
# Probabilidade do atacante vencer
# Probabilidade do defensor vencer
def calc_prob(attack, defense):
    divisor = attack + defense

    prob_atac = (100*attack) / (divisor)
    prob_def = (100*defense) / (divisor)

    return prob_atac, prob_def

# Escolhe quem sera a kvutza vizinha que esta sendo atacada
# Recebe:
# Lista dos vizinhos do atacante
# Devolve:
# Kvutza que sera atacada
def choose_def(vizinhos):
    kvutza = randint(0,len(vizinhos)-1)
    return vizinhos[kvutza]

# Atualiza as listas de vizinhos
# Recebe:
# String: Quem ganhou
# String: Quem perdeu
# Dicionario: Vizinhos
# Lista: Grupos ainda vivos
# Devolve:
# Dicionario: Vizinhos atualizado
# Lista: Grupos ainda vivos atualizada
def update_war(win,lost, vizinhos, war_g):
    # print("1 --- ",vizinhos)
    for i in vizinhos:
        if (lost in vizinhos[i]):
            vizinhos[i].remove(lost)
            if ((i != win) and not (i in vizinhos[i])):
                vizinhos[i].append(win)
    
    # print("2 --- ",vizinhos)
    
    for i in vizinhos[lost]:
        if ((i != win) and not (i in vizinhos[win])):
            vizinhos[win].append(i)

    # print("VAI DELETAR")
    del vizinhos[lost]
    war_g.remove(lost)
    
    # print("3 --- ",vizinhos)
    return vizinhos, war_g