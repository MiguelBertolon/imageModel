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
        Tupla contendo (total, média, maior, menor).

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    total = 0.0
    maior = menor = numeros[0]

    for numero in numeros:
        total += numero
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    media = total / len(numeros)

    return total, media, maior, menor


def exibir_estatisticas(numeros: List[float]) -> None:
    """
    Calcula e exibe as estatísticas de uma lista de números.

    Args:
        numeros: Lista de números para análise.
    """
    try:
        total, media, maior, menor = calcular_estatisticas(numeros)

        print("📊 Estatísticas dos Números:")
        print(f"   Total: {total}")
        print(f"   Média: {media:.2f}")
        print(f"   Maior: {maior}")
        print(f"   Menor: {menor}")
    except ValueError as erro:
        print(f"❌ Erro: {erro}")


if __name__ == '__main__':
    # Lista de exemplo
    lista_numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    exibir_estatisticas(lista_numeros)