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

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

class Jogador:
    def __init__(self, nome, pontos, primeiro, simbolo):
        self.nome = nome
        self.pontos = pontos
        self.primeiro = primeiro
        self.simbolo = simbolo




n1 = str(input("Digite nome do jogador 1: "))
n2 = str(input("Digite nome do jogador 2: "))

verificar_ordem = False
verificar_simbolo = False

while verificar_ordem == False:
    first = str(input(f"O primeiro jogador sera: [1]{n1} [2]{n2}: "))
    if first == "1" or first == "2":
        verificar_ordem = True
    else:
        print("Digite um valor válido")

while verificar_simbolo == False:
    simbolo = str(input(f"Quem será o X?: [1]{n1} [2]{n2}: "))
    if simbolo == "1" or simbolo == "2":
        verificar_simbolo = True
    else:
        print("Digite um valor válido")
        
if first == '1':
    jogador1 = Jogador(n1, "", True, "")
    jogador2 = Jogador(n2, "", False, "")
    jogadores.append(jogador1)
    jogadores.append(jogador2)

elif first == '2':
    jogador1 = Jogador(n1, "", False)
    jogador2 = Jogador(n2, "", True)
    jogadores.append(jogador1)
    jogadores.append(jogador2)

if simbolo == "1":
    jogador1.simbolo = "X"
    jogador2.simbolo = "O"

if simbolo == "2":
    jogador1.simbolo = "O"
    jogador2.simbolo = "X"


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
                            Montar_Tabuleiro(r[cont], jogador.simbolo)
                            
                else:
                    for jogador in jogadores:
                        if jogador.primeiro == False:
                            jogador.pontos += r[cont]
                            jogada_feita = True
                            Montar_Tabuleiro(r[cont], jogador.simbolo)
        if jogada_feita == False:
            print("Digite uma jogada possível")
            r.pop()

def Verificar_Vencedor():
    global vencedor
    if cont<=8:
        for jogador in jogadores:
            if jogador.pontos.count("e") == 3 or \
            jogador.pontos.count("d") == 3 or \
            jogador.pontos.count("mm") == 1 and jogador.pontos.count("em") == 1 and jogador.pontos.count("dm") == 1  or \
            jogador.pontos.count("mm") == 1 and jogador.pontos.count("mc") == 1 and jogador.pontos.count("mb") == 1  or \
            jogador.pontos.count("c") == 3 or \
            jogador.pontos.count("b") == 3 or \
            jogador.pontos.count("mm") == 1 and jogador.pontos.count("eb") == 1 and jogador.pontos.count("dc") == 1  or \
            jogador.pontos.count("mm") == 1 and jogador.pontos.count("ec") == 1 and jogador.pontos.count("db") == 1:
                print(f"{jogador.nome} venceu!")
                vencedor = True

def Verificar_Vencedor2():
    global vencedor
    if cont<=8:
        for jogador in jogadores:
            if tabuleiro [0][0] == jogador.simbolo and tabuleiro [0][1] == jogador.simbolo and tabuleiro [0][2] == jogador.simbolo or\
            tabuleiro [1][0] == jogador.simbolo and tabuleiro [1][1] == jogador.simbolo and tabuleiro [1][2] == jogador.simbolo or\
            tabuleiro [2][0] == jogador.simbolo and tabuleiro [2][1] == jogador.simbolo and tabuleiro [2][2] == jogador.simbolo or\
            tabuleiro [0][0] == jogador.simbolo and tabuleiro [1][0] == jogador.simbolo and tabuleiro [2][0] == jogador.simbolo or\
            tabuleiro [0][1] == jogador.simbolo and tabuleiro [1][1] == jogador.simbolo and tabuleiro [2][1] == jogador.simbolo or\
            tabuleiro [0][2] == jogador.simbolo and tabuleiro [1][2] == jogador.simbolo and tabuleiro [2][2] == jogador.simbolo or\
            tabuleiro [0][0] == jogador.simbolo and tabuleiro [1][1] == jogador.simbolo and tabuleiro [2][2] == jogador.simbolo or\
            tabuleiro [0][2] == jogador.simbolo and tabuleiro [1][1] == jogador.simbolo and tabuleiro [2][0] == jogador.simbolo:
                Exibir_Tabuleiro()
                print(f"{jogador.nome} venceu!")
                vencedor = True
            
def Montar_Tabuleiro(r, s):
    match r:
        case "ec":
            tabuleiro[0][0] = s
        case "em":
            tabuleiro[1][0] = s
        case "eb":
            tabuleiro[2][0] = s
        case "mc":
            tabuleiro[0][1] = s
        case "mm":
            tabuleiro[1][1] = s
        case "mb":
            tabuleiro[2][1] = s
        case "dc":
            tabuleiro[0][2] = s
        case "dm":
            tabuleiro[1][2] = s
        case "db":
            tabuleiro[2][2] = s


def Exibir_Tabuleiro():
    for linha in tabuleiro:
        print(linha)




print("Digite sua jogada com 2 letras (a primeira E para esquerda, M para meio e D para direita. A segunda C para cima, M para meio, B para baixo. Ex: MB=meio embaixo)")
for cont in range(9):
    Exibir_Tabuleiro()
    Fazer_Jogada()
    Verificar_Vencedor2()
    if vencedor == True:
        break
if vencedor == False:
    Exibir_Tabuleiro()
    print("Deu Velha")

