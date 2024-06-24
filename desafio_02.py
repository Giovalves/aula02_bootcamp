nome_usuario = input("Digite o seu nome:")
if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Você nao digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você nao digitou espaco")
    exit()