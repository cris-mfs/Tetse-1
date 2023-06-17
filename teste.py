# Teste 1
import random
#contador para tentativas falahadas

lista_palavras = ["batata","gnar","mialgia"]
palavra_secreta = random.sample(lista_palavras,1)[0].lower()

#palavra_secreta.lower()
#print("A palavra secreta é: ", palavra_secreta)

# Mostrar palavra secreta com espaços em branco
resposta_list = ""
for i in range(len(palavra_secreta)):
    resposta_list = resposta_list + "_"
resposta_list = list(resposta_list)
print(resposta_list)

# número tentativas função para faze ro boneco consoante ov alor do numero de tentativas 
# só dar errado se for uma tentiva falhada
falha = 0
while falha < 5:
    tentativa = str(input("escreva uma letra: ")).lower()
    i = 0
    for letra in palavra_secreta:
        if tentativa == letra:
            resposta_list[i]=letra
        i = i + 1
    resposta_str = "".join(resposta_list)
    print(resposta_str)
    if resposta_str == palavra_secreta:
        print("Parabéns, Ganhou!!")
        break

# sair quando o utilizador acertar na