
print ("*********************************")
print ("***Bem vindo ao jogo da Forca!***")
print ("*********************************")

palavras_secretas= ["banana", "paralelepipedo", "python", "programacao"]
letras_acertadas= ["_", "_", "_", "_", "_", "_"]


enforcou= False
acertou= False
chances= int(5)

print ("Palavra para descobrir: ",end="")
print (*letras_acertadas)

while (not enforcou and not acertou):
    print (f'Chances: {chances}')
    chute = input("Qual letra? ")
    chute = chute.strip()

    if (chute != "b") and (chute != "a") and (chute != "n"):
        chances-= 1
    
    index= 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index+= 1

    print (*letras_acertadas)
    print ("__"*20)

    if (("_" in letras_acertadas) == False):
        acertou= True
    elif chances == 0:
        enforcou = True

if acertou == True:
    print()
    print ("Parabéns, você acertou a palavra secreta!!!")
    print ("***** Well done *****")
elif enforcou == True:
    print ()
    print ("Que pena, você não conseguiu acertar a palavra secreta...  =( ")
    print ("***** Game Over *****")


