"""Módulo para verificação de números primos com algoritmo otimizado."""

from math import isqrt


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo utilizando otimização de raiz quadrada.
    
    Este algoritmo utiliza o método de verificação até a raiz quadrada do número,
    oferecendo compplexidade O(√n), significativamente mais rápido que a busca linear.
    
    Args:
        numero: Número inteiro positivo a ser verificado.
        
    Returns:
        bool: True se o número é primo, False caso contrário.
        
    Raises:
        TypeError: Se o parâmetro não for um inteiro.
        
    Exemplos:
        >>> eh_primo(7)
        True
        >>> eh_primo(10)
        False
        >>> eh_primo(1)
        False
    """
    if not isinstance(numero, int):
        raise TypeError("O número deve ser um inteiro.")
    
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    
    # 2 e 3 são primos
    if numero <= 3:
        return True
    
    # Números pares não são primos
    if numero % 2 == 0:
        return False
    
    # Verifica divisores ímpares até a raiz quadrada
    limite = isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False
    
    return True


def obter_numero_usuario() -> int:
    """
    Solicita um número inteiro ao usuário com validação automática de entrada.
    
    A função realiza um loop contínuo até que o usuário digite um valor inteiro válido.
    Mensagens de erro claras são exibidas para orientar o usuário.
    
    Returns:
        int: Número inteiro válido fornecido pelo usuário.
        
    Exemplos:
        >>> # Usuário digita: 42
        >>> resultado = obter_numero_usuario()
        >>> resultado
        42
    """
    while True:
        try:
            entrada = input("Digite um número inteiro: ")
            numero = int(entrada)
            return numero
    Orquestra o fluxo principal da aplicação de verificação de números primos.
    
    A função:
        1. Solicita um número ao usuário com validação
        2. Verifica se o número é primo
        3. Exibe o resultado de forma amigável com indicadores visuais
        
    Exemplo de execução:
        Entrada do usuário: 17
        Saída: ✅ 17 é um número PRIMO!

def verificar_numero_primo() -> None:
    """
    Solicita um número ao usuário e verifica se é primo.
    
    Exibe o resultado de forma legível no console.
    """
    numero = obter_numero_usuario()
    
    if eh_primo(numero):
        print(f"✅ {numero} é um número PRIMO!")
    else:
        print(f"❌ {numero} NÃO é um número primo.")


if __name__ == '__main__':
    verificar_numero_primo()
