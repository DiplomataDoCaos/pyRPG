#biblioteca de itens consumáveis

def Poção_de_cura(usuário,alvo):
    alvo[0]+=50
    if alvo[0]>alvo[5]:
        alvo[0]=alvo[5]
    print(usuário[11],"usa uma poção de cura!")
    
def Poção_de_fogo(usuário,alvo):
    alvo[0]-=30
    alvo[3]-=2
    alvo[2]-=2
    print(usuário[11],"joga uma poção de fogo em",alvo[11])

def Poção_de_gelo(usuário,alvo):
    alvo[0]-=25
    alvo[4]-=2
    print(usuário[11],"usa uma poção de gelo em",alvo[11])
