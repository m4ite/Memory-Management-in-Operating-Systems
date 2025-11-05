# Demonstração do Garbage Collector em Python
---

## 📋 Descrição

Este projeto tem como objetivo **demonstrar o funcionamento do gerenciamento de memória no Python**, explorando conceitos fundamentais como:

- **Contagem de referências (Reference Counting)**
- **Coleta geracional (Garbage Collection)**
- **Ciclos de referência**
- **Liberação de memória em massa**

O código cria objetos grandes em memória e mostra **como e quando o Python libera esses objetos**, com mensagens automáticas que indicam a criação e destruição de instâncias.

---

## ⚙️ Conteúdo

O arquivo principal do projeto está dividido em três seções independentes, que podem ser ativadas e testadas separadamente:
### 1️⃣ Contagem de Referências
Demonstra o mecanismo básico de **referência e destruição automática** de objetos.

- Cria um objeto e exibe sua contagem de referências.
- Adiciona e remove referências adicionais.
- Mostra a destruição automática quando o contador chega a zero.


### 2️⃣ Referência Circular (Coleta Geracional)
Mostra como o Python trata ciclos de referência, nos quais objetos se referenciam mutuamente.

- Cria dois objetos que apontam um para o outro.
- Remove as referências externas, mas o ciclo interno impede a liberação imediata.
- Usa gc.collect() para forçar a coleta e liberar memória.

### 3️⃣ Objetos Não Referenciados em Massa
Cria vários objetos grandes armazenados em uma lista e, depois, remove todos de uma vez.

- Simula a criação em massa de dados.
- Mostra o comportamento do coletor ao liberar vários objetos simultaneamente.
- Exibe estatísticas de coleta por geração.

---

## ⚙️ Execução

💡 Ative cada bloco de teste descomentando a seção desejada no código.


