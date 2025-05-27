jogadores=[]
r=[]
jogadas = {
    "ec" : False,
    "em" : False,
    'eb' : False,
    'mc' : False,
    'mm' : False,
    'mb' : False,
    'dc' : False,
    'dm' : False,
    'db' : False
}
vencedor = False

class Jogador:
    def __init__(self, nome, pontos, primeiro):
        self.nome = nome
        self.pontos = pontos
        self.primeiro = primeiro




n1 = str(input("Digite nome do jogador 1: "))
n2 = str(input("Digite nome do jogador 2: "))

verificar_ordem = False

while verificar_ordem == False:
    first = str(input(f"O primeiro jogador sera: [1]{n1} [2]{n2}: "))
    if first == "1" or first == "2":
        verificar_ordem = True
    else:
        print("Digite um valor válido")
        
if first == '1':
    jogador1 = Jogador(n1, "", True)
    jogador2 = Jogador(n2, "", False)
    jogadores.append(jogador1)
    jogadores.append(jogador2)

elif first == '2':
    jogador1 = Jogador(n1, "", False)
    jogador2 = Jogador(n2, "", True)
    jogadores.append(jogador1)
    jogadores.append(jogador2)




def Fazer_Jogada():
    jogada_feita = False
    while jogada_feita == False:
        r.append(str(input(f"Digite a posição da jogada {cont+1}: ")))
        for jogada in jogadas:
            if r[cont] == jogada and jogadas[r[cont]] == False:
                jogadas[r[cont]] = True
                if cont%2==0:
                    for jogador in jogadores:
                        if jogador.primeiro == True:
                            jogador.pontos += r[cont]
                            jogada_feita = True
                else:
                    for jogador in jogadores:
                        if jogador.primeiro == False:
                            jogador.pontos += r[cont]
                            jogada_feita = True
        if jogada_feita == False:
            print("Digite uma jogada possível")
            r.pop()

def Verificar_Vencedor():
    global vencedor
    if cont<=8:
        for jogador in jogadores:
            if jogador.pontos.count("e") == 3 or \
            jogador.pontos.count("d") == 3 or \
            jogador.pontos.count("m") == 4 or \
            jogador.pontos.count("c") == 3 or \
            jogador.pontos.count("b") == 3 or \
            jogador.pontos.count("m") == 2 and jogador.pontos.count("d") == 1 and jogador.pontos.count("e") == 1 and jogador.pontos.count("c") == 1 and jogador.pontos.count("b") == 1:
                print(f"{jogador.nome} venceu!")
                vencedor = True
    else:
        print("Deu velha!")




print("Digite sua jogada com 2 letras (a primeira E para esquerda, M para meio e D para direita. A segunda C para cima, M para meio, B para baixo. Ex: MB=meio embaixo)")
for cont in range(9):
    Fazer_Jogada()
    Verificar_Vencedor()
    if vencedor == True:
        break


