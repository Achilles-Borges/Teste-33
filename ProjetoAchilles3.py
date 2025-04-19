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