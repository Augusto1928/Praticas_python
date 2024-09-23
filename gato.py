
#CRIANDO O GATO


import random
#O Gato decide a caixa
caixas = [1,2,3,4,5]
caixa_de_inicio = random.choice(caixas)

#O Comportamento do gato
class gato():
    def __init__(self, caixa_inicial, caixa_atual):
        self.caixa_inicial = caixa_inicial
        self.caixa_atual = caixa_atual
    
    def mudar_caixa(self):
        lado = random.choice([-1,1])
        if (self.caixa_atual + lado) > 5:
            lado = -1
        if (self.caixa_atual + lado) < 1:
            lado = 1
        self.caixa_atual = self.caixa_atual + lado

    def caixa(self):
        print(self.caixa_atual)

nao = gato(caixa_de_inicio, caixa_de_inicio)
#Tem que acertar a caixa do gato nao
tentativas = 7
while True:
    
    print("você tem", tentativas, "TENTATIVAS!")
    escolha = int(input(("em que caixa o gato está (DIGITE 1,2,3,4 OU 5): ")))
    if escolha == nao.caixa_atual:
        break
    nao.mudar_caixa()
    tentativas = tentativas - 1
    if tentativas == 0:
        print("você perdeu")
    
    
    
    
print("ACERTOU!")
