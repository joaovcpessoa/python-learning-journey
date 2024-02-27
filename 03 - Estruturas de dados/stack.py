# Em Python, você pode implementar uma pilha usando uma lista. 
# Uma pilha segue a regra "last-in, first-out" (LIFO), 
# o que significa que o último elemento adicionado é o primeiro a ser removido.
# Aqui está um exemplo simples de como você pode criar e usar uma pilha em Python:

# Bom para recordar:
# A função __init__() é chamada automaticamente sempre que a classe está sendo usada para criar um novo objeto.
# O parâmetro self é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe.

class Pilha:
    def __init__(self):
        # O construtor da classe inicializa uma lista vazia para armazenar os elementos da pilha.
        self.items = []

    def vazia(self):
        # Retorna True se a pilha estiver vazia, caso contrário, retorna False.
        return len(self.items) == 0

    def empilhar(self, item):
        # Adiciona um elemento ao topo da pilha.
        self.items.append(item)

    def desempilhar(self):
        # Remove e retorna o elemento no topo da pilha.
        if not self.vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        # Retorna o elemento no topo da pilha sem removê-lo.
        if not self.vazia():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        # Retorna o número de elementos na pilha.
        return len(self.items)

# Exemplo de uso da pilha
pilha_exemplo = Pilha()

# Adiciona elementos à pilha
pilha_exemplo.empilhar(1)
pilha_exemplo.empilhar(2)
pilha_exemplo.empilhar(3)

# Exibe informações sobre a pilha
print("Topo da pilha:", pilha_exemplo.topo())        # Saída: 3
print("Tamanho da pilha:", pilha_exemplo.tamanho())  # Saída: 3

# Remove um elemento da pilha
elemento_removido = pilha_exemplo.desempilhar()
print("Elemento removido:", elemento_removido)                  # Saída: 3
print("Topo da pilha apos desempilhar:", pilha_exemplo.topo())  # Saída: 2

# Neste exemplo, a classe Pilha possui métodos para:
# empilhar (empilhar), 
# desempilhar (desempilhar),
# verificar se está vazia (vazia), 
# obter o topo da pilha (topo) e 
# obter o tamanho da pilha (tamanho). 
# Certifique-se de lidar com casos em que a pilha está vazia ao chamar métodos como desempilhar ou topo.