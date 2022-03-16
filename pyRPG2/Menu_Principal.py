
import math

#######################################################
#classes de combate
##################################################

class Combatente(object):
    def __init__(self,Nome,Vivo,Vida,Energia,Ataque,Defesa,Velocidade,Exp,Lis_Habilidades):
            self.Nome =Nome
            self.Vivo=Vivo
            self.Vida=Vida
            self.Energia=Energia
            self.Ataque=Ataque
            self.Defesa=Defesa
            self.Velocidade=Velocidade
            self.Exp=Exp
            self.Status={}#(dicionário, vc não pode acumular multiplas instancias do mesmo status, mas podem ser intensificados e recarregados )
            self.Lis_Habilidades=Lis_Habilidades
    def Ataque(self,Alvo):
        if Alvo.Defesa<self.Ataque:
            Alvo.Vida[0]= Alvo.Vida[0] + Alvo.Defesa- self.Ataque
        else:
            print("O ataque é inefetivo, luuuuzer")
    def Defender(self):
            self.Defesa= self.Defesa* 2
            self.Status.Insert("")
    def Usar_habilidade(self,alvo): #imcompleto não se pode ser escrito assim
            print(self.Lis_habilidades)
            Escolha=int(input("Selecione sua habildade por número")) -1
            if [Escolha].Custo <= self.Energia[1]:
                [Escolha].Usar(self,alvo)
            
            #Abrir lista (feito), o usuário pode escolher qual usar, talvez tenha que fazer da maneira chata?
    def Fugir(PartyA,PartyB): #adicionar fator de random com curva de sino # está adaptado para o player
        va=0
        for a in PartyA:
            va=+a.velocidade + math.random(-1,1)
            vb=0
        for b in PartyB:
            vb=+b.velocidade + math.random(-1,1)
        if PartyA>PartyB:
            print(self.name,"Conseguiu arregar!")
            return (PParty)
        else:
            print(self.name, "Não conseguiu correr, se prepara que lá vem bomba!")

######
#Lista de habilidades (somente em combate por enquanto)
######

class Habilidade(object): #Não sei se presta converter em classe - se eu fizer, dá para usar como instancias as habilidades
    def __init__(self, Nome, Custo,Poder):
        Nome=Nome
        Custo=Custo
        Poder=Poder
    def Usar(self,Usuário,Alvo):
        print("Insira as coisas que abilidade faz aqui, dar override para isso")

class Curar(Habilidade):
    def Usar(self,Usuário,Alvo):
        Alvo.Vida[1] =+ Usuário.Ataque
        if Alvo.Vida[1] > Alvo.Vida[0]:
            Alvo.Vida[1]=Alvo.Vida[0]
        Usuário.Energia[1] =- self.Custo

class Dano (Habilidade):
    def Usar (self,Usuário,Alvo):
        Alvo.Vida =- Usuário.Ataque*self.Poder
        Usuário.Energia[1]=-self.Custo

class DanoFixo (Habilidade):
    def Usar (self,Usuário,Alvo):
        Alvo.Vida=-self.Poder
        Usuário.Energia[1]=-self.Custo

class Buff (Habilidade):
    def Usar (self,Usuário,Alvo) :
        Usuário.Energia[1]=-self.Custo
    
#######
#Inicialização de habilidades    
######

Remendo=Curar("Curar",10,1)
Powercura=Curar("Powercura!",20,2)
Bomba=Dano("Bomba",20,2)
Racoon_powers=Dano("Racoon Powers!",20,1.5)
Mordida=DanoFixo("Mordida",20,30)


######################################################################
#Inicialização de combatentes - precisa de ajustes, os combatentes específicos tem que ser inicializados no inicio do combate
#########################

Fatboy=Combatente("Fatboy",1,[100,100],[100,100],25,10,10,[0,100],[Curar])
Racoon=Combatente("Racoon",1,[50,50],[20,20],20,5,5,[15,0],[Racoon_powers])
Lizard=Combatente("Lizard",1,[75,75],[0,0],25,5,5,[20,0],[Mordida])
Chefãobásico=Combatente("Chefão Básico",1,[200,200],[200,200],40,15,15,[300,0],[Bomba])

#####
#Classes do Mapa
#####

class Mapa(object):
    def __init__(self,Nome,Mapa_gráfico,Mapa_mov,Mapa_ação):
        self.Mapa_gráfico = Mapa_gráfico
        self.Mapa_mov = Mapa_mov
        self.Mapa_ação = Mapa_ação
        self.Nome = Nome
    def Começar_ação(self,Evento):
        pass
    def Ação_passiva(self,Evento):
        pass

class Gráfico(object): #Tá muuuito bobo ainda
    def __init__(self,Gráfico,Código):
        self.Código=Código
        self.Gráfico=Gráfico

class Ação(object):
    def __init__(self,Gráfico,Código):
        self.Gráfico=Gráfico
        self.Código=Código

class Jogador(Ação):
    Dentro=True
    def Mover(Mapa_mov,Mapa_ação,Coordenadas):#inputs de movimento e ação #Checar se isso tá certo
        while Dentro[0]==True:
            for x in Mapa_mov:#Hud básica
                print(x)
            mov=input()
            if mov=="a": #Movimento nos quatro sentidos
                Movimento(-1,0,3,Coordenadas,Mapa_mov,Dentro)
            elif mov=="s":
                Movimento(0,1,2,Coordenadas,Mapa_mov,Dentro)
            elif mov=="d":
                Movimento(1,0,1,Coordenadas,Mapa_mov,Dentro)
            elif mov=="w":
                Movimento(0,-1,0,Coordenadas,Mapa_mov,Dentro)
            elif mov=="p":
                Volume_som,Volume_música=Menu_Principal.Opções(Volume_som,Volume_música)
            elif mov=="i":
                Menu_inv()#Inventário e status




############################
#Inicialização de ações
############################

J=Jogador("Sem gráfico","J")

#########################
#Inicialização de mapas
######################

Mapa_teste=Mapa("Teste de bug","No grx",[[1,1,1],[1,0,1],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]])

#####################################################

def Começar():#Carrega um mapa diretamente (o primeiro
    Jogando=1
    while Jogando==1:
        Dentro=True
        MAtivo=Mapa(Mapauno) #Ampliar aqui #não está lendo a tupla como vários argumentos
        while Jogador.Dentro==True:
            for x in Mapa_mov:#Hud básica
                print(x)
            mov=input()
            if mov=="a": #Movimento nos quatro sentidos
                Movimento(-1,0,3,Coordenadas,Mapa_mov,Dentro)
            elif mov=="s":
                Movimento(0,1,2,Coordenadas,Mapa_mov,Dentro)
            elif mov=="d":
                Movimento(1,0,1,Coordenadas,Mapa_mov,Dentro)
            elif mov=="w":
                Movimento(0,-1,0,Coordenadas,Mapa_mov,Dentro)
            elif mov=="p":
                Volume_som,Volume_música=Menu_Principal.Opções(Volume_som,Volume_música)
            elif mov=="i":
                Menu_inv()#Inventário e status

   
def Carregar(Arquivo):
    #Começará com 3 saves diferentes independentes
    #O jogador escole qual save quer pelo número
    #Nome dos arquivos save1.txt save2.txt etc...
    #Adicionar depois leitura prévia, mostrando alguns dadosdos saves
    print("Under Construction")


###########################################################################

def main():
    #load das tralhas

###############################
    
    #Fazer carregar opções de arquivo
    Volume_som,Volume_música=50,50
    Pausa=False#Inútil agora
    Start="z"
    #Play melody básica
    input("Seja bem vindo ao jogo mais loucamente maneiro que você vai encontrar!/ Um jogo de comédia que não apela pra baixaria!")
    #input("Adamastor e Lizzie apresentam:")
    #input("Tam Tam Taaaam...")
    #input("dududu dududu DUDUDU (Tá eu paro de improvisar...)")
    #input("As aventuras de Fatboy - Jogue isso quando estiver itediàdo")
    #Play other mélody básica
    while Start!="s":
        Start = input("O que deseja fazer? n-Novo jogo(Isso rima!),c-Carregar besteira,o-Opções,p-Sair dessa droga!!!")
        if Start=="n":
            input("Ih droga... eu não tenho roteiro... melhor começar a improvisar essa coisa")
            Começar()
        elif Start=="c":
            input("Ainda nem temos jogo para começar...")
        elif Start=="o":
            Volume_som,Volume_música=Opções(Volume_som,Volume_música)
        elif Start=="p":
            Start=input("Seu filho de pisadela e um beslicão, trate de parar de arregar!!! s-Sair v-Voltar")
            if Start=="v":
                input("Boa escolha!!!")
            elif Start=="s":
                ("NOOOOOOOOOOOOOOOOOOOOOO!!!")

def Opções(Volume_som,Volume_música):
    Pausa=True
    while Pausa==True:
        Start=input ("q/w-Abaixar/aumentar o volume dos efeitos speCiALs ehhhh, a/s-Abaixar/aumentar o volume da música, p-Para deixar de ser fresco")
        if Start=="q" and Volume_som>0:
            Volume_som-=10
        elif Start=="w" and Volume_som<100:
            Volume_som+=10
        elif Start=="a" and Volume_música>100:
            Volume_música-=10
        elif Start=="s" and Volume_música<100:
            Volume_música+=10
        elif Start=="p":
            Pausa=False
    return(Volume_som,Volume_música)#ver o que acontece se colocar em lista




main()
