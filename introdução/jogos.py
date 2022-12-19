import forca
import advinhacao

def escolhe_jogo():
    print("*********************************")
    print("******** Escolha um Jogo ********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()