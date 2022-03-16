import math
import random

def Ordenador(PParty,MParty):
    Ordem=[] #Criando a lista, sem ordem
    for x in PParty:
        Ordem.append(x)
    for x in MParty:
        Ordem.append(x)
    for y in range(len(Ordem)): #Algoritmo inicial de ordem - precisa de correção
        print("placaholder",y)
        #if Ordem[y]["Velocidade"]<Ordem[y+1]["Velocidade"]:
         #   Ordem[y],Ordem[y+1] = Ordem[y+1],Ordem[y]
    return(Ordem)

def Ataque(Atacante,Defensor):
    Dano=Atacante["Ataque"]-Defensor["Defesa"]
    print("O ataque de",Atacante["Nome"],"causou",Dano,"dano em",Defensor["Nome"])
    Defensor["Vida"][1]-=Dano
    if Defensor["Vida"][1]<0:
        Defensor["Vida"][1]=0
        Defensor["Vivo"]=0

def Cura(Usuário):
    Cura= 50
    Usuário["Vida"][1]+=Cura
    print(Usuário["Nome"], "curou-se", Cura, "de vida")
    if Usuário["Vida"][1]>Usuário["Vida"][0]:
        Usuário["Vida"][1]=Usuário["Vida"][0]

def Check_vivo(Party):
    Check=False
    for x in Party:
        if x["Vivo"]==1:
            Check=True
    return(Check)

def Batalha(PParty,Mparty):#Batalha

    Ordem=Ordenador(PParty,MParty)

    y=1 #Apresentação da ordem - preciso de formatador de quebra de linha
    print("Ordem:")
    for x in Ordem:
        print(y)
        y+=1
        print(":")
        print(x["Nome"])
    
    while (True,True)==(Check_vivo(PParty),Check_vivo(MParty)): #Sistema de repetição do ciclo de batalha :
        for x in range(len(Ordem)):
            if Ordem[x]["Jogador"]==1:
                if Ordem[x]["Vivo"]==1:
                    for h in range(len(Ordem)):#melhorar apresentação
                        print(Ordem[h])
                    a=input("Qual é a pizza manolo! a=Ataque,c=Cura,f=Fugir") #input do jogador
                    if a=="a":
                        Defensor=input("Insira o nome de quem merece umas palmadas na bunda!")
                        Ataque(Ordem[x],Defensor) #Sem controle por enquanto
                    elif a=="c":
                        Cura(Ordem[x])
                    elif a=="f": #Adicionar chance
                        print("Você é conseguiu arregar!")
                        return(PParty)
                    else:
                        print("Errou o comando manolo! Perdeu a vez!") #Adicionar second chance
            else:
                if Ordem[x]["Vivo"]==1:
                    Ataque(Ordem[x],random.choice(PParty))

    if Check_vivo(PParty)==False:
        print("Sua equipe MÓrreu, seu perdedor")
        return(Game_over)
    else:
        print("Yeeeaaaahh você não é tão ruím assim!")
        for x in MParty: #sistema de exp e lvl up básicos
            Somaexp=+x["Expg"]
        for x in PParty:
            x["Exp"][0] =+ Somaexp
            if x["Exp"][0] >= x["Exp"][1]:
                x["Exp"][0] =- x["Exp"][1]
                x["Exp"][1]=+50
                x["Vida"][1]=+ 20
                x["Ataque"]=+3
                x["Defesa"]=+2
                x["Velocidade"]=+1
        return(PParty)
#####################################################################################################

#Fatboy = {"Nome":"Fatboy","Vida":[100,100],"Energia":100,"Ataque":25,"Defesa":10, "Velocidade":10, "Jogador":1, "Vivo":1,"Exp":[0,100]} #Atributos dos personagens
#Template = {"Nome":"Template","Vida":[50,50],"Energia":20,"Ataque":20,"Defesa":5, "Velocidade":5, "Jogador":1, "Vivo":1, "Expg":20 }

#Fatboy1, Fatboy2 = Fatboy,Fatboy
#Lizard = Template.copy() #Isso faz uma cópia ligada da lista
#Lizard["Nome"]="Lizard"
#Lizard["Vida"]=Template["Vida"][:]
#Racoon = Template.copy()
#Racoon["Nome"]="Racoon"
#Racoon["Vida"]=Template["Vida"][:]

#PParty = [Fatboy1, Fatboy2] #trabalhar aqui a expansão dos grupos adicionar randomizador
#MParty = [Lizard, Racoon]

#Batalha(PParty,MParty)#Base para o teste
