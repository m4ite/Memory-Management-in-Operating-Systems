# Simulação de Fragmentação de Memória
---

## 📋 Descrição

Este projeto implementa um **simulador de gerenciamento de memória com partições fixas**, utilizando o **algoritmo de alocação First-Fit**.  
O objetivo é demonstrar, de forma prática e didática, como o sistema operacional gerencia a alocação e liberação de processos em partições de memória.

---

## ⚙️ Funcionalidades

✅ **Alocação de processos** com o algoritmo **First-Fit**  
✅ **Liberação de partições** ocupadas por processos  
✅ **Cálculo de fragmentação interna total**  
✅ **Visualização detalhada** do estado da memória  
✅ Dois modos de execução:
- **Modo Automático:** executa uma sequência pré-definida de operações  
- **Modo Manual:** permite que o usuário interaja com o simulador via comandos  


---

##  🧩 Estrutura da Memória

O sistema possui **5 partições fixas**, pré-definidas no código:

| ID | Tamanho | Estado Inicial |
|----|----------|----------------|
| 1  | 100      | Livre          |
| 2  | 150      | Livre          |
| 3  | 200      | Livre          |
| 4  | 250      | Livre          |
| 5  | 300      | Livre          |

A memória total é de **1000 unidades**.


