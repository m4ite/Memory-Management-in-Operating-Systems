import sys
import gc

class Objeto:
    def __init__(self,nome, tamanho_mb):
        self.nome = nome
        self.dados = bytearray(tamanho_mb * 1024 * 1024) # Aloca 'tamanho_mb' de bytes
        self.ref = None  # referência a outro objeto
        self.id = id(self) # endereço de memória do objeto
        print(f"Objeto criado com {tamanho_mb} MB. ID (endereço): {self.id}")

    def __del__(self):
        # método chamado quando o objeto é destruído pelo coletor de lixo
        print(f"Objeto com ID {self.id} destruído.")
        
        
        
gc.enable()  # Habilita o garbage collector

#------ COLETA POR CONTAGEM DE REFERÊNCIAS ------
# O Python libera automaticamente objetos quando sua contagem de referências chega a zero

# obj1 = Objeto ("Objeto 1", 5)
# print(f"Contagem de referências para obj1: {sys.getrefcount(obj1)} \n")

# ref_extra = obj1 # variável apontando para o mesmo objeto
# print(f"Após criar ref_extra, contagem: {sys.getrefcount(obj1)}\n")

# Removendo referências
# del ref_extra
# print("Referência extra removida.")
# print(f"Contagem de referências atual: {sys.getrefcount(obj1)}\n")

# Removendo a última referência, o objeto deve ser destruído automaticamente
# del obj1
# print("obj1 removido. O coletor deve liberar a memória imediatamente.\n")



#------ REFERÊNCIA CIRCULAR (COLETA GERACIONAL) ------

# Cria dois objetos grandes
# obj1 = Objeto("obj1", 5)
# obj2 = Objeto("obj2", 5)

# Cria referência circular: obj1 → obj2 → obj1
# obj1.ref = obj2
# obj2.ref = obj1

# Exibe contagem de referências
# print(f"Referências de obj1: {sys.getrefcount(obj1)}")
# print(f"Referências de obj2: {sys.getrefcount(obj2)}")

# Removendo referências externas — mas os objetos ainda se referem entre si
# del obj1
# del obj2
# print("Referências externas removidas. Os objetos ainda estão em ciclo interno.")

# Forçando a coleta de lixo
# print("\nForçando execução do coletor de lixo...")
# coletados = gc.collect()
# print(f"Objetos coletados: {coletados}")
# print("Após a coleta, o ciclo é resolvido.\n")




#------ OBJETOS NÃO REFERENCIADOS EM MASSA ------
objetos = [Objeto(f"obj_{i}", 2) for i in range(3)]
# Cada item da lista mantém uma referência.
print(f"Referência total da lista: {sys.getrefcount(objetos)}")

# Removendo toda a lista de uma vez
del objetos
print("Lista de objetos removida. Coletor deve liberar todos os objetos.")

# # Forçando o GC para limpar resíduos rapidamente
gc.collect()

print("\nEstatísticas do GC:")
for i, geracao in enumerate(gc.get_stats()):
    print(f"Geração {i}: {geracao}")

