# Pesquisa binária

É uma técnica eficaz para encontrar elementos em listas ordenadas e é amplamente utilizada em algoritmos e estruturas de dados para otimizar as operações de busca. A ideia básica por trás desse algoritmo é reduzir continuamente a quantidade de dados a serem analisados pela metade, aproveitando a propriedade ordenada da lista.

Aqui estão os passos detalhados do algoritmo de pesquisa binária:

1. Inicialização:

- A pesquisa binária começa com uma lista ordenada de maneira ascendente ou descendente para que o algoritmo funcione corretamente.

2. Determinar o Intervalo de Busca:

- Inicialmente, considere a lista inteira como o intervalo de busca.

3. Calcular o Ponto Médio:

- Encontre o ponto médio do intervalo de busca. Isso pode ser feito calculando o índice médio da lista. Se o índice médio não for um número inteiro, você pode arredondar para cima ou para baixo.

4. Comparar o Elemento no Ponto Médio:

- Compare o elemento no ponto médio com o elemento que está sendo buscado.
    - Se o elemento no ponto médio for igual ao elemento procurado, a busca é concluída, e a posição do elemento é retornada.
    - Se o elemento no ponto médio for menor que o elemento procurado, então o elemento procurado deve estar à direita do ponto médio.
    - Se o elemento no ponto médio for maior que o elemento procurado, então o elemento procurado deve estar à esquerda do ponto médio.

5. Atualizar o Intervalo de Busca:

- Com base na comparação, atualize o intervalo de busca para a metade esquerda ou direita, excluindo a metade onde o elemento procurado não pode estar.
    - Se o elemento procurado estiver à direita, atualize o intervalo para a metade direita da lista.
    - Se o elemento procurado estiver à esquerda, atualize o intervalo para a metade esquerda da lista.

6. Repetir:

- Repita os passos 3 a 5 até encontrar o elemento ou até que o intervalo de busca seja vazio. Se o intervalo de busca for vazio e o elemento não for encontrado, retorne None.

7. Complexidade:

- A pesquisa binária tem uma complexidade de tempo O(log n), onde n é o número de elementos na lista. Isso torna a pesquisa binária significativamente mais eficiente do que a busca linear, especialmente para listas grandes.

### Código:

```python
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2  # Usando divisão inteira
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9, 11, 13]

print(pesquisa_binaria(minha_lista, 3))   # Saída: 1
print(pesquisa_binaria(minha_lista, -1))  # Saída: None
```