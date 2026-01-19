import random as rd
import string

print("Gerador de Senhas Seguras\nO Gerador de Senhas Seguras cria senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.")

opcoes = string.ascii_letters + string.digits + string.punctuation
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha = ""

for i in range(tamanho_senha):
    senha += rd.choice(opcoes)

print("-"*30)
print("Sua senha gerada é:\n", senha)
print("-"*30)
input("Pressione Enter para sair...")