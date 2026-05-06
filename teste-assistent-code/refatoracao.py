"""
Módulo para cálculo de estatísticas básicas de uma lista de números.
"""

from typing import List, Tuple


def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula as principais estatísticas descritivas de um conjunto de números.

    Calcula a soma total, média aritmética, valor máximo e mínimo de uma lista.
    Utiliza funcções nativas do Python para garantir eficiência e precisão.

    Args:
        numeros: Lista de números (float) para análise estatística.

    Returns:
        Tupla[float, float, float, float]: Contém respectivamente:
            - soma_total: Soma de todos os números
            - media: Média aritmética dos números
            - valor_maximo: Maior valor da lista
            - valor_minimo: Menor valor da lista

    Raises:
        ValueError: Se a lista estiver vazia.
        TypeError: Se a lista contiver elementos não numéricos (esperado float ou int).
        
    Exemplos:
        >>> calcular_estatisticas([2, 4, 6, 8, 10])
        (30.0, 6.0, 10, 2)
        >>> calcular_estatisticas([])
        Levanta ValueError
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
    Calcula e exibe as estatísticas descritivas de forma formatada no console.

    Funciona como wrapper em torno de calcular_estatisticas(), adicionando
    tratamento de erros e formatação visual com emojis para melhor legibilidade.

    Args:
        numeros: Lista de números (float ou int) para análise.
        
    Nota:
        Se a lista estiver vazia, uma mensagem de erro é exibida no console
        sem interromper a execução do programa.
        
    Exemplos:
        >>> exibir_estatisticas([23, 7, 45, 2, 67])
        📊 Estatísticas dos Números:
           Soma Total: 144
           Média: 28.80
           Valor Máximo: 67
           Valor Mínimo: 2
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