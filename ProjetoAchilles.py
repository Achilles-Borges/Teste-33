# Sistema de Gerenciamento de Restaurante - Fase 1
estoque = []
cardapio = []

def menu_principal():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Gestão de Estoque")
        print("2. Gestão de Cardápio")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_estoque()
        elif opcao == "2":
            menu_cardapio()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

def menu_estoque():
    while True:
        print("\n--- Gestão de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Consultar Estoque")
        print("3. Atualizar Produto")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_estoque()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

def cadastrar_produto():
    codigo = input("Código: ")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    unidade = input("Unidade de medida: ")
    preco = float(input("Preço unitário: "))
    validade = input("Data de validade (dd/mm/aaaa): ")
    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "unidade": unidade,
        "preco": preco,
        "validade": validade
    }
    estoque.append(produto)
    print("Produto cadastrado com sucesso!")

def consultar_estoque():
    if not estoque:
        print("Estoque vazio.")
    for p in estoque:
        print(f"{p['codigo']} | {p['nome']} | {p['quantidade']} {p['unidade']} | R${p['preco']:.2f} | Vence: {p['validade']}")

def atualizar_produto():
    cod = input("Informe o código do produto a atualizar: ")
    for p in estoque:
        if p["codigo"] == cod:
            p["quantidade"] = int(input("Nova quantidade: "))
            print("Produto atualizado.")
            return
    print("Produto não encontrado.")

def menu_cardapio():
    while True:
        print("\n--- Gestão de Cardápio ---")
        print("1. Cadastrar Item")
        print("2. Consultar Cardápio")
        print("3. Atualizar Item")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_item_cardapio()
        elif opcao == "2":
            consultar_cardapio()
        elif opcao == "3":
            atualizar_item_cardapio()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

def cadastrar_item_cardapio():
    nome = input("Nome do prato: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    ingredientes = input("Ingredientes (separados por vírgula): ").split(",")
    item = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "ingredientes": [i.strip() for i in ingredientes]
    }
    cardapio.append(item)
    print("Item cadastrado no cardápio!")

def consultar_cardapio():
    if not cardapio:
        print("Cardápio vazio.")
    for i in cardapio:
        print(f"{i['nome']} | {i['descricao']} | R${i['preco']:.2f} | Ingredientes: {', '.join(i['ingredientes'])}")

def atualizar_item_cardapio():
    nome = input("Informe o nome do prato a atualizar: ")
    for i in cardapio:
        if i["nome"] == nome:
            i["preco"] = float(input("Novo preço: "))
            print("Item atualizado.")
            return
    print("Item não encontrado.")

menu_principal()