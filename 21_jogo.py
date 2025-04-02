import random

class Carta:
    def __init__(self, valor, nipe):
        self.valor = valor
        self.nipe = nipe
        self.pontos = self.definir_pontos()
    
    def definir_pontos(self):
        if self.valor in ['Valete', 'Dama', 'Rei']:
            return 10
        elif self.valor == 'Ás':
            return 11
        else:
            return int(self.valor)
    
    def __str__(self):
        return f'{self.valor} de {self.nipe}'

class Baralho:
    nipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
    
    def __init__(self):
        self.cartas = [Carta(valor, nipe) for nipe in self.nipes for valor in self.valores]
        random.shuffle(self.cartas)
    
    def puxar_carta(self):
        return self.cartas.pop() if self.cartas else None

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
    
    def receber_carta(self, carta):
        self.mao.append(carta)
    
    def calcular_pontos(self):
        total = sum(carta.pontos for carta in self.mao)
        ases = sum(1 for carta in self.mao if carta.valor == 'Ás')
        while total > 21 and ases:
            total -= 10
            ases -= 1
        return total
    
    def mostrar_mao(self):
        return ', '.join(str(carta) for carta in self.mao)

class Jogo21:
    def __init__(self):
        self.baralho = Baralho()
        self.jogador = Jogador("Marcelo")
        self.oponente = Jogador("Mu Santos")
        self.distribuir_cartas()
    
    def distribuir_cartas(self):
        jogador = self.jogador
        oponente = self.oponente
        for _ in range(2):
            self.jogador.receber_carta(self.baralho.puxar_carta())
            self.oponente.receber_carta(self.baralho.puxar_carta())
        print(f"Cartas distribuídas!")
        print(f"Mão do {jogador.nome}: {self.jogador.mostrar_mao()} (Pontuação: {self.jogador.calcular_pontos()})")
        print(f"Mão do {oponente.nome}: {self.oponente.mostrar_mao()} (Pontuação: {self.oponente.calcular_pontos()})")
    
    def turno_jogador(self, jogador):
        while jogador.calcular_pontos() < 21:
            acao = input(f"{jogador.nome}, deseja outra carta? (s/n) ").strip().lower()
            if acao == 's':
                jogador.receber_carta(self.baralho.puxar_carta())
                print(f"{jogador.nome} agora tem: {jogador.mostrar_mao()} (Pontuação: {jogador.calcular_pontos()})")
            else:
                break

    def jogar(self):
        self.turno_jogador(self.jogador)
        jogador = self.jogador
        oponente = self.oponente
        
        if self.jogador.calcular_pontos() > 21:
            print(f"Você estourou! {jogador.nome} vence.")
            return
        
        print(f"Turno do {oponente.nome}!")
        self.turno_jogador(self.oponente)
        
        
        if self.oponente.calcular_pontos() > 21 or self.jogador.calcular_pontos() > self.oponente.calcular_pontos():
            print("Você venceu!")
        elif self.jogador.calcular_pontos() < self.oponente.calcular_pontos():
            print(f"{jogador.nome} vence!")
        else:
            print("Empate!")

if __name__ == "__main__":
    jogo = Jogo21()
    jogo.jogar()
