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


#FASE 2

mesas = []
pedidos = []
cardapio = [
    {"nome": "Pizza", "preco": 30.0},
    {"nome": "Hambúrguer", "preco": 20.0},
    {"nome": "Suco", "preco": 8.0},
]

def cadastrar_mesa():
    numero = input("Número da mesa: ")
    capacidade = input("Capacidade da mesa: ")
    mesa = {
        "numero": numero,
        "capacidade": capacidade,
        "status": "livre",
        "cliente": None
    }
    mesas.append(mesa)
    print("Mesa cadastrada com sucesso.")

def listar_mesas():
    print("\n--- Mesas ---")
    for mesa in mesas:
        print(f"Mesa {mesa['numero']} | Capacidade: {mesa['capacidade']} | Status: {mesa['status']}")

def atribuir_cliente_mesa():
    numero = input("Número da mesa para atribuir cliente: ")
    nome_cliente = input("Nome do cliente: ")
    for mesa in mesas:
        if mesa["numero"] == numero:
            if mesa["status"] == "livre":
                mesa["status"] = "ocupada"
                mesa["cliente"] = nome_cliente
                print("Cliente atribuído à mesa.")
                return
            else:
                print("Mesa já está ocupada.")
                return
    print("Mesa não encontrada.")

def mostrar_cardapio():
    print("\n--- Cardápio ---")
    for i, item in enumerate(cardapio):
        print(f"{i + 1}. {item['nome']} - R${item['preco']}:.2f")


        #Fase3

        def calcular_conta():
    numero = input("Número da mesa para calcular conta: ")
    for pedido in pedidos:
        if pedido["mesa"] == numero:
            total = sum(item["preco"] for item in pedido["itens"])
            print(f"\nTotal da mesa {numero}: R${total:.2f}")
            dividir = input("Deseja dividir a conta entre clientes? (s/n): ").lower()
            if dividir == "s":
                pessoas = int(input("Número de pessoas: "))
                valor_por_pessoa = total / pessoas
                print(f"Cada pessoa deve pagar: R${valor_por_pessoa:.2f}")
            aplicar_taxa = input("Aplicar taxa de serviço (10%)? (s/n): ").lower()
            if aplicar_taxa == "s":
                total *= 1.1
                print(f"Total com taxa de serviço: R${total:.2f}")
            aplicar_desc = input("Aplicar desconto? (s/n): ").lower()
            if aplicar_desc == "s":
                desconto = float(input("Digite o valor do desconto: "))
                total -= desconto
                print(f"Total com desconto: R${total:.2f}")
            return total
    print("Pedido não encontrado.")
    return None

def registrar_pagamento():
    numero = input("Número da mesa para pagamento: ")
    total = calcular_conta()
    if total is None:
        return

    forma = input("Forma de pagamento (dinheiro/cartao): ").lower()
    if forma == "dinheiro":
        valor_pago = float(input("Valor pago: "))
        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento aceito. Troco: R${troco:.2f}")
        else:
            print("Valor insuficiente.")
            return
    elif forma == "cartao":
        print("Pagamento com cartão aceito.")
    else:
        print("Forma de pagamento inválida.")
        return

    for mesa in mesas:
        if mesa["numero"] == numero:
            mesa["status"] = "livre"
            mesa["cliente"] = None
            break
    print("Mesa liberada.")

def menu_pagamento():
    while True:
        print("\n")


        #fase4

        


estoque = [
    {"codigo": "ING1", "nome": "Queijo", "quantidade": 1000, "unidade": "g", "preco": 0.05, "validade": "2025-05-01"},
    {"codigo": "ING2", "nome": "Molho", "quantidade": 500, "unidade": "ml", "preco": 0.03, "validade": "2025-05-10"},
    {"codigo": "ING3", "nome": "Pão", "quantidade": 50, "unidade": "un", "preco": 0.50, "validade": "2025-04-30"},
]

receitas = {
    "Pizza": [
        {"ingrediente": "Queijo", "quantidade": 200},
        {"ingrediente": "Molho", "quantidade": 100}
    ],
    "Hambúrguer": [
        {"ingrediente": "Pão", "quantidade": 2},
        {"ingrediente": "Queijo", "quantidade": 100}
    ]
} 


