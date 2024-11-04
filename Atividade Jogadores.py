import os
import time

os.system("cls")

jogadores = {
    'Cristiano Ronaldo': {'idade': 36, 'nacionalidade': 'Portugal', 'posicao': 'Atacante'},
    'Lionel Messi': {'idade': 34, 'nacionalidade': 'Argentina', 'posicao': 'Atacante'}
}

def menu():
    print("""
        1.Adicionar ou atualizar um jogador
        2.Listar todos os jogadores
        3.Mostrar os dados de um jogador específico
        4.Remover um jogador
    """)

def add(nome, idade, nacionalidade, posicao):
    jogadores[nome] = {"idade": idade, "nacionalidade": nacionalidade, "posicao": posicao}

def listar():
    print("================ Lista de Jogadores ==================")
    print(f"{'Nome': <20} {'Idade': <4} {'Nacionalidade': <20} {'Posição': <20}")
    for nome, dados in jogadores.items():
        print(f"{nome: <20} {dados['idade']: <5} {dados['nacionalidade']: <20} {dados['posicao']: <20}")

def mostrarEspec(mostrar_dados):
    for nome, dados in jogadores.items():
        if nome == mostrar_dados:
            print(f"{nome: <20} {dados['idade']: <5} {dados['nacionalidade']: <20} {dados['posicao']: <20}")

def revome(nomeRemov):
    if nomeRemov in jogadores:
        del jogadores[nomeRemov]
        print(f"Jogador {nomeRemov} foi removido.\n")
    else:
        print(f"Jogador {nomeRemov} não encontrado.\n")

while True:
    operacao = int(input("Digite a Operação: "))
    match operacao:
        case 1:
            nome = input("Digite o nome do footballer: ")
            idade = int(input("Digite a idade do footballer: "))
            nacionalidade = input("Digite a nacionalidade do footballer: ")
            posicao = input("Digite a posição preferida: ")
            add(nome, idade, nacionalidade, posicao)
        case 2:
            listar()
        case 3:
            mostrar_dados = input("Digite o nome do jogador a mostrar os dados: ")
            mostrarEspec(mostrar_dados)
        case 4:
            nomeRemov = input("Digite o nome do jogador a ser removido: ")
            revome(nomeRemov)