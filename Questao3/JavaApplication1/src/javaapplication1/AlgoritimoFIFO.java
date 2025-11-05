import java.util.*;

public class AlgoritimoFIFO{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // PARTE 1 - RECEBER ENTRADAS
        // receber como entrada, que seria o espaço disponivel na memoria, tipo 2, 1,3 seria o espaço disponivel
        System.out.print("Número de frames disponíveis na memória: ");
        int framesNum = sc.nextInt();

        System.out.println("Sequência de referências a páginas (ex: 7 0 1 2 0 3 0 4 2 3 0 3 2): ");
        sc.nextLine();
        String line = sc.nextLine();
        
        // salva os valores digitados no array
        String[] pagesStr = line.split(" ");
        int[] pages = new int[pagesStr.length];
        for (int i = 0; i < pagesStr.length; i++) {
            pages[i] = Integer.parseInt(pagesStr[i]);
        }
        

        // simular o algoritmo FIFO
        Queue<Integer> frames = new LinkedList<>();
        
        // SET - busca rápida (verificar se uma página já está em memória)
        Set<Integer> pagesSet = new HashSet<>(); 
        int pageFaults = 0;

        for (int page : pages) {
            boolean pageHit = pagesSet.contains(page); // Verifica se a página já está em memória
            Integer removedPage = null;

            if (!pageHit) {
                // page fault ocorreu
                pageFaults++;
                
                // Se a memória estiver cheia, remove a mais antiga
                if (frames.size() == framesNum) {
                    removedPage = frames.poll(); // remove o primeiro elemento da fila
                    pagesSet.remove(removedPage);  // remove o elemento do conjunto de busca
                }
                frames.offer(page);
                pagesSet.add(page);
            }

            // exibir estado após cada referência
            System.out.print("Referência: " + page + " | Frames: " + frames);
            if (pageHit) {
                // página já na memória
                System.out.println(" | Page Hit");
            } else {
            	// Página nova ou substituída
            	if (removedPage != null) {
                    System.out.print(" | Page Fault (substituiu " + removedPage + ")");
                } else {
                    System.out.print(" | Page Fault");
                }
                System.out.print(" | Total Faults: " + pageFaults);
            }
            
            System.out.println();

        }

        //exibindo as estatisticas
        System.out.println("Número total de faltas de página (page faults): " + pageFaults);

        sc.close();
    }
}
