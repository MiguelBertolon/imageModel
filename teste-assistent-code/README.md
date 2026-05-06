# 📚 Repositório de Práticas com GitHub Copilot

## 🎯 Sobre o Projeto

Este repositório contém uma coleção de scripts Python desenvolvidos como práticas educacionais para aplicar **boas práticas de programação** e **documentação de código** utilizando **GitHub Copilot** como assistente integrado no VS Code.

O projeto incorpora princípios de **Clean Code**, **desenvolvimento defensivo** e **separação de responsabilidades**, resultando em código legível, mantível e bem documentado.

---

## 📁 Estrutura do Repositório

```
test-assistent-programing/
├── debug.py                    # Sistema de cálculo de recibos com comentários inline
├── num_primo.py                # Verificador de números primos com algoritmo otimizado
├── refatoracao.py              # Calculadora de estatísticas descritivas
├── explicacao_debug.md         # Análise detalhada das correções do debug.py
├── explicacao_refatoracao.md   # Documentação da refatoração de código
├── explicacao_num_primo.md     # Explicação linha a linha do algoritmo
└── README.md                   # Este arquivo
```

---

## 🚀 Scripts Disponíveis

### 1. **num_primo.py** — Verificador de Números Primos

**Descrição:**
Script interativo que solicita um número ao usuário e verifica se é primo utilizando algoritmo otimizado com complexidade O(√n).

**Funcionalidades:**
- ✅ Verificação eficiente de primalidade
- ✅ Validação de entrada com loop de retry
- ✅ Interface amigável com indicadores visuais (emojis)
- ✅ Tratamento de exceções com mensagens claras

**Como executar:**
```bash
python num_primo.py
```

**Exemplo de uso:**
```
Digite um número inteiro: 17
✅ 17 é um número PRIMO!
```

**Principais características técnicas:**
- Import direto de `isqrt` do módulo `math` (Clean Code)
- Type hints em todos os parâmetros e retornos
- Docstrings em estilo Google com exemplos de uso
- Validação de tipo com `isinstance()`

---

### 2. **refatoracao.py** — Calculadora de Estatísticas

**Descrição:**
Sistema de cálculo de estatísticas descritivas (soma, média, máximo, mínimo) de uma lista de números, exemplificando princípios de refatoração e Clean Code.

**Funcionalidades:**
- 📊 Cálculo de estatísticas básicas
- 📈 Formatação elegante de resultados
- ✅ Validação de entrada (rejeita listas vazias)
- 🛡️ Tratamento robusto de erros

**Como executar:**
```bash
python refatoracao.py
```

**Exemplo de saída:**
```
📊 Estatísticas dos Números:
   Soma Total: 244
   Média: 24.40
   Valor Máximo: 89
   Valor Mínimo: 2
```

**Aplicações práticas:**
```python
# Pode ser importado em outros scripts
from refatoracao import calcular_estatisticas

resultado = calcular_estatisticas([10, 20, 30, 40])
# Retorna: (100, 25.0, 40, 10)
```

**Principais características técnicas:**
- Separação de responsabilidades (cálculo vs. exibição)
- Uso de type hints e Tuple para retorno múltiplo
- List comprehension para cálculos eficientes
- Exceções customizadas com `ValueError`

---

### 3. **debug.py** — Sistema de Cálculo de Recibos

**Descrição:**
Aplicação completa de PDV (Ponto de Venda) que calcula recibos com suporte a múltiplos itens, descontos e impostos, com foco em **comentários inline explicativos** e lógica clara.

**Funcionalidades:**
- 💳 Cálculo de recibos com até 3 itens
- 🏷️ Suporte a cupons de desconto
- 📋 Formatação visual profissional
- 🛡️ Tratamento de erros em entrada de desconto

**Como executar:**
```bash
python debug.py
```

**Exemplo de fluxo:**
```
Qual é seu nome? João Silva
Quantidade do item 1: 2
Preço do item 1? 50.00
Quantidade do item 2: 1
Preço do item 2? 120.00
Quantidade do item 3: 3
Preço do item 3? 25.50
Você tem um cupom de desconto? (Digite o percentual ou 0): 10

===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 100.00
 Item 2:        R$ 120.00
 Item 3:        R$ 76.50
-------------------------------
 Subtotal:      R$ 296.50
 Imposto (10%): R$ 29.65
 Desconto (10%): -R$ 29.65
===============================
 TOTAL:         R$ 296.50
===============================
```

**Principais características técnicas:**
- Comentários inline explicando decisões de lógica (não apenas o obvio)
- Constante global `TAX_RATE` evitando números mágicos
- Funções focadas com responsabilidade única
- List comprehension para cálculo de totais
- Estrutura de dados com tuplas para pares quantidade-preço

---

## 🛠️ Tecnologias e Ferramentas

| Tecnologia | Versão | Descrição |
|----------|--------|-----------|
| **Python** | 3.8+ | Linguagem de programação |
| **GitHub Copilot** | - | Assistente de code completion via VS Code |
| **VS Code** | Latest | Editor de código |
| **PEP 257** | - | Padrão de docstrings Python |
| **Type Hints** | PEP 484 | Tipagem estática em Python |

---

## 📚 Documentação Aplicada

### Docstrings (estilo Google)

Todos os arquivos possuem docstrings completas em português:

```python
def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo utilizando otimização de raiz quadrada.
    
    Args:
        numero: Número inteiro positivo a ser verificado.
        
    Returns:
        bool: True se o número é primo, False caso contrário.
        
    Exemplos:
        >>> eh_primo(7)
        True
    """
```

### Comentários Inline

Comentários explicam *por quê* as decisões foram tomadas, não apenas *o quê* o código faz:

```python
# Multiplica o subtotal pela alíquota global (10%) definida no topo
# Exemplo: Se subtotal é 100, resultado é 10
return subtotal * TAX_RATE
```

### Type Hints

Todos os parâmetros e retornos possuem anotações de tipo:

```python
def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    ...
```

---

## 🎓 Boas Práticas Implementadas

### ✅ Clean Code
- Nomes de variáveis descritivos
- Funções com responsabilidade única
- Evitar números mágicos com constantes

### ✅ Validação Defensiva
- Type checking com `isinstance()`
- Try-except para entradas inválidas
- Limites de validação (ex: números ≤ 1 não são primos)

### ✅ Documentação Completa
- Docstrings em estilo Google
- Comentários inline significativos
- Exemplos de uso para cada função

### ✅ Performance
- Algoritmo O(√n) para verificação de primos
- Funções nativas (`sum()`, `max()`, `min()`) vs. loops manuais
- List comprehension para operações eficientes

---

## 📖 Arquivos de Explicação

Este repositório também contém arquivos markdown detalhados:

- **`explicacao_num_primo.md`**: Análise linha a linha do algoritmo de primos com técnicas de Clean Code
- **`explicacao_refatoracao.md`**: Documentação completa da refatoração com antes/depois
- **`explicacao_debug.md`**: Explicação detalhada das correções e princípios aplicados

Recomenda-se ler estes arquivos para maior compreensão das práticas aplicadas.

---

## ✨ Como Usar GitHub Copilot com Este Projeto

### Solicitações Recomendadas:

1. **Para docstrings:**
   ```
   "Gere uma docstring no estilo Google para esta função, em português"
   ```

2. **Para comentários:**
   ```
   "Adicione comentários inline explicando as decisões de lógica, sem comentar linhas óbvias"
   ```

3. **Para geração de testes:**
   ```
   "Gere testes unitários para esta função usando pytest"
   ```

4. **Para melhorias:**
   ```
   "Sugira melhorias de performance para este código"
   ```

---

## 🤝 Contribuição

Este é um repositório educacional. Sugestões de melhorias são bem-vindas!

---

## 📝 Licença

Código desenvolvido para fins educacionais.

---

## 👨‍💼 Autor

Desenvolvido como prática de **Documentação de Software com GitHub Copilot** — Aula 06

**Data:** Maio de 2026

---

## 📞 Suporte

Para dúvidas sobre o código ou documentação, consulte os arquivos `.md` inclusos ou revisite os comentários inline nos scripts Python.

