#template(vida0,energia1,ataque2,defesa3,velocidade4,vida_max5,energia_max6,especiais7,experiência8,experiência_next9,level10,nome11)
#herói(100,20,10,5,9,100,20,especiais[ataque pesado,surtar])
#para sistemas mais avançados, é necessário marcar inimigo que vai tomar e quem realiza(que é comum de toda a lista),lista
#na lista de caracteristicas do monstro e do jogador,a lista de habilidades pode estar agregada, ou colocada numa lista a parte
#para multi-combate, tem que criar listas de oponentes e heróis
#criar instruções de input para me organizar

import random
import Biblio_e#Mover depois para main
import Biblio_i
import Biblio_m

random.seed()

def gerador_de_AP(velocidade):#action points posso complicar o código
    return (velocidade//3)

def lista_de_ordem(monstro,hero):#Isso pode ser adaptado para lista, podendo trabalhar com vários membros de cada lado
    if monstro[4]>hero[4]:
        return([monstro,hero])
    else:
        return([hero,monstro])

def apresentação_de_hud():#usar para especiais e itens
    print("em construção")


def executor(comando):#lê o comando da lista o executa
    '''função recebe um comando(lista) com tipo de ação0,especificidade1,usuário2 e alvo3'''
    if comando[0]=="ataque":
        dano=atacar(comando[1][2],comando[2][3])
        comando[2][0]-=dano
        print(comando[1][11],"ataca e causa",dano,"de dano em",comando[2][11])
    elif comando[0]=="especial":
        if comando[1]=="ataque forte":
           comando[3][0]-=atacar(comando[2][2]+5,comando[3][3])
        else:
           comando[3][0]-=atacar(comando[2][2]+5,comando[3][3])*2
    elif comando[0]=="defesa":
        comando[1][3]=comando[1][3]*2
        post_r.append(["defesa",comando[1]])
    elif comando[0]=="fuga":
        a=comando[1][4]-comando[2][4]#a=gerar número aleatório baseado nas velocidades  ###Aparentemente, as funções não atribuidas são desconeças da função
        if a>=0:
            print("Conseguiu fugir!")
            return("fuga!")
        else:
            print("fail,seu arregão!")
    elif comando[0]=="item":
        base="Biblio_i."
        if comando[1]==0:
            base+="Poção_de_cura"
        elif comando[1]==1:
            base+="Poção_de_fogo"
        else:
            base+="Poção_de_gelo"
        base+="(",comando[2][11],",",comando[3][11],")"#tem que ajustar aqui
        exec(base)
    else:
        print("nada aqui por enquanto")

def contra_executor(comando):
    if comando[0]=="defesa":
        comando[1][3]=comando[1][3]/2


def atacar(ataque,defesa):
    '''recebe os valores de defesa e ataque e calcula o dano'''
    if (ataque-defesa)>0:
        return(ataque-defesa)#dano
    else:
        return(0)

def ajuda():#pronto
    print("atacar:causa dano no oponente (ataque-defesa)\
          especiais:Ações especiais, cada uma segue sua própria regra, consomem energia\
          defender:Aumenta o valor da defesa temporariamente até o fim da rodada, bom contra ataques pesados\
          fugir:tenta escapar do combate, arregão!\
          itens:use um de seus itens consumáveis(ou não)\
          ajuda:dããããã\
          cancelar:cancela a última ação dada")

def combate(hero,especiais,itens,monstro):##trabalhar em dados permanentes e temporários
    #por enquanto o monstro tem as mesma habilidades que o personagem
    '''Idéia de combate:
    jogador escolhe movimentos, inimigo(aleatóriamente) também
    os aps são jogados um a um, mas quem tem mais velocidade vai primeiro
    movimentos terão valores deiferentes(?)
    '''
    post_r=[]
    post_t=[]
    while hero[0]>0 and monstro[0]>0:#Enquanto um dos combatentes não for derrubado
        AP_m=gerador_de_AP(monstro[4])#é calculado todo turno devido a efeitos por rodada
        AP_h=gerador_de_AP(hero[4])
        comandos_h, comandos_m=[],[]#listas zeradas de comandos
        print(hero[11],": Vida:",hero[0],"/",hero[5],"Energia:",hero[1],"/",hero[6],"Ataque:",hero[2],"Defesa:",hero[3])##HUD basica, precisa de melhoras
        print(monstro[11],": Vida:",monstro[0],"/",monstro[5],"Energia:",monstro[1],"/",monstro[6],"Ataque:",monstro[2],"Defesa:",monstro[3])
        ordem=lista_de_ordem(monstro,hero)
        AP_R=gerador_de_AP(ordem[0][4])
        print("Ordem:",ordem[0][11],ordem[1][11])

        while AP_h>0:#pode-se generalizar-se isso para aceitar o monstro tb
            print("Comandos:")
            for i in range (len(comandos_h)):
                if comandos_h[i][0]=="especial" or comandos_h[i][0]=="item":
                    print(comandos_h[i][1])
                else:
                    print(comandos_h[i][0])
            print()
            z=input("[a]tacar,[e]speciais,[d]efender,[f]ugir,[i]tens,a[j]uda,[c]ancelar")
            if z=="a": ##fazer subtrações de AP avançadas
                comandos_h.append(["ataque",hero,monstro])
                AP_h-=1
            elif z=="e":##preciso fazer a subtração de energia aqui
                print("1:",especiais[0],"2:",especiais[1])
                tipo=input("escolha por número:")
                if tipo==1:
                    tipo="ataque pesado"       
                else:
                    tipo="surtar"
                comandos_h.append(["especial",tipo,hero,monstro])
                AP_h-=1
            elif z=="d":
                comandos_h.append(["defesa",hero])
                AP_h-=1
            elif z=="f":
                comandos_h.append(["fuga",hero,monstro])
                AP_h-=1
            elif z=="i":
                print(itens)
                item=int(input("escolha por número:"))##HUD básica #fazer que ele verifica se é válido
                if itens[item][1]>0:
                    itens[item][1]-=1
                    comandos_h.append(["item",item,hero,monstro])
                    AP_h-=1
                else:
                    print("você não tem esse item! Mané!")
            elif z=="c" and comandos_h!=[]:
                ##tirar da lista comandos_h:
                AP_h+=1
            elif z=="j":
                ajuda()
            else:
                print("O que droga você quer que eu faça?!")

        while AP_m>0: #comandos do monstro
            gerador=random.choice([0,1,2])
            if gerador==0:
                comandos_m.append(["ataque",monstro,hero])
                AP_m-=1
            elif gerador==1:
                tipo=random.choice([0,1])
                comandos_m.append(["especial",tipo,monstro,hero])
                AP_m-=1
            elif gerador==2:
                comandos_m.append(["defesa",monstro])
                AP_m-=1

        for i in range(AP_R):#execução da rodada #funcionando
            if i < len(comandos_h):
                executor(comandos_h[i])
            if i < len(comandos_m):
                executor(comandos_m[i])
            for u in range(len(post_t)):
                contra_executor(post_t[u])#fim de eventos de turno
        for i in range(len(post_r)):
            contra_executor(post_r[i])#fim de eventos de rodada
            
    if hero[0]>0:#resultados da batalha
        hero[8]=hero[8]+ monstro[8]
        if hero[8]>=hero[9]:#level up!
            print("Você subiu de nível!")
            hero[8]= hero[8] - hero[9]
            hero[9]=hero[9]+50
            hero[10]= hero[10]+1
            hero[2],hero[3],hero[4],hero[5],hero[6]=hero[2]+2,hero[3]+1,hero[4]+1,hero[5]+20,hero[6]+5#aumento de status
        print("Parabéns, você não virou jantar!")
        print("Ganhou",monstro[8],"de experiência!")
    else:
        print("Você morreu e agora virou adubo! Game over")
        #return(game_over)

especiais=["ataque forte","surtar"]
hero=[100,20,10,5,9,100,20,especiais,0,100,1,"hero"]
itens=[["poção de cura",2],["poção de manadium fira",1], ["poção de manádium crio",1]]
monstro=[30,30,10,5,9,30,30,especiais,50,0,0,"monstro"]
combate(hero,especiais,itens,monstro)
