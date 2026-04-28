# Constants
TAX_RATE = 0.10

def get_client_name():
    """Obtém o nome do cliente."""
    return input("Qual é seu nome? ")

def get_item_details(item_num):
    """Obtém quantidade e preço de um item."""
    quantity = int(input(f"Quantidade do item {item_num}: "))
    price = float(input(f"Preço do item {item_num}? "))
    return quantity, price

def calculate_item_total(quantity, price):
    """Calcula o total de um item."""
    return quantity * price

def calculate_subtotal(item_totals):
    """Calcula o subtotal somando os totais dos itens."""
    return sum(item_totals)

def get_discount_percentage():
    """Obtém o percentual de desconto, tratando erros de entrada."""
    try:
        return float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
    except ValueError:
        print("Valor inválido. Considerando 0% de desconto.")
        return 0.0

def calculate_discount(subtotal, discount_percentage):
    """Calcula o valor do desconto."""
    return subtotal * (discount_percentage / 100)

def calculate_tax(subtotal):
    """Calcula o imposto."""
    return subtotal * TAX_RATE

def print_receipt(client, item_totals, subtotal, tax, discount_percentage, discount, total):
    """Imprime o recibo."""
    linha = "=" * 31
    separador = "-" * 31

    print(linha)
    print(f" Cliente: {client}")
    print(linha)
    for i, total in enumerate(item_totals, 1):
        print(f" Item {i}:        R$ {total:.2f}")
    print(separador)
    print(f" Subtotal:      R$ {subtotal:.2f}")
    print(f" Imposto (10%): R$ {tax:.2f}")
    if discount_percentage > 0:
        print(f" Desconto ({discount_percentage:.0f}%): -R$ {discount:.2f}")
    print(linha)
    print(f" TOTAL:         R$ {total:.2f}")
    print(linha)

def main():
    """Função principal do programa."""
    client = get_client_name()
    items = []
    for i in range(1, 4):
        qty, price = get_item_details(i)
        items.append((qty, price))

    item_totals = [calculate_item_total(qty, price) for qty, price in items]
    subtotal = calculate_subtotal(item_totals)
    tax = calculate_tax(subtotal)
    discount_percentage = get_discount_percentage()
    discount = calculate_discount(subtotal, discount_percentage)
    total = subtotal + tax - discount

    print_receipt(client, item_totals, subtotal, tax, discount_percentage, discount, total)

if __name__ == "__main__":
    main()