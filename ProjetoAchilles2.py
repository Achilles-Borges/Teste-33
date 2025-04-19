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