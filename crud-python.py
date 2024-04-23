import datetime

# Base de dados fictícia
computadores = {
    1: {"nome": "PC 1", "disponivel": True, "horas_uso": 0},
    2: {"nome": "PC 2", "disponivel": True, "horas_uso": 0},
    3: {"nome": "PC 3", "disponivel": True, "horas_uso": 0},
}

produtos = {
    1: {"nome": "Mouse", "quantidade": 30},
    2: {"nome": "Teclado", "quantidade": 15},
    3: {"nome": "Fone de Ouvido", "quantidade": 50},
}

usuarios = {}

reservas = {}

feedbacks = []

def formatar_data_hora(data_hora):
    try:
        return datetime.datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except ValueError:
        return None

# Funções para controle das máquinas
def listar_computadores():
    print("\n===== LISTAR COMPUTADORES =====")
    for id, info in computadores.items():
        print(f"ID: {id}, Nome: {info['nome']}, Disponível: {info['disponivel']}")
    print("")

def cadastrar_computador(nome):
    novo_id = max(computadores.keys(), default=0) + 1
    computadores[novo_id] = {"nome": nome, "disponivel": True, "horas_uso": 0}
    print(f"Computador {nome} cadastrado com sucesso!\n")

def consultar_computador(id):
    if id in computadores:
        info = computadores[id]
        print(f"\nID: {id}, Nome: {info['nome']}, Disponível: {info['disponivel']}\n")
    else:
        print("Computador não encontrado.\n")

def atualizar_computador(id, nome, disponivel):
    if id in computadores:
        computadores[id] = {"nome": nome, "disponivel": disponivel, "horas_uso": 0}
        print("Computador atualizado com sucesso!\n")
    else:
        print("Computador não encontrado.\n")

def remover_computador(id):
    if id in computadores:
        del computadores[id]
        print("Computador removido com sucesso!\n")
    else:
        print("Computador não encontrado.\n")

# Funções para controle de produtos
def listar_produtos():
    print("\n===== LISTAR PRODUTOS =====")
    for id, info in produtos.items():
        print(f"ID: {id}, Nome: {info['nome']}, Quantidade: {info['quantidade']}")
    print("")

def cadastrar_produto(nome, quantidade):
    novo_id = max(produtos.keys(), default=0) + 1
    produtos[novo_id] = {"nome": nome, "quantidade": quantidade}
    print(f"Produto {nome} cadastrado com sucesso!\n")

def consultar_produto(id):
    if id in produtos:
        info = produtos[id]
        print(f"\nID: {id}, Nome: {info['nome']}, Quantidade: {info['quantidade']}\n")
    else:
        print("Produto não encontrado.\n")

def atualizar_produto(id, nome, quantidade):
    if id in produtos:
        produtos[id] = {"nome": nome, "quantidade": quantidade}
        print("Produto atualizado com sucesso!\n")
    else:
        print("Produto não encontrado.\n")

def remover_produto(id):
    if id in produtos:
        del produtos[id]
        print("Produto removido com sucesso!\n")
    else:
        print("Produto não encontrado.\n")

# Funções para controle de usuários
def listar_usuarios():
    print("\n===== LISTAR USUÁRIOS =====")
    for cpf, info in usuarios.items():
        print(f"CPF: {cpf}, Nome: {info['nome']}, E-mail: {info['email']}, Telefone: {info['telefone']}")
    print("")

def cadastrar_usuario(nome, cpf, email, telefone):
    if cpf in usuarios:
        print("Usuário já cadastrado.\n")
    else:
        usuarios[cpf] = {"nome": nome, "email": email, "telefone": telefone}
        print(f"Usuário {nome} cadastrado com sucesso!\n")

def consultar_usuario(cpf):
    if cpf in usuarios:
        info = usuarios[cpf]
        print(f"\nCPF: {cpf}, Nome: {info['nome']}, E-mail: {info['email']}, Telefone: {info['telefone']}\n")
    else:
        print("Usuário não encontrado.\n")

def atualizar_usuario(cpf, nome, email, telefone):
    if cpf in usuarios:
        usuarios[cpf] = {"nome": nome, "email": email, "telefone": telefone}
        print("Usuário atualizado com sucesso!\n")
    else:
        print("Usuário não encontrado.\n")

def remover_usuario(cpf):
    if cpf in usuarios:
        del usuarios[cpf]
        print("Usuário removido com sucesso!\n")
    else:
        print("Usuário não encontrado.\n")

# Funções para reserva de máquina
def reservar_computador(id, cliente, data_hora):
    data_hora_reserva = formatar_data_hora(data_hora)
    if data_hora_reserva is None:
        print("Formato de data/hora inválido. Use o formato dd/mm/aaaa hh:mm.\n")
        return

    if id in computadores:
        if computadores[id]["disponivel"]:
            if not verificar_conflito_reserva(id, data_hora_reserva):
                computadores[id]["disponivel"] = False
                reservas[(id, data_hora_reserva)] = cliente
                print(f"Computador {id} reservado para o cliente {cliente} às {data_hora}.\n")
            else:
                print("Conflito de reserva. O computador já está reservado para este horário.\n")
        else:
            print("Computador não disponível.\n")
    else:
        print("Computador não encontrado.\n")

def verificar_conflito_reserva(id, data_hora_reserva):
    for reserva_id, reserva_data_hora in reservas.keys():
        if reserva_id == id and reserva_data_hora == data_hora_reserva:
            return True
    return False

def iniciar_tempo_uso(id):
    if id in computadores:
        if not computadores[id]["disponivel"]:
            computadores[id]["horas_uso"] += 1
            print(f"Tempo de uso do computador {id} iniciado.")
        else:
            print("Computador não reservado ou disponível.")
    else:
        print("Computador não encontrado.")

def encerrar_tempo_uso(id):
    if id in computadores:
        if not computadores[id]["disponivel"]:
            computadores[id]["disponivel"] = True
            print(f"Tempo de uso do computador {id} encerrado.")
        else:
            print("Computador não reservado ou disponível.")
    else:
        print("Computador não encontrado.")

# Funções para feedback do cliente
def coletar_feedback(cliente, nota, comentario):
    feedbacks.append({"cliente": cliente, "nota": nota, "comentario": comentario})
    print("Feedback coletado com sucesso!\n")

def listar_feedbacks():
    print("\n===== LISTAR FEEDBACKS =====")
    for feedback in feedbacks:
        print(f"Cliente: {feedback['cliente']}, Nota: {feedback['nota']}, Comentário: {feedback['comentario']}")
    print("")

# Menu de interação com o usuário
while True:
    print("\n===== MENU =====")
    print("1. Gerenciar Computadores")
    print("2. Gerenciar Produtos")
    print("3. Gerenciar Usuários")
    print("4. Reservar Computador")
    print("5. Iniciar Tempo de Uso")
    print("6. Encerrar Tempo de Uso")
    print("7. Coletar Feedback dos Usuários")
    print("8. Listar Feedbacks")
    print("9. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        while True:
            print("\n===== GERENCIAR COMPUTADORES =====")
            print("1. Listar Computadores")
            print("2. Cadastrar Computador")
            print("3. Consultar Computador")
            print("4. Atualizar Computador")
            print("5. Remover Computador")
            print("6. Voltar ao Menu Principal")

            opcao_computadores = input("\nEscolha uma opção: ")

            if opcao_computadores == "1":
                listar_computadores()
            elif opcao_computadores == "2":
                nome = input("Digite o nome do computador: ")
                cadastrar_computador(nome)
            elif opcao_computadores == "3":
                id = int(input("Digite o ID do computador: "))
                consultar_computador(id)
            elif opcao_computadores == "4":
                id = int(input("Digite o ID do computador: "))
                nome = input("Digite o novo nome do computador: ")
                disponivel = input("O computador está disponível? (S/N): ").upper() == "S"
                atualizar_computador(id, nome, disponivel)
            elif opcao_computadores == "5":
                id = int(input("Digite o ID do computador a ser removido: "))
                remover_computador(id)
            elif opcao_computadores == "6":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    elif opcao == "2":
        while True:
            print("\n===== GERENCIAR PRODUTOS =====")
            print("1. Listar Produtos")
            print("2. Cadastrar Produto")
            print("3. Consultar Produto")
            print("4. Atualizar Produto")
            print("5. Remover Produto")
            print("6. Voltar ao Menu Principal")

            opcao_produtos = input("\nEscolha uma opção: ")

            if opcao_produtos == "1":
                listar_produtos()
            elif opcao_produtos == "2":
                nome = input("Digite o nome do produto: ")
                quantidade = int(input("Digite a quantidade disponível: "))
                cadastrar_produto(nome, quantidade)
            elif opcao_produtos == "3":
                id = int(input("Digite o ID do produto: "))
                consultar_produto(id)
            elif opcao_produtos == "4":
                id = int(input("Digite o ID do produto: "))
                nome = input("Digite o novo nome do produto: ")
                quantidade = int(input("Digite a nova quantidade disponível: "))
                atualizar_produto(id, nome, quantidade)
            elif opcao_produtos == "5":
                id = int(input("Digite o ID do produto a ser removido: "))
                remover_produto(id)
            elif opcao_produtos == "6":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    elif opcao == "3":
        while True:
            print("\n===== GERENCIAR USUÁRIOS =====")
            print("1. Listar Usuários")
            print("2. Cadastrar Usuário")
            print("3. Consultar Usuário")
            print("4. Atualizar Usuário")
            print("5. Remover Usuário")
            print("6. Voltar ao Menu Principal")

            opcao_usuarios = input("\nEscolha uma opção: ")

            if opcao_usuarios == "1":
                listar_usuarios()
            elif opcao_usuarios == "2":
                nome = input("Digite o nome do usuário: ")
                cpf = input("Digite o CPF do usuário: ")
                email = input("Digite o e-mail do usuário: ")
                telefone = input("Digite o telefone do usuário: ")
                cadastrar_usuario(nome, cpf, email, telefone)
            elif opcao_usuarios == "3":
                cpf = input("Digite o CPF do usuário: ")
                consultar_usuario(cpf)
            elif opcao_usuarios == "4":
                cpf = input("Digite o CPF do usuário: ")
                nome = input("Digite o novo nome do usuário: ")
                email = input("Digite o novo e-mail do usuário: ")
                telefone = input("Digite o novo telefone do usuário: ")
                atualizar_usuario(cpf, nome, email, telefone)
            elif opcao_usuarios == "5":
                cpf = input("Digite o CPF do usuário a ser removido: ")
                remover_usuario(cpf)
            elif opcao_usuarios == "6":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    elif opcao == "4":
        print("\n===== RESERVAR COMPUTADOR =====")
        id = int(input("Digite o ID do computador a ser reservado: "))
        cliente = input("Digite o nome do cliente: ")
        data_hora = input("Digite a data e hora da reserva (formato: dd/mm/aaaa hh:mm): ")
        reservar_computador(id, cliente, data_hora)

    elif opcao == "5":
        print("\n===== INICIAR TEMPO DE USO =====")
        id = input("Digite o ID do computador para iniciar o tempo de uso: ")
        iniciar_tempo_uso(id)

    elif opcao == "6":
        print("\n===== ENCERRAR TEMPO DE USO =====")
        id = input("Digite o ID do computador para encerrar o tempo de uso: ")
        encerrar_tempo_uso(id)

    elif opcao == "7":
        print("\n===== COLETAR FEEDBACK DOS USUÁRIOS =====")
        cliente = input("Digite o nome do cliente: ")
        nota = input("Digite a nota (de 1 a 5): ")
        comentario = input("Digite o comentário: ")
        coletar_feedback(cliente, nota, comentario)

    elif opcao == "8":
        listar_feedbacks()

    elif opcao == "9":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")
