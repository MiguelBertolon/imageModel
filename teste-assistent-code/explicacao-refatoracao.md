# Explicação da refatoração

## Código original

O código original tinha a função `c(l)` para calcular o total, a média, o maior e o menor valor de uma lista:

- Usava loops manuais para somar elementos e calcular média.
- Calculava máximo e mínimo usando `for i in range(len(l))` e índices.
- Tinha nomes de variáveis curtos e pouco descritivos (`c`, `l`, `t`, `m`, `mx`, `mn`).
- Retornava os valores em uma tupla, mas não havia encapsulamento claro de responsabilidade.

## Refatoração aplicada em `refatoracao.py`

### 1. Nomes claros e significativos

- `c` foi renomeada para `calcular_estatisticas`.
- `l` foi renomeada para `numeros`.
- `t` virou `soma_total`.
- `m` virou `media`.
- `mx` virou `valor_maximo`.
- `mn` virou `valor_minimo`.

Isso deixa o código mais legível e fácil de entender sem precisar decodificar abreviações.

### 2. Separação de responsabilidades

- A lógica de cálculo foi movida para `calcular_estatisticas`.
- A apresentação dos resultados foi colocada em `exibir_estatisticas`.

Com isso, cada função tem uma única responsabilidade: uma só calcula valores e outra só exibe os resultados.

### 3. Uso de funções padrão do Python

- A soma agora é feita com `sum(numeros)` em vez de um loop manual.
- O maior valor usa `max(numeros)`.
- O menor valor usa `min(numeros)`.

Isso reduz complexidade e aproveita construções mais expressivas e eficientes da linguagem.

### 4. Validação de entrada

- A função lança `ValueError` quando a lista está vazia.

Isso garante que o cálculo da média não cause uma divisão por zero e torna o comportamento do código mais previsível.

### 5. Documentação e estrutura

- Adicionei docstrings em ambas as funções para explicar o propósito, parâmetros e retorno.
- A execução do script ficou sob `if __name__ == '__main__':`, o que permite importar as funções sem executar imediatamente o código de exemplo.

## Benefícios da refatoração

- Melhor legibilidade.
- Funções com nomes autodescritivos.
- Menos código repetido e menos lógica imperativa.
- Código mais fácil de testar e manter.
- Comportamento mais seguro para listas vazias.
