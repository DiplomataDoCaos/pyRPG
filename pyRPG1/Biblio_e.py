#Biblioteca de especiais

def Ataque_pesado(atacante,defensor):
    dano=atacar(atacante[2]+5,defensor[3])
    print(atacante[11],"executa um ataque pesado que causa",dano,"de dano em",defensor[11])

def Surtar(atacante,defensor):
    dano1=atacar(atacante[2]+5,defensor[3])
    print(atacante[11],"surta e causa",dano1,"de dano em",defensor[11])
    dano2=atacar(atacante[2]+5,defensor[3])
    print(atacante[11],"continua atacando e causa",dano2,"de dano em",defensor[11])
    defensor[0]-=dano1+dano2
