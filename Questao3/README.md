# Simulador do Algoritmo de Substituição de Página FIFO (Java)
Este projeto implementa uma **simulação do algoritmo de substituição de páginas FIFO (First In, First Out)** em Java.  
O programa permite que o usuário informe a quantidade de **frames disponíveis na memória** e uma **sequência de referências a páginas**, mostrando passo a passo como as páginas são carregadas, substituídas e contabilizando as **faltas de página (page faults)**.

---

## 📋 Funcionalidades

- Recebe como entrada:
  - Número de **frames disponíveis** na memória.
  - Sequência de **referências a páginas** (ex: `7 0 1 2 0 3 0 4 2 3 0 3 2`).
- Simula o comportamento do **algoritmo FIFO**:
  - Carrega páginas conforme são acessadas.
  - Substitui sempre a **página mais antiga** quando não há espaço livre.
- Exibe:
  - O **estado atual da memória (frames)** após cada referência.
  - Se ocorreu **Page Fault** ou **Page Hit**.
  - Qual página foi substituída (quando aplicável).
  - O **total de faltas de página acumuladas**.
- Calcula e mostra:
  - O **número total** de faltas de página.
  - A **taxa de faltas de página**, em relação ao total de referências.


---

## 📚 Conceitos importantes

- Page Fault: ocorre quando a página solicitada não está na memória e precisa ser carregada.

- Page Hit: ocorre quando a página já está nos frames, evitando substituição.

- FIFO: substitui a página mais antiga entre as que estão carregadas.
ferença percentual de desempenho.

---

