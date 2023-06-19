# Teste 1

def boneco(numero):
    resto = 5 - numero
    if numero == 1:
        boneco = """
        oo
        
        
            """ 
        print(boneco)
        print("Tente novamente. Restam-lhe {} tentativas!".format(resto))   
    elif numero == 2:
        boneco = """
        \o/
         
        
            """ 
        print(boneco)
        print("Tente novamente. Restam-lhe {} tentativas!".format(resto))   
    elif numero == 3:
        boneco = """
        \o/
         |
        
            """ 
        print(boneco)
        print("Tente novamente. Restam-lhe {} tentativa!".format(resto))  
    elif numero == 4:
        boneco = """
        \o/
         |
        /
            """ 
        print(boneco)
        print("Tente novamente. Restam-lhe {} tentativas!".format(resto))
    elif numero == 5:
        boneco = """
        \o/
         |
        / |
            """ 
        print(boneco)
        print("Lamento, você perdeu")
    return

import random

print("Bem-vindo ao jogo da forca Edição Frutas!")
print("Terá que adivinhar a palavra secreta que será o nome de uma fruta deliciosa. Terá apenas 5 tentativas para acertar.")
lista_palavras = ["banama","pêra","maçã", "abacate", "tomate"]
palavra_secreta = random.sample(lista_palavras,1)[0].lower()
# Mostrar palavra secreta com espaços em branco
resposta_str = ""
for i in range(len(palavra_secreta)):
    resposta_str = resposta_str + "_"
resposta_list = list(resposta_str)
print("Antes de começar, aqui vai uma dica. A palavra secreta tem {} letras!\n{}".format(len(palavra_secreta),resposta_str))

falha = 0
historico_tentativas = []
while falha < 5:
    tentativa = str(input("Escreva uma letra: ")).lower() #
    tentativa = tentativa[0] # caso o utilizador escreva mais que uma letra, apenas utilizar a primeira letra
    historico_tentativas.append(tentativa)
    resposta_old = "".join(resposta_list) # cria a variavel que vai utilizar para considerar uma tantativa errada
    i = 0
    for letra in palavra_secreta: # loop para mostrar a letra  certa
        if tentativa == letra:
            resposta_list[i]=letra
        i = i + 1
    resposta_str = "".join(resposta_list)
    print(resposta_str)
    print("Letras já escolhidas: ", historico_tentativas)
    if resposta_old == resposta_str:
        falha = falha + 1
        boneco(falha)
    if resposta_str == palavra_secreta:
        print("Parabéns, Ganhou!! A palavra secreta era: {}".format(palavra_secreta))
        break
