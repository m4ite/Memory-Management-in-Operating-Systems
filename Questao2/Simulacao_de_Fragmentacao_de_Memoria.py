

class GerenciadorMemoria:
    def __init__(self):
        # Lista de partições
        self.particoes = [
            {"id": 1, "tamanho": 100, "ocupada_por": None, "frag_interna": 0},
            {"id": 2, "tamanho": 150, "ocupada_por": None, "frag_interna": 0},
            {"id": 3, "tamanho": 200, "ocupada_por": None, "frag_interna": 0},
            {"id": 4, "tamanho": 250, "ocupada_por": None, "frag_interna": 0},
            {"id": 5, "tamanho": 300, "ocupada_por": None, "frag_interna": 0},
        ]
        self.memoria_total = sum(p["tamanho"] for p in self.particoes)
        print(f"Gerenciador iniciado. Memoria total: {self.memoria_total} unidades.")

    def alocar_processo(self, nome, tamanho):
        """
        Aloca um processo usando o algoritmo First-Fit.
        Procura a primeira particao livre que seja grande o suficiente.
        """
        print(f"\nTentando alocar {nome} (Tamanho: {tamanho})")
        
        # 1. Verifica se o processo já existe
        for p in self.particoes:
            if p["ocupada_por"] == nome:
                print(f"Falha: O processo '{nome}' já está alocado na partição {p['id']}.")
                return False

        # 2. Verifica se o processo é maior que a maior partição LIVRE
        maior_particao_livre = 0
        for p in self.particoes:
             if p["ocupada_por"] is None and p["tamanho"] > maior_particao_livre:
                 maior_particao_livre = p["tamanho"]
                 
        if tamanho > maior_particao_livre:
            if maior_particao_livre == 0:
                 print(f"Falha: Não há partições livres no momento.")
            else:
                print(
                    f"Falha: Processo '{nome}' ({tamanho}) é maior que a maior partição LIVRE ({maior_particao_livre})."
                )
            return False

        # 3. Algoritmo First-Fit
        for particao in self.particoes:
            if particao["ocupada_por"] is None and particao["tamanho"] >= tamanho:
                particao["ocupada_por"] = nome
                fragmentacao = particao["tamanho"] - tamanho
                particao["frag_interna"] = fragmentacao

                print(
                    f"Sucesso: Processo {nome} alocado na partição {particao['id']} (Tamanho: {particao['tamanho']})"
                )
                print(f"Fragmentação Interna gerada: {fragmentacao} unidades")

                self.exibir_memoria()  # Mostra o estado da memória após alocar
                return True

        print(
            f"Falha: Não há partição livre ou grande o suficiente para {nome} (Tamanho: {tamanho})"
        )
        return False

    def liberar_processo(self, nome):
        """
        Libera a partição ocupada por um processo específico.
        """
        print(f"\nTentando liberar processo {nome}")
        for particao in self.particoes:
            if particao["ocupada_por"] == nome:
                particao["ocupada_por"] = None
                particao["frag_interna"] = 0
                print(f"Sucesso: Processo {nome} liberado da Partição {particao['id']}")
                self.exibir_memoria()  # Mostra o estado após liberar
                return True

        print(f"Falha: Processo {nome} não encontrado na memória.")
        return False

    def exibir_memoria(self):
        """
        Mostra o estado atual de todas as partições de memória
        """
        print("\n--- ESTADO ATUAL DA MEMÓRIA ---")
        print("ID | Tamanho | Ocupada Por | Frag. Interna")
        print("---|---------|-------------|---------------")
        for p in self.particoes:
            status = p["ocupada_por"] if p["ocupada_por"] else "LIVRE"
            print(f"{p['id']:<2} | {p['tamanho']:<7} | {status:<11} | {p['frag_interna']}")
        print("-------------------------------------------")

    def calcular_frag_interna_total(self):
        """
        Calcula e exibe a fragmentação interna total somando a de todas as partições.
        """
        total_frag = sum(p["frag_interna"] for p in self.particoes)
        print(f"\nFragmentação Interna Total: {total_frag} unidades")
        return total_frag


def exibir_ajuda():
    """Mostra o menu de ajuda para o modo manual."""
    print("\n--------------- Comandos Disponíveis -----------------------------")
    print("  alocar nome tamanho - Aloca um processo (ex: alocar p1 90)")
    print("  liberar nome - Libera um processo (ex: liberar p1)")
    print("  exibir - Mostra o estado atual da memória")
    print("  frag - Calcula a fragmentação interna total")
    print("  ajuda - Mostra esta mensagem")
    print("  sair - Encerra o programa")
    print("-------------------------------------------------------------------")

# --- MODO 1: AUTOMÁTICO ---
def modo_automatico():
    print("\n--- MODO AUTOMÁTICO SELECIONADO ---")
    gm = GerenciadorMemoria() # Cria um novo gerenciador
    gm.exibir_memoria()
    
    
    gm.alocar_processo("P1", 90)
    gm.alocar_processo("P2", 140)
    gm.alocar_processo("P3", 180)
    gm.liberar_processo("P2")
    gm.alocar_processo("P4", 100)
    gm.alocar_processo("P5", 350)  # falhar
    gm.calcular_frag_interna_total()
    
    print("\n--- FIM DO MODO AUTOMÁTICO ---")

# --- MODO 2: MANUAL  ---
def modo_manual():
    print("\n--- MODO MANUAL SELECIONADO ---")
    gm = GerenciadorMemoria() # Cria um novo gerenciador
    gm.exibir_memoria()
    exibir_ajuda() # Mostra a ajuda no início
    
    
    while True:
        entrada = input("\nComando > ").strip().lower()
        if not entrada:
            continue

        partes = entrada.split()
        comando = partes[0]

        if comando == "sair":
            print("Encerrando o simulador...")
            break

        elif comando == "ajuda":
            exibir_ajuda()

        elif comando == "exibir":
            gm.exibir_memoria()

        elif comando == "frag":
            gm.calcular_frag_interna_total()

        elif comando == "alocar":
            if len(partes) == 3:
                nome = partes[1].upper() # Converte nome para maiúsculo
                try:
                    tamanho = int(partes[2])
                    gm.alocar_processo(nome, tamanho)
                except ValueError:
                    print(f"Erro: O tamanho '{partes[2]}' deve ser um número inteiro.")
            else:
                print("Erro: Uso incorreto. Tente: alocar nome tamanho")

        elif comando == "liberar":
            if len(partes) == 2:
                nome = partes[1].upper() # Converte nome para maiúsculo
                gm.liberar_processo(nome)
            else:
                print("Erro: Uso incorreto. Tente: liberar nome")

        else:
            print(f"Erro: Comando '{comando}' desconhecido. Digite 'ajuda' para ver as opções.")


# --- MENU PRINCIPAL ---
if __name__ == "__main__":
    while True:
        print("\n--- SIMULADOR DE GERENCIAMENTO DE MEMÓRIA ---")
        print("  Escolha o modo de execução:")
        print()
        print("  1: Modo Automático (Executa um teste pré-definido)")
        print("  2: Modo Manual (Interativo, você digita os comandos)")
        print("  sair: Encerrar o programa")
        print()

        escolha = input("Digite 1, 2 ou 'sair': ").strip().lower()

        if escolha == "1":
            modo_automatico()
            break # Termina o programa após rodar o modo automático
        elif escolha == "2":
            modo_manual()
            break # Termina o programa após o usuário digitar 'sair' no modo manual
        elif escolha == "sair":
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Tente novamente.")