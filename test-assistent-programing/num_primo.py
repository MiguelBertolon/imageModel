"""Módulo para verificação de números primos com algoritmo otimizado."""

from math import isqrt


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo usando otimização de raiz quadrada.
    
    Args:
        numero: Número inteiro a ser verificado.
        
    Returns:
        bool: True se o número é primo, False caso contrário.
        
    Raises:
        TypeError: Se o número não for um inteiro.
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
    Solicita um número ao usuário com validação de entrada.
    
    Returns:
        int: Número inteiro válido digitado pelo usuário.
        
    Raises:
        ValueError: Se o usuário não inserir um número inteiro válido.
    """
    while True:
        try:
            entrada = input("Digite um número inteiro: ")
            numero = int(entrada)
            return numero
        except ValueError:
            print(f"❌ Erro: '{entrada}' não é um número inteiro válido. Tente novamente.")


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
