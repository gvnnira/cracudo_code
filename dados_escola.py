import json

menu_p = 999999999999
estudante_lista = []


# Função para CARREGAR dados cadastrados
def carregar_dados():
    try:
        with open("estudante_lista.json", "r") as file:
            estudante_lista = json.load(file)
    except FileNotFoundError:
        estudante_lista = []
    return estudante_lista


# Função para SALVAR dados cadastrados
def salvar_dados(estudante_lista):
    with open("estudante_lista.json", "w") as file:
        json.dump(estudante_lista, file)


# Menu Principal
def menu_principal():
    print("-" * 30)
    print(" " * 6, "MENU PRINCIPAL")
    print(
        "[1] Estudantes\n"
        "[2] Professores\n"
        "[3] Disciplinas\n"
        "[4] Turmas\n"
        "[5] Matrículas\n"
        "[0] Sair"
    )
    return int(input("Digite o número da opção desejada: "))


# Menu de Operações
def menu_operacoes():
    print("-" * 30)
    print(" " * 5, "MENU DE OPERAÇÕES")
    print(
        "1 - Incluir\n"
        "2 - Listar\n"
        "3 - Atualizar\n"
        "4 - Excluir\n"
        "0 - Voltar ao menu principal"
    )
    return int(input("Digite o número da opção desejada: "))


# Mensagem de Desenvolvimento
def develop():
    print("-" * 30)
    print("ERRO! Programa em desenvolvimento")


# Título Padrão
def titulo(txt):
    print("-" * 30)
    print(">", txt)


# Função de Incluir Usuário
def incluir_estudante():
    titulo("INCLUIR")
    print("\nPor favor, forneça dos dados abaixo para incluir um estudante.")
    nome = input("Nome: ").upper()
    codigo = int(input("Código: "))
    cpf = input("CPF: ")
    estudante_dic = {
            "Nome": nome,
            "Código": codigo,
            "CPF": cpf
    }
    # Verificar se o código já existe na lista
    for estudante in estudante_lista:
        if estudante["Código"] == codigo:
            print("! Código já existente. Por favor, tente novamente !\n")
            codigo_novo = int(input("Digite um novo código: "))
            estudante_dic["Código"] = codigo_novo
            break
    estudante_lista.append(estudante_dic)
    # Salvar os dados do estudante no arquivo
    salvar_dados(estudante_lista)
    print("Estudante cadastrado com sucesso!\n")


# Função Listar
def listar_estudante():
    titulo("LISTAR")
    print("=" * 30)
    if len(estudante_lista) == 0:
        print("A lista está vazia!")
    else:
        print("Seguem abaixo os alunos cadastrados:\n")
        for dados in estudante_lista:
            for c, v in dados.items():
                print(f'{c}: {v}')
            print("=" * 30)
    print(input("\nAperte a tecla ENTER para continuar "))


# Função Atualizar
def atualizar_estudante():
    carregar_dados()
    titulo("ATUALIZAR")
    codigo = int(input("\nDigite o código do estudante que deseja atualizar: "))
    for estudante in estudante_lista:
        if estudante['Código'] == codigo:
            estudante['Nome'] = input("Digite o novo nome do estudante: ").upper()
            estudante['Código'] = int(input("Digite o novo código do estudante: "))
            estudante['CPF'] = input("Digite o novo CPF do estudante: ")
            print(f"\n--- Os dados do estudante foram atualizados com sucesso! ---")
            break
    else:
        print(f"\nNão foi encontrado nenhum estudante com código {codigo}.")
    # Salvar os dados do estudante no arquivo
    salvar_dados(estudante_lista)


# Função Excluir
def excluir_estudante():
    carregar_dados()
    titulo("EXCLUIR")
    if input("Deseja excluir um estudante cadastrado? (S/N): ").upper() == "S":
        cod_excluir = int(input("Digite o CÓDIGO referente ao estudante que deseja excluir: "))
        for excluir in estudante_lista:
            if excluir.get('Código') == cod_excluir:
                estudante_lista.remove(excluir)
                print(f'\nO estudante com código {cod_excluir} foi removido!')
                break
        else:
            print(f'\nO código {cod_excluir} não foi encontrado.')
    # Salvar os dados do estudante no arquivo
    salvar_dados(estudante_lista)


# Programa Principal (Menu Principal)
print("\nOlá, seja bem-vindo (a)!")
while menu_p != 0:
    menu_p = menu_principal()
    # As opções abaixo como funções
    if menu_p == 1:
        titulo("ESTUDANTES")
    # Opções não desenvolvidas
    elif menu_p == 2:
        titulo("PROFESSORES")
        develop()
        continue
    elif menu_p == 3:
        titulo("DISCIPLINAS")
        develop()
        continue
    elif menu_p == 4:
        titulo("TURMAS")
        develop()
        continue
    elif menu_p == 5:
        titulo("MATRÍCULAS")
        develop()
        continue
    elif menu_p == 0:
        # Caso o usuário digite 0 (zero) o sistema encerra.
        titulo("SISTEMA ENCERRADO")
        break
    else:
        # Caso o usuário digite qualquer número que não esteja listado no menu, aparece uma mensagem de erro.
        print("\nValor inválido! Por favor, selecione uma das opções abaixo:")
        continue

# Programa Secundário (Menu de Operações)
    menu_o = 99999999
    estudante_lista = carregar_dados()
    while menu_o != 0:
        menu_o = menu_operacoes()
        if menu_o == 1:
            incluir_estudante()
        elif menu_o == 2:
            listar_estudante()
        elif menu_o == 3:
            atualizar_estudante()
        elif menu_o == 4:
            excluir_estudante()
        elif menu_o == 0:
            # O usuário tem a opção de voltar ao menu principal.
            print("\nVocê voltou ao menu principal.")
        else:
            # Qualquer número que não esteja no menu será invalidado.
            print("\nValor inválido! Por favor, selecione uma das opções abaixo:")
            continue
