# Constants
# Define a alíquota de imposto em 10% para cálculos de total
TAX_RATE = 0.10

def get_client_name():
    """Obtém o nome do cliente."""
    return input("Qual é seu nome? ")

def get_item_details(item_num):
    """Obtém quantidade e preço de um item."""
    # Solicita a quantidade como inteiro para évitar resultados com decimais
    quantity = int(input(f"Quantidade do item {item_num}: "))
    # Solicita o preço como float para permitir valores com centavos (ex: 10.50)
    price = float(input(f"Preço do item {item_num}? "))
    return quantity, price

def calculate_item_total(quantity, price):
    """Calcula o total de um item."""
    # Multiplicção simples: quantidade × preço unitário
    return quantity * price

def calculate_subtotal(item_totals):
    """Calcula o subtotal somando os totais dos itens."""
    # Usa sum() para evitar loop manual e reduzir complexidade
    return sum(item_totals)

def get_discount_percentage():
    """Obtém o percentual de desconto, tratando erros de entrada."""
    try:
        # Converte para float para permitir descontos como 15.5% (exatidão)
        return float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
    except ValueError:
        # Se o usuário digitar texto inválido, retorna 0 (sem desconto) como padrão seguro
        print("Valor inválido. Considerando 0% de desconto.")
        return 0.0

def calculate_discount(subtotal, discount_percentage):
    """Calcula o valor do desconto."""
    # Fórmula: desconto_valor = subtotal × (percentual / 100)
    # Exemplo: Se subtotal é 100 e desconto é 10%, resultado é 10
    return subtotal * (discount_percentage / 100)

def calculate_tax(subtotal):
    """Calcula o imposto."""
    # Multiplica o subtotal pela alíquota global (10%) definida no topo
    return subtotal * TAX_RATE

def print_receipt(client, item_totals, subtotal, tax, discount_percentage, discount, total):
    """Imprime o recibo."""
    # Define linhas de formatação com 31 caracteres para criar visual limpo e profissional
    linha = "=" * 31
    separador = "-" * 31

    print(linha)
    print(f" Cliente: {client}")
    print(linha)
    # Enumera os itens a partir de 1 para exibição mais intuitiva (não técnica)
    for i, total in enumerate(item_totals, 1):
        print(f" Item {i}:        R$ {total:.2f}")
    print(separador)
    print(f" Subtotal:      R$ {subtotal:.2f}")
    print(f" Imposto (10%): R$ {tax:.2f}")
    # Apenas exibe a linha de desconto se houver desconto (desconto > 0)
    if discount_percentage > 0:
        print(f" Desconto ({discount_percentage:.0f}%): -R$ {discount:.2f}")
    print(linha)
    print(f" TOTAL:         R$ {total:.2f}")
    print(linha)

def main():
    """Função principal do programa."""
    # Coleta o nome do cliente uma única vez no início
    client = get_client_name()
    items = []
    # Itera 3 vezes para obter quantidade e preço de 3 itens diferentes
    for i in range(1, 4):
        qty, price = get_item_details(i)
        # Armazena tupla (quantidade, preço) para cálculos posteriores
        items.append((qty, price))

    # Usa list comprehension para calcular total de cada item em uma linha eficiente
    item_totals = [calculate_item_total(qty, price) for qty, price in items]
    # Calcula valores base para o recibo
    subtotal = calculate_subtotal(item_totals)
    tax = calculate_tax(subtotal)
    discount_percentage = get_discount_percentage()
    discount = calculate_discount(subtotal, discount_percentage)
    # Ordem de operação: subtotal + imposto - desconto = total final
    total = subtotal + tax - discount

    print_receipt(client, item_totals, subtotal, tax, discount_percentage, discount, total)

if __name__ == "__main__":
    main()