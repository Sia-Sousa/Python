import random

acertar = 0
palpite = 0
jogadas = 0


while palpite != 's':
    aleatorio = random.randint (1,10)
    # print ("\n", aleatorio) para testar se acertou ou errou. 
    jogadas += 1
        
    for tentativa in range (3):
        palpite = input("Indique o seu palpite de 1 a 10 ('s' para sair): ")
            
        if palpite == 's':
            print ("Terminado.")
            break
        else :
            int(palpite) == palpite
            if int(palpite) == aleatorio:
                print ("Acertou!")
                acertar += 1
                break
            else:
                print ("Erro.")
    if jogadas == 9:
        print ("Em 10 jogadas, acertou", acertar, "vezes.")
        jogadas = 0
                
print ("Fim")
