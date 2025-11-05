#include <stdio.h>
#include <stdlib.h>

int main() {
    // 1. Declaração do array estático
    int array_estatico[5];
    for (int i = 0; i < 5; i++) {
        array_estatico[i] = i + 1; // preenchendo com valores de 1 a 5
    }

    // 2. Alocação dinâmica de um array de 10 inteiros
    int *array_dinamico = (int *) malloc(10 * sizeof(int));

    // Verifica se a alocação foi bem-sucedida
    if (array_dinamico == NULL) {
        printf("Erro: não foi possível alocar memória dinamicamente.\n");
        return 1; // encerra o programa
    }

    // 3. Preenche o array dinâmico com valores de 10 a 19
    for (int i = 0; i < 10; i++) {
        array_dinamico[i] = 10 + i;
    }

    // 4. Imprime os valores e endereços de ambos os arrays
    printf("\n=== Array Estático ===\n");
    for (int i = 0; i < 5; i++) {
        printf("Valor: %d | Endereço: %p\n", array_estatico[i], (void*)&array_estatico[i]);
    }

    printf("\n=== Array Dinâmico ===\n");
    for (int i = 0; i < 10; i++) {
        printf("Valor: %d | Endereço: %p\n", array_dinamico[i], (void*)&array_dinamico[i]);
    }

    // 5. Mostra a diferença entre os endereços iniciais
    // (para demonstrar que estão em áreas diferentes da memória)
    printf("\nEndereço inicial do array estático: %p\n", (void*)array_estatico);
    printf("Endereço inicial do array dinâmico: %p\n", (void*)array_dinamico);
    printf("Diferença entre os endereços (em bytes): %ld\n",
           (long)((char*)array_dinamico - (char*)array_estatico));

    // 6. Libera a memória alocada dinamicamente
    free(array_dinamico);
    printf("\nMemória dinâmica liberada com sucesso.\n");
    return 0;
}
