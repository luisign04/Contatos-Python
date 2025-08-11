# Gerenciador de Contatos - CRUD em Python
#Membros: João Pedro Santana, Luis Augusto Barbosa, Victor Torres, Ezequiel, Cleybson Teixeira

contatos = []


def cadastrar_contato():

  while True:
    nome = input("Digite o nome: ").strip()
    if nome:
      break
    print("O campo não pode ser vazio")

  while True:
    telefone = input("Digite o número: ").strip()
    if telefone:
      break
    print("O campo não pode ser vazio")

  while True:
    email = input("Digite o e-mail: ").strip()
    if email:
      break
    print("O campo não pode ser vazio")

  contato = {"nome": nome, "telefone": telefone, "email": email}
  contatos.append(contato)
  print(f"Contato '{nome}' cadastrado com sucesso!\n")


def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.\n")
        return
    print("\nLista de Contatos:")
    for i, contato in enumerate(contatos, start=1):
        print(f"{i}. Nome: {contato['nome']} | Tel: {contato['telefone']} | Email: {contato['email']}")
    print()


def atualizar_contato():
    listar_contatos()
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato que deseja atualizar: ")) - 1
        if 0 <= indice < len(contatos):
            print("Deixe em branco para não alterar.")
            nome = input(f"Novo nome ({contatos[indice]['nome']}): ") or contatos[indice]['nome']
            telefone = input(f"Novo telefone ({contatos[indice]['telefone']}): ") or contatos[indice]['telefone']
            email = input(f"Novo e-mail ({contatos[indice]['email']}): ") or contatos[indice]['email']
            contatos[indice] = {"nome": nome, "telefone": telefone, "email": email}
            print("Contato atualizado com sucesso!\n")
        else:
            print("Contato não encontrado.\n")
    except ValueError:
        print("Entrada inválida.\n")


def excluir_contato():
    listar_contatos()
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato que deseja excluir: ")) - 1
        if 0 <= indice < len(contatos):
            removido = contatos.pop(indice)
            print(f"🗑 Contato '{removido['nome']}' removido com sucesso!\n")
        else:
            print("Contato não encontrado.\n")
    except ValueError:
        print("Entrada inválida.\n")


def menu():
    while True:
        print("===== GERENCIADOR DE CONTATOS =====")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Atualizar contato")
        print("4 - Excluir contato")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            atualizar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    menu()
