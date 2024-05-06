from random import randint
palavras = ["programação", "estudar", "faculdade", "python", "java", "matemática"]
palavra_secreta = palavras[randint(0, 5)]
chutes = []
letras_corretas = []
erros = 0
correto = 0

print("=-=-=-=-=-=- BEM-VINDO AO JOGO DA FORCA =-=-=-=-=-=-")
print(f"A palavra secreta possui {len(palavra_secreta)} letras")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
while True:
    #se a posição atual corresponder a uma letra em palavra_secreta, mostra essa letra, senão, mostra um underline
    for letra in palavra_secreta:
        if letra in letras_corretas:
            print(letra, end="")
        else:
            print("_ ", end="")

    chute = (input("\nDigite uma letra: ")).lower().strip()
    #verifica se o usuário digitou de fato uma letra e a quantidade
    if chute.isalpha() != True or len(chute) != 1:
        print("Por favor, digite apenas uma letra")
        continue

    #verifica se a letra digitada está no vetor de chutes, se não estiver add no mesmo
    if chute not in chutes:
        chutes.append(chute)
    else:
        print(f"Você já tentou a letra '{chute}', escolha outra")
        continue

    #verifica se a letra digitada está na palavra secreta, se estiver add no vetor de letras corretas e mostra uma msg positiva, senão, mostra uma msg negativa
    for l in palavra_secreta:
        if chute == l:
            letras_corretas.append(chute)

    if chute in palavra_secreta:
        print(f"'{chute}' faz parte da palavra secreta")
    else:
        print(f"'{chute}' não faz parte da palavra secreta")
        erros += 1

    #verifica se o jogador perdeu por tentativas
    if erros == 6:
        print(f"Você perdeu! A palavra secreta era '{palavra_secreta.capitalize()}'\n")
        break
    
    if len(letras_corretas) == len(palavra_secreta):
        print(f"Parabéns! Você descobriu a palavra secreta '{palavra_secreta.capitalize()}'\n")
        break