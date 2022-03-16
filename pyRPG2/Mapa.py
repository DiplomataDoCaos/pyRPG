def Mover(Mapa_mov,Mapa_ação,Coordenadas):#inputs de movimento e ação
    Dentro=[True]
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

def Movimento(x,y,z,Coordenadas,Mapa_mov,Dentro):
    if Mapa_mov[Coordenadas[0]+y][Coordenadas[1]+x]==0:
        Mapa_mov[Coordenadas[0]+y][Coordenadas[1]+x]="P"
        Mapa_mov[Coordenadas[0]][Coordenadas[1]]=0
        Coordenadas[0],Coordenadas[1],Coordenadas[2]=Coordenadas[0]+y,Coordenadas[1]+x,z
        if Coordenadas[3][0]==True:  
            if 100>=random.randrange(0,Coordenadas[3][1]): #gerar um número nesse intervalo #terminar
                Combate(PParty,MParty)
                Coordenadas[3][1]=-50
            else:
                Coordenadas[3][1]=+ 5
                #Aumentar a chance de encontrar sutilmente
    elif Mapa_mov[Coordenadas[0]+y][Coordenadas[1]+x]==2:
        Dentro[0]=False
        
def Mapa():
    Mover(Mapa_mov,Mapa_ação,Coordenadas)

def Menu_inv():
    print("Under construction")
