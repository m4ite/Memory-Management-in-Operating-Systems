# 🧠Memory-Management-in-Operating-Systems


## 👥 Integrantes do Grupo

| Nome Completo | RA |
|----------------|-----|
| Maite Feld | 24038305-2 |
| Arthur Afonso Pereira Mistura | 24042130 2 |
| Henrique Chittolina Silva | 241514342 |
| Eduardo Vinicius Viante Vieira | 24136242-2 |
| Brendon Cesario | 24250743-2 |
| Lucas Crais | 24151355-2 |
| Pedro Leandro Hack Ruthes | 24170562-2 |
| Bruno Danker | 24229576-2 |


---

## 🎯 Objetivo Geral

Este trabalho tem como objetivo **avaliar a compreensão dos conceitos de gerenciamento de memória em sistemas operacionais**, explorando desde os mecanismos básicos de alocação até estratégias de coleta de lixo e substituição de páginas.

Os exercícios combinam **parte teórica** e **parte prática**, exigindo tanto explicação conceitual quanto implementação funcional nas linguagens **C, Python ou Java**.

---

## 🧩 Estrutura do Trabalho

### **Questão 1 — Alocação Estática vs. Dinâmica (C)**
Demonstra a diferença entre alocação estática e dinâmica de memória.  
Implementa um programa em C que cria arrays estáticos e dinâmicos, exibe seus endereços e compara as regiões de memória.  
Inclui verificação de sucesso na alocação e liberação com `free()`.

---

### **Questão 2 — Simulação de Fragmentação de Memória (Python)**
Simula um **gerenciador de memória com partições fixas**, aplicando o algoritmo **First-Fit**.  
Calcula fragmentação interna após cada alocação e demonstra como partições podem ficar inutilizadas.  
Enfatiza o impacto da **fragmentação interna e externa** no uso da memória.

---

### **Questão 3 — Algoritmo de Substituição de Página FIFO (Java)**
Implementa o algoritmo **FIFO (First-In, First-Out)** para substituição de páginas na memória.  
Recebe uma sequência de referências e o número de quadros, exibindo **faltas de página**, **page hits** e **taxa de faltas**.  
Utiliza uma estrutura de dados em fila (Queue) para simular a política de substituição.

---

### **Questão 4 — Garbage Collection em Python**
Explora o **mecanismo de coleta de lixo do Python**, demonstrando três cenários:
1. Coleta por contagem de referências;  
2. Referência circular entre objetos;  
3. Liberação em massa via coletor geracional.  
Inclui o uso dos módulos `gc` e `sys` para exibir **contagem de referências** e **estatísticas de coleta**.  
Código amplamente comentado para fins didáticos.

---

### **Questão 5 — Comparação de Desempenho de Alocação (Python/C/Java)**
Compara o tempo de execução entre **alocação na pilha (stack)** e **alocação no heap**, demonstrando por que a pilha é mais rápida.  
O programa mede o tempo médio de criação e destruição de 1.000.000 de variáveis/objetos e calcula a diferença percentual de desempenho.

---

