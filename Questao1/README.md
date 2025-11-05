# Comparação de Memória Estática e Dinâmica em C
---

## 📋 Descrição

Este projeto demonstra a diferença entre alocação estática e alocação dinâmica de memória em linguagem C.
O programa cria dois arrays:

Um array estático de 5 inteiros (valores de 1 a 5)

Um array dinâmico de 10 inteiros (valores de 10 a 19)

Em seguida, o programa imprime os endereços de memória de ambos os arrays, calcula a diferença entre os endereços, e mostra que estão armazenados em áreas distintas da memória (Stack vs Heap).
Por fim, a memória alocada dinamicamente é liberada corretamente.

---

## ⚙️ Funcionalidades

Declaração de array estático e preenchimento automático

Alocação dinâmica com malloc() e verificação de sucesso

Impressão de valores e endereços de memória dos dois arrays

Cálculo da diferença entre endereços

Liberação segura da memória dinâmica com free()


---

## ⚠️ Observações

Os endereços de memória variam a cada execução — o importante é perceber que estão em regiões distintas.

Sempre verifique se malloc() retornou um ponteiro válido antes de usar a memória alocada.

Liberar a memória com free() evita vazamentos e comportamento indefinido.


