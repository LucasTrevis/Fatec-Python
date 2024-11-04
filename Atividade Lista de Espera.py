import os
os.system("cls")

lista_espera = []
lista_atendidos = []

def menu():
    print("\n 1. Adicionar paciente a lista de espera"
        "\n 2. Remover paciente da lista de espera"
        "\n 3. Exibir lista de paciente atendidos"
        "\n 4. Exibir lista de espera"
        )

def gerar_codigo():
    return lista_espera[-1][0] + 1 if lista_espera else 1

def add_espera(nome_p, especialidade):
    codigo = gerar_codigo()
    pre_espera = [codigo, nome_p, especialidade]
    lista_espera.append(pre_espera)

def remover_paciente(cod_remov):
    for pacientes in lista_espera:
        if pacientes[0] == cod_remov:
            lista_atendidos.append(pacientes)
            lista_espera.remove(pacientes)
            print("Paciente adicionado na lista de atendidos!")
            break
    if cod_remov is not pacientes[0]:
        print("Paciente não encontrado!")
        input("Enter para continuar")

def ex_atendidos():
    print("\n========== Lista de Pacientes Atendidos =========")
    print(f"{'Código':<10}|{'Nome':<15}|{'Especialidade':<10}")
    for paciente in lista_atendidos:
        print(f"{paciente[0]:<10}|{paciente[1]:<15}|{paciente[2]:<10}")

def ex_espera():
    print("\n========== Lista de Espera =========")
    print(f"{'Código':<10}|{'Nome':<15}|{'Especialidade':<10}")
    for paciente in lista_espera:
        print(f"{paciente[0]:<10}|{paciente[1]:<15}|{paciente[2]:<10}")

#Programa principal
while True:
    menu()
    op = int(input("Digite a opção desejada: "))
    match op:
        case 1:
            os.system("cls")
            nome_p = input("Digite o nome do paciente: ")
            especialidade = input("Digite a especialidade médica: ")
            add_espera(nome_p, especialidade)
        case 2:
            os.system("cls")
            if not lista_espera:
                print("Lista vazia!")
                input("Enter para continuar")
                os.system("cls")
            else:
                cod_remov = int(input("Digite o código do paciente a ser removido: "))
                remover_paciente(cod_remov)
        case 3:
            if not lista_atendidos:
                
                print("Lista vazia!")
                input("Enter para continuar")
                os.system("cls")
            else:
                ex_atendidos()
                input("Enter para continuar")
                os.system("cls")
        case 4:
            if not lista_espera:
                print("Lista vazia!")
                input("Enter para continuar")
                os.system("cls")
            else:
                ex_espera()
                input("Enter para continuar")
                os.system("cls")