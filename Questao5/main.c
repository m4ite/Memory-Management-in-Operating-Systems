
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 1000000 // número de testes
#define REP 5    // Quantas vezes cada teste será repetido


// Função que usa alocação na pilha (stack)
void teste_stack() {
    for (int i = 0; i < N; i++) {
        int a = i; // variável local (alocada na pilha)
        a += 1;
    }
}

// Função que usa alocação no heap (dinâmica)
void teste_heap() {
    
    // Cada iteração aloca e libera memória com malloc/free.
    // Isso é mais custoso pois envolve o gerenciador de heap.
    for (int i = 0; i < N; i++) { 
        int *a = (int*)malloc(sizeof(int)); // aloca no heap
        if (a == NULL) {
            printf("Erro de alocacao!\n");
            exit(1);
        }
        *a = i; // usa o espaço alocado
        free(a); // libera memória
    }
}

int main() {
    clock_t inicio, fim;
    double tempo_stack = 0, tempo_heap = 0;




    // Teste stack
     for (int r = 0; r < REP; r++) {
        inicio = clock();
        teste_stack();
        fim = clock();
        double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        tempo_stack += tempo;
        printf("Execucao %d (STACK): %.6f segundos\n", r + 1, tempo);
    }

    double media_stack = tempo_stack / REP;
    printf("\nTempo medio STACK: %.6f segundos\n\n", media_stack);

    // Teste heap
    for (int r = 0; r < REP; r++) {
        inicio = clock();
        teste_heap();
        fim = clock();
        double tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        tempo_heap += tempo;
        printf("Execucao %d (HEAP): %.6f segundos\n", r + 1, tempo);
    }

    double media_heap = tempo_heap / REP;
    printf("\nTempo medio HEAP: %.6f segundos\n", media_heap);

    // Comparação em percentual  %
    double diferenca = ((media_heap - media_stack) / media_stack) * 100.0;
    printf("A alocacao no HEAP foi aproximadamente %.2f%% mais lenta.\n", diferenca);

    return 0;
}


  // ------------------------------------------------------------
    // Analise dos resultados:
    // ------------------------------------------------------------
    // A alocação na STACK é mais rápida, pois o espaço é alocado de 
    // forma direta e previsível, bastando mover o ponteiroda pilha.
    // Não há necessidade de solicitar espaço ao sistema operacional
    //
    // A alocação no HEAP envolve chamadas a funções de gerenciamento
    // de memória (malloc e free), deixando o processo mais complexo e lento
    //
    // Pequenas variações podem ocorrer entre execuções devido a:
    //  - Carga do processador no momento da execução
    //  - Estratégias internas de otimização do compilador
    //  - Sistema operacional gerenciando a memória
    // ------------------------------------------------------------