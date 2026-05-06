# Análise Detalhada do Código - num_primo.py (Versão Interativa)

Explicação linha a linha do código refatorado com técnicas de **Clean Code** que solicita um número do usuário e verifica se é primo:

---

## Imports e Configurações (Linhas 1-3)

### Linhas 1-3:

```python
"""Módulo para verificação de números primos com algoritmo otimizado."""

from math import isqrt
```

- **Linha 1:** Docstring do módulo descrevendo seu propósito de forma clara e concisa
- **Linha 3:** Importa `isqrt` diretamente do módulo `math` **(Clean Code)** - Melhor que `import math` e depois `math.isqrt()`, pois:
  - Deixa clara a dependência no topo do arquivo
  - Reduz acoplamento
  - Melhora a legibilidade
  - **Nota:** Nenhum import adicional é necessário! O `input()` é built-in do Python

---

## Definição da Função Principal (Linhas 6-39)

### Linhas 11-27: Docstring e Validação

```python
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
```

**Clean Code aplicado:**

- **Assinatura com type hints:** `(numero: int) -> bool` **(Clean Code)** 
  - Deixa claro os tipos de entrada e saída
  - Melhora a autocompletar em IDEs
  - Facilita detecção de erros estáticos

- **Docstring completa:** Segue PEP 257 com seções Args, Returns e Raises
  - Essencial para documentação automática
  - Melhora a compreensão do código
  - Descreve comportamento esperado e exceções

- **Validação de tipo:** Verificar se a entrada é um inteiro **(Defensive Programming)**
  - Previne erros sutil durante execução
  - Falha rápido e explicitamente

- **Nome da variável mais descritivo:** `numero` em vez de `n` **(Naming Convention)**
  - Aumenta legibilidade
  - Reduz necessidade de comentários

---

## Verificações Iniciais (Linhas 28-37)

### Linhas 28-37: Validações Rápidas

```python
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    
    # 2 e 3 são primos
    if numero <= 3:
        return True
    
    # Números pares não são primos
    if numero % 2 == 0:
        return False
```

**Explicação:**
- **Comentários significativos:** Explicam *por quê*, não *o quê* **(Clean Code)** - Reduz ambiguidade
- **Linha 30-31:** Números ≤ 1 não são primos por definição
- **Linha 33-34:** 2 e 3 são primos (casos base), evita cálculos desnecessários
- **Linha 36-37:** Números pares não são primos (exceto 2, já tratado). Eliminação de metade do espaço de busca

---

## Otimização com Raiz Quadrada (Linhas 39-41)

```python
    # Verifica divisores ímpares até a raiz quadrada
    limite = isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False
    
    return True
```

**Explicação:**
- **Linha 39:** Comentário explicativo **(Self-documenting Code)** - Deixa claro a estratégia
- **Linha 40:** `isqrt()` importado no topo **(Clean Code)** - Mais limpo que `import math` inline
  - Calcula raiz quadrada inteira de `numero`
  - **Otimização crucial:** só precisa verificar até √n
  
- **Linhas 41-43:** Loop otimizado
  - Começa em 3 (já testou 2)
  - Incrementa de 2 em 2 (apenas números ímpares)
  - Vai até √numero (inclusive)
  
- **Linha 44-45:** Se encontra divisor, não é primo. Retorna `False`

- **Linha 47:** Se completa o loop sem encontrar divisores, é primo

---

## Função para Solicitar Entrada do Usuário (Linhas 42-55)

```python
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
```

**Explicação:**

- **Assinatura:** `() -> int` - Não recebe parâmetros, retorna um inteiro
- **Docstring completa** **(Clean Code)** - Documenta o propósito, retorno e exceções possíveis

- **Loop infinito:** `while True:` - Continua pedindo até usuário digitar valor válido
  - **Validação robusta:** Garante que será retornado sempre um inteiro válido

- **`input()`** - Função built-in do Python que:
  - Exibe mensagem ao usuário
  - Aguarda entrada via teclado
  - Retorna string com o digitado

- **`int(entrada)`** - Converte string em inteiro
  - Se a string não for um número válido, lança `ValueError`

- **Bloco try-except** **(Defensive Programming)** - Trata erros graciosamente:
  - Se conversão falhar, mostra mensagem amigável com ❌
  - Pede ao usuário tentar novamente
  - Nunca deixa o programa quebrar por entrada inválida

---

## Função Principal de Verificação (Linhas 58-68)

```python
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
```

**Explicação:**

- **Assinatura:** `() -> None` - Não recebe parâmetros, não retorna valor
- **Docstring clara** **(Clean Code)** - Descreve fluxo e comportamento

- **Linha 63:** Chama `obter_numero_usuario()` e armazena resultado
  - Aguarda validação do usuário
  - Garante que `numero` é sempre um inteiro válido

- **Linhas 65-68:** Verifica e exibe resultado
  - Chama `eh_primo(numero)` para verificação
  - Usa expressão condicional (ternário) com emoji para melhor UX
  - ✅ para primo, ❌ para não primo
  - **F-string** para formatação clara

---

## Bloco de Execução Principal (Linhas 71-72)

```python
if __name__ == '__main__':
    verificar_numero_primo()
```

**Explicação:**

- **`if __name__ == '__main__':`** - Garante execução apenas quando rodado diretamente, não quando importado como módulo
- **Chama função dedicada:** `verificar_numero_primo()` **(Clean Code)** - Melhor que ter lógica espalhada
  - Inicia o fluxo interativo com o usuário
  - Solicita número
  - Valida entrada
  - Verifica se é primo
  - Exibe resultado

---

## Fluxo de Execução

1. **Usuário roda** `python num_primo.py`
2. **Programa exibe:** "Digite um número inteiro: "
3. **Usuário digita:** um número (ex: 17)
4. **Validação:**
   - Se número válido → continua
   - Se inválido → mensagem de erro e volta ao passo 2
5. **`eh_primo(17)`** calcula se 17 é primo
6. **Resultado exibido:** "✅ 17 é um número PRIMO!"

### Exemplos de Execução:

```
Digite um número inteiro: 17
✅ 17 é um número PRIMO!
```

```
Digite um número inteiro: 20
❌ 20 NÃO é um número primo.
```

```
Digite um número inteiro: abc
❌ Erro: 'abc' não é um número inteiro válido. Tente novamente.
Digite um número inteiro: 23
✅ 23 é um número PRIMO!
```

---

## Melhorias Aplicadas (Clean Code & Best Practices)

| Técnica | Antes | Depois | Benefício |
|---------|-------|--------|-----------|
| **Type Hints** | Nenhum | `int -> bool`, `() -> int`, `() -> None` | Melhor verificação de tipos, autocompletar em IDE |
| **Imports** | `import math` (inline) | `from math import isqrt` (topo) | Deixa dependências claras, legibilidade |
| **Docstrings** | Nenhuma | Completas com Args/Returns/Raises | Documentação automática e legibilidade |
| **Validação de Entrada** | Não há | try-except com `isinstance()` e conversão | Defensive programming, tratamento explicito de erros |
| **Nomes de Variáveis** | `n`, `i` | `numero`, `divisor`, `entrada` | Maior clareza e auto-documentação |
| **Comentários** | Nenhum | Estratégicos e significativos | Explicam "por quê", não "o quê" |
| **Separação de Responsabilidades** | Tudo em main | 3 funções dedicadas | Cada função tem um propósito claro |
| **User Experience** | Output simples | Emojis e mensagens claras | Melhor experiência do usuário |
| **Interatividade** | Testes fixos | Input dinâmico do usuário | Programa flexível e reutilizável |

---

## Análise de Complexidade

## Análise de Complexidade

- **Complexidade de Tempo:** O(√n) 
  - Verifica apenas divisores até a raiz quadrada
  - Incrementa de 2 em 2 (apenas ímpares)
  
- **Complexidade de Espaço:** O(1) 
  - Não usa estruturas de dados auxiliares
  - Entrada do usuário não conta na complexidade do algoritmo

---

## Vantagens do Código Final

1. ✅ **Validações rápidas:** Descarta ≤1 e pares imediatamente
2. ✅ **Raiz quadrada como limite:** Reduz significativamente iterações
3. ✅ **Incremento por 2:** Ignora números pares após testar divisibilidade
4. ✅ **Didático:** Fácil de entender e implementar
5. ✅ **Robusto:** Valida entrada com type hints e try-except
6. ✅ **Interativo:** Solicita entrada dinâmica do usuário
7. ✅ **Manutenível:** Code limpo com documentação clara
8. ✅ **Amigável:** Emojis e mensagens claras para melhor UX

---

## Como Executar

```bash
python num_primo.py
```

O programa solicitará um número e informará se é primo ou não!
