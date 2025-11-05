# Comparação de Desempenho: Stack vs Heap em C
---

## 📋 Descrição

Este projeto tem como objetivo **comparar o desempenho entre alocação de memória na Stack (pilha)** e **no Heap (memória dinâmica)** em linguagem C.  
O código mede o tempo necessário para realizar **1 milhão de operações** de alocação em cada tipo de memória, repetindo o processo várias vezes para obter uma **média confiável** dos resultados.

A partir dos tempos médios obtidos, é exibida uma **comparação percentual** mostrando quanto a alocação no Heap é mais lenta que na Stack.

---

## ⚙️ Funcionalidades

- Mede o tempo de execução de operações na **Stack** (variáveis locais automáticas);
- Mede o tempo de execução de operações no **Heap** (alocação dinâmica com `malloc` e `free`);
- Calcula o **tempo médio** após múltiplas execuções;
- Exibe uma **comparação percentual** entre os dois métodos;
- Inclui comentários explicativos sobre as diferenças entre os tipos de memória.


---

## 🧠 Análise dos Resultados

A STACK é muito mais rápida, pois a alocação e liberação são automáticas e previsíveis — basta mover o ponteiro da pilha.

A HEAP é muito mais lenta, pois envolve chamadas a funções do sistema operacional (malloc e free) e controle de blocos de memória.

A diferença pode variar conforme:

- A carga do processador no momento da execução;

- Estratégias de otimização do compilador;

- Gerenciamento de memória do sistema operacional.

Em geral, a alocação no Heap pode ser de dezenas a centenas de vezes mais lenta do que na Stack.


