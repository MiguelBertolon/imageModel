# Explicação das Correções no Código debug.py

## Problemas Identificados no Código Original

1. **Erros de Sintaxe**:
   - Na linha 5, a string no `input` estava sem aspas: `input(Preço do item 1? )` deveria ser `input("Preço do item 1? ")`.
   - Na linha 20, a f-string estava incompleta: `print(" Item 2:        R$ {total_item2:.2f}")` faltava o prefixo `f`.
   - Na linha 27, `round(total, 2)` era redundante, pois `.2f` já formata para 2 casas decimais.

2. **Problemas de Tipos de Dados**:
   - `desconto_cupom` era uma string (resultado de `input`), mas era usado como número em operações matemáticas e comparações (`desconto_cupom / 100` e `desconto_cupom > 0`), causando erros de tipo.

3. **Estrutura do Código (Violação de Clean Code)**:
   - Todo o código estava no escopo global, sem funções, tornando-o difícil de ler, testar e manter.
   - Código repetitivo: Entrada de dados para 3 itens era copiada e colada.
   - Nomes de variáveis ruins: `qtd1`, `item1`, etc., não eram descritivos.
   - Números mágicos: `0.10` para imposto hardcoded sem constante.
   - Sem tratamento de erros: Entrada inválida poderia quebrar o programa.
   - Sem documentação: Não havia comentários ou docstrings explicando o que cada parte fazia.

4. **Outros Problemas**:
   - Indentação inconsistente (linha 23: `if desconto_cupom > 0:` sem indentação correta na linha seguinte).
   - Código monolítico: Tudo em uma sequência linear, sem separação de responsabilidades.

## Como Foi Arrurado

1. **Correção de Sintaxe e Tipos**:
   - Adicionei aspas nas strings de `input`.
   - Corrigi a f-string adicionando `f`.
   - Converti `desconto_cupom` para `float` usando `try-except` para lidar com entradas inválidas.
   - Removi `round(total, 2)` pois `.2f` já cuida da formatação.

2. **Aplicação de Princípios de Clean Code**:
   - **Separação de Responsabilidades**: Dividi o código em funções pequenas e focadas:
     - `get_client_name()`: Para obter o nome do cliente.
     - `get_item_details()`: Para obter quantidade e preço de um item.
     - `calculate_item_total()`, `calculate_subtotal()`, `calculate_tax()`, `calculate_discount()`: Para cálculos.
     - `get_discount_percentage()`: Com tratamento de erro.
     - `print_receipt()`: Para exibir o resultado.
     - `main()`: Função principal que orquestra tudo.
   - **Uso de Constantes**: Defini `TAX_RATE = 0.10` para evitar números mágicos.
   - **Estruturas de Dados**: Usei listas (`items` e `item_totals`) e loops para evitar repetição.
   - **Nomes Descritivos**: Variáveis como `quantity`, `price`, `subtotal`, etc.
   - **Tratamento de Erros**: Adicionei `try-except` em `get_discount_percentage()` para entradas inválidas.
   - **Documentação**: Adicionei docstrings em cada função explicando seu propósito.
   - **Execução como Script**: Usei `if __name__ == "__main__":` para permitir execução direta ou importação.

3. **Outras Técnicas Aplicadas**:
   - **DRY (Don't Repeat Yourself)**: Eliminei código duplicado usando loops e funções.
   - **Legibilidade**: Código mais fácil de entender e manter.
   - **Testabilidade**: Funções isoladas podem ser testadas individualmente.
   - **Manutenibilidade**: Mudanças em cálculos ou entrada podem ser feitas em funções específicas.

O código agora está mais robusto, legível e segue boas práticas de programação em Python.