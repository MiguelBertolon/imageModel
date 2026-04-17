"""
Módulo para cálculo de estatísticas básicas de uma lista de números.
"""

from typing import List, Tuple


def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros: Lista de números float para análise.

    Returns:
        Tupla contendo (soma_total, media, valor_maximo, valor_minimo).

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    soma_total = sum(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    media = soma_total / len(numeros)

    return soma_total, media, valor_maximo, valor_minimo


def exibir_estatisticas(numeros: List[float]) -> None:
    """
    Calcula e exibe as estatísticas de uma lista de números.

    Args:
        numeros: Lista de números para análise.
    """
    try:
        soma_total, media, valor_maximo, valor_minimo = calcular_estatisticas(numeros)

        print("📊 Estatísticas dos Números:")
        print(f"   Soma Total: {soma_total}")
        print(f"   Média: {media:.2f}")
        print(f"   Valor Máximo: {valor_maximo}")
        print(f"   Valor Mínimo: {valor_minimo}")
    except ValueError as erro:
        print(f"❌ Erro: {erro}")


if __name__ == '__main__':
    # Lista de exemplo para demonstração
    lista_exemplo = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    exibir_estatisticas(lista_exemplo)