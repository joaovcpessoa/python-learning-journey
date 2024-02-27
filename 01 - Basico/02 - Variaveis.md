# VARIÁVEIS

Variáveis são contêineres para armazenar valores de dados.

## Criação de variáveis

Python não tem comando para declarar uma variável.

Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.

```python
x = 5
y = "João"
print(x)
print(y)

#Saída:
"""
5
João
"""
```

As variáveis não precisam ser declaradas com nenhum *tipo* específico e podem até mesmo mudar de tipo após terem sido definidas.

```python
x = 4      # x é do tipo int
x = "Solo" # x agora é do tipo str
print(x)

#Saída:
"""
Solo
"""
```

## Casting

Se você deseja especificar o tipo de dados de uma variável, isso pode ser feito com o casting.

```python
x = str(3)    # x será '3'
y = int(3)    # y será 3
z = float(3)  # z será 3.0
```

## Obtenha o tipo da variável

Você pode obter o tipo de dados de uma variável com a `type()`função.

```python
x = 5
y = "João"
print(type(x))
print(type(y))

#Saída:
"""
<class 'int'>
<class 'str'>
"""
```

## Aspas simples ou duplas?

Variáveis de string podem ser declaradas usando aspas simples ou duplas, desde que sejam pares combinados. Se abrir aspas duplas, deve fechar com aspas duplas, assim também para aspas simples.

```python
x = "João"
# é o mesmo que
x = 'João'
```

## Maiúsculas e Minúsculas

Os nomes das variáveis diferenciam maiúsculas de minúsculas.

É o que chamamos de *case-sensitive.*

```python
a = 4
A = "Solo"
#A não substituirá a, são variáveis diferentes
```

## Nomes de Variáveis

Uma variável pode ter um nome curto (como xey) ou um nome mais descritivo (idade, carname, total_volume). Regras para variáveis Python:

- O nome de uma variável deve começar com uma letra ou o caractere de sublinhado
- O nome de uma variável não pode começar com um número
- Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (A-z, 0-9 e _)
- Os nomes das variáveis diferenciam maiúsculas de minúsculas
(idade, Idade e IDADE são três variáveis diferentes)

```python
myvar = "João"
my_var = "João"
_my_var = "João"
myVar = "João"
MYVAR = "João"
myvar2 = "João"

#Nomes de variáveis ilegais:
2myvar = "João"
my-var = "João"
my var = "João"
```

## Nomes de variáveis com várias palavras

Nomes de variáveis com mais de uma palavra podem ser difíceis de ler.

Existem várias técnicas que você pode usar para torná-los mais legíveis:

## Camel Case

Cada palavra, exceto a primeira, começa com uma letra maiúscula:

```python
myVariableName = "João"
```

## Pascal Case

Cada palavra começa com uma letra maiúscula:

```python
MyVariableName = "João"
```

## Snake Case

Cada palavra é separada por um caractere de sublinhado:

```python
my_variable_name = "João"
```

## Muitos Valores para Variáveis Múltiplas

Python permite que você atribua valores a várias variáveis em uma linha:

### Exemplo:

```python
x, y, z = "Laranja", "Banana", "Cereja"
print(x)
print(y)
print(z)

#Saída:
"""
Laranja
Banana
Cereja
"""
```

💡**Nota:** Certifique-se de que o número de variáveis corresponda ao número de valores, ou então você obterá um erro.

## Um valor para múltiplas variáveis

E você pode atribuir o *mesmo* valor a várias variáveis em uma linha.

```python
x = y = z = "Laranja"
print(x)
print(y)
print(z)

#Saída:
"""
Laranja
Laranja
Laranja
"""
```

## Descompacte uma coleção

Se você tem uma coleção de valores em uma list, tuple, etc. Python permite que você extraia os valores em variáveis. Isso é chamado de *descompactação* .

```python
frutas = ["maçã", "banana", "cereja"]
x, y, z = frutas
print(x)
print(y)
print(z)

#Saída:
"""
maçã
banana
cereja
"""
```

## Variáveis de saída

A instrução `print` costuma ser usada para gerar variáveis, já quando queremos combinar uma variável do tipo texto e do tipo numérico, usamos o operador aritmético `+`:

```python
x = "maravilhoso"
print("Python é " + x)

#Você também pode usar o +caractere para adicionar uma variável a outra variável:
x = "Python é"
y = "maravilhoso"
z =  x + y
print(z)

#Para números, o + funciona como um operador matemático:
x = 5
y = 10
print(x + y)

#Se você tentar combinar uma string e um número, o Python apresentará um erro:
x = 5
y = "João"
print(x + y)
```

## Variáveis globais

Variáveis que são criadas fora de uma função (como em todos os exemplos acima) são conhecidas como variáveis globais e podem ser usadas em qualquer parte do código, tanto dentro quanto fora das funções. No decorrer dos estudos você irá aprender sobre funções.

```python
x = "maravilhoso"
 def myfunc():
  print("Python é " + x)
   myfunc()
```

Se você criar uma variável com o mesmo nome dentro de uma função, essa variável será local e só pode ser usada dentro da função. A variável global com o mesmo nome permanecerá como era, global e com o valor original.

```python
x = "maravilhoso"
 def myfunc():
  x = "fantástico"
   print("Python é " + x)
    myfunc()
     print("Python é " + x)
```

## A palavra-chave global

Normalmente, quando você cria uma variável dentro de uma função, essa variável é local e só pode ser usada dentro dessa função.

Para criar uma variável global dentro de uma função, você pode usar a palavra - chave `global`.

```python
def myfunc():
 global x
  x = "fantástico"
   myfunc()
    print("Python é " + x)
```

**Nota:** Podemos usar a palavra-chave `global` se quisermos alterar uma variável global dentro de uma função.

```python
x = "maravilhoso"
 def myfunc():
  global x
   x = "fantástico"
    myfunc()
     print("Python é " + x)
```

# TIPOS DE DADOS

Na programação, o tipo de dados é um conceito importante.

Variáveis podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes.

Python tem os seguintes tipos de dados integrados por padrão, nestas categorias:

**Tipo de texto:** *str*

**Tipos numéricos:** *int, float, complex*

**Tipos de sequência:** *list, tuple, range*

**Tipo de mapeamento:** *dict*

**Tipos de conjuntos:** *set, frozenset*

**Tipo booleano:** *bool*

**Tipos binários:** *bytes, bytearray, memoryview*

## Obtendo o tipo de dados

Você pode obter o tipo de dados de qualquer objeto usando a função `type()`:

### Exemplo:

```python
x = 5
print(type(x))

#Saída:
"""
<class 'int'>
"""

```

## Definindo o tipo de dados

Em Python, o tipo de dados é definido quando você atribui um valor a uma variável.

```python
x = "Olá, Mundo"
print(x)         #exibe x:
print(type(x))   #exibe o tipo de dado de x:

#Saída:
"""
Olá, Mundo
<class 'str'>
"""
```

Você pode utilizar o código acima para verificar cada tipo de dados na tabela abaixo:

| Exemplo | Tipo de dado |
| --- | --- |
| x = "Olá, Mundo!" | str |
| x = 20 | int |
| x = 20.5 | float |
| x = 1j | complex |
| x = ["maçã", "banana", "cereja"] | list |
| x = ("maçã", "banana", "cereja") | tuple |
| x = range(6) | range |
| x = {"nome" : "João", "idade" : 21} | dict |
| x = {"maçã", "banana", "cereja"} | set |
| x = frozenset({"maçã", "banana", "cereja"}) | frozenset |
| x = True | bool |
| x = b"Olá" | bytes |
| x = bytearray(5) | bytearray |
| x = memoryview(bytes(5)) | memoryview |

## Definir o Tipo de Dado Específico

Se você deseja especificar o tipo de dados, pode usar as seguintes funções de construtor.

```python
x = str("Olá, Mundo") #note a sintaxe str antes do valor de x
print(x)
print(type(x))

#Saída:
"""
Olá, Mundo
<class 'str'>
"""
```

## Especifique um tipo de variável - CASTING

Pode haver momentos em que você deseja especificar um tipo em uma variável. Isso pode ser feito com casting. Python é uma linguagem orientada a objetos e, como tal, usa classes para definir tipos de dados, incluindo seus tipos primitivos.

A conversão em python é, portanto, feita usando funções construtoras:

- `int ()` - constrói um número inteiro a partir de um literal inteiro, um literal flutuante (removendo todos os decimais) ou um literal de string (desde que a string represente um número inteiro)
- `float ()` - constrói um número flutuante a partir de um literal inteiro, um literal flutuante ou um literal de string (desde que a string represente um flutuante ou um inteiro)
- `str ()` - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, literais inteiros e literais flutuantes

```python
#inteiros
x = int(1)       # x será 1
y = int(2.8)     # y será 2
z = int("3")     # z será 3
#ponto flutuante
x = float(1)     # x será 1.0
y = float(2.8)   # y será 2.8
z = float("3")   # z será 3.0
w = float("4.2") # w será 4.2
#strings
x = str("s1")    # x será 's1'
y = str(2)       # y será '2'
z = str(3.0)     # z será '3.0'
```

## Entrada de Dados

Python permite a entrada de dados.

O método é um pouco diferente no Python 3.6 e no Python 2.7.

Python 3.6 usa o método `input()`. Python 2.7 usa o método`raw_input()`.

O exemplo a seguir pede o nome de usuário e, quando você digita o nome de usuário, ele é impresso na tela:

### Python 3.6

```python
username = input("Enter username:")
 print("Username is: " + username)
```

### Python 2.7

```python
username = raw_input("Enter username:")
print("Username is: " + username)
```

Assim é possível solicitar a entrada de dados ao usuário para trabalhar com eles pelo código. Veremos exemplos que deixam bem claro o funcionamento dessa função.

Na versão atual do Python (3.10) segue com a sintaxe da versão 3.6.

### STRING

As strings em python são colocadas entre aspas simples ou aspas duplas.

Você pode exibir uma dado do tipo string com a função `print()`:

```python
print("Olá")
print('Olá')

#Saída:
"""
Olá
Olá
"""
```

## **Atribuir String a uma Variável**

A atribuição de uma string a uma variável é feita com o nome da variável seguido por um sinal de igual, uso de aspas simples ou duplas e dentro o valor da string:

```python
a = "Olá"
print(a)

#Saída:
"""
Olá
"""
```

## **Strings Multilinha**

Você pode atribuir uma string multilinha a uma variável usando três aspas:

```python
#Você pode usar três aspas duplas:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Ou três aspas simples
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

💡 **Nota:** no resultado, as quebras de linha são inseridas na mesma posição que no código.

## **Strings são matrizes**

Como muitas outras linguagens de programação populares, as strings em Python são matrizes de bytes que representam caracteres Unicode. No entanto, Python não tem um tipo de dados de caractere, um único caractere é simplesmente uma string com o comprimento 1. Os colchetes podem ser usados para acessar os elementos da string.

```python
a = "Olá, Mundo!"
print(a[0])

#Saída:
"""
O
"""
```

## **Looping através de uma string**

Como as strings são arrays, podemos percorrer os caracteres de uma string, com um loop ****`for`.

```python
for x in "banana":
 print(x)

#Saída:
"""
b
a
n
a
n
a
"""
```

## **Comprimento da string**

Para obter o comprimento de uma string, use a função `len().`

```python
a = "Comprimento"
print(len(a))

#Saída:
"""
11
"""
```

## **Verificar String**

Para verificar se uma determinada frase ou caractere está presente em uma string, podemos usar a palavra-chave `in`.

```python
texto = "Verificando a string..."
print("string" in texto)

#Saída:
"""
True
"""
```

## **Verifique se NÃO**

Para verificar se uma determinada frase ou caractere NÃO está presente em uma string, podemos usar a palavra-chave `not in`.

```python
texto = "Verificando a string..."
print("estar" not in texto)

#Saída:
"""
True
"""
```

# **Fatiando Strings**

Você pode retornar um intervalo de caracteres usando a sintaxe de fatia(slice).

Especifique o índice inicial e o índice final, separados por dois pontos, para retornar uma parte da string.

```python
b = "Olá, Mundo!"
print(b[2:5])
#Ao omitir o índice inicial, o intervalo começará no primeiro caractere:
b = "Olá, Mundo!"
print(b[:5])
#Ao omitir o índice *final* , o intervalo irá para o final:
b = "Olá, Mundo!"
print(b[2:])
#É possível utilizar indexação negativa também, começando do fim da string.
b = "Olá, Mundo!"
print(b[-11:])
```

💡 **Nota:** O primeiro caractere tem índice 0.

# **Modificar String**

Python tem um conjunto de métodos embutidos que você pode usar em strings. Confira nas referências todos os métodos de string.

```python
a = "Modificando uma string de maneira simples"
print(a.upper()) #O método upper() retorna a string em maiúsculas
print(a.lower()) #O método lower() retorna a string em letras minúsculas

#Saída:
"""
MODIFICANDO UMA STRING DE MANEIRA SIMPLES
modificando uma string de maneira simples
"""
```

## **Remover espaço em branco**

O espaço em branco é o espaço antes e/ou depois do texto real e, muitas vezes, você deseja remover esse espaço.

```python
a = "     Retirando o espaço em branco     "
print(a.strip()) #O método strip() remove qualquer espaço em branco do início e/ou do final de uma string.

#Saída:
"""
Retirando o espaço em branco
#Observe que o método funciona apenas nos espaços anteriores ao primeiro caractér e após o último.
"""
```

## **Dividir String**

O método `split()` retorna uma lista onde o texto entre o separador especificado se torna os itens da lista.

```python
a = "Divida a string aqui, exato!"
print(a.split(",")) #O separador é a vírgula

#Saída:
"""
['Divida a string aqui', ' exato!']
"""
```

# **Concatenação de String**

Para concatenar ou combinar duas strings, você pode usar o operador +.

```python
a = "Concatenando"
b = "duas strings"
c = a + " " + b
print(c)

#Saída:
"""
Concatenando duas strings
"""
```

# **Caractere de fuga**

Para inserir caracteres ilegais em uma string, use um caractere de escape.

Um caractere de escape é uma barra invertida `\` seguida pelo caractere que você deseja inserir.

Um exemplo de caractere ilegal é uma aspa dupla dentro de uma string que está entre aspas duplas:

```python
texto = "Usando o "caractere de fuga" você evita erros." 
#Você obterá um erro se usar aspas duplas dentro de uma string entre aspas duplas.
#Para corrigir esse problema, use o caractere de escape \"
texto = "Usando o \"caractere de fuga\" você evita erros."
```

Outros caracteres de escape usados em Python:

| Símbolo | Descrição |
| --- | --- |
| \' | Aspas Simples |
| \\ | Barra invertida |
| \n | Nova linha |
| \r | Carriage Return |
| \t | Tab |
| \b | Backspace |
| \f | Form Feed |
| \ooo | Valor Octal |
| \xhh | Valor Hexadecimal |

## **Formatação de String**

Para ter certeza de que uma string será exibida conforme o esperado, podemos formatar o resultado com o método `format()` que permite que você formate partes selecionadas de uma string. Às vezes, há partes de um texto que você não controla, talvez venham de um banco de dados ou da entrada do usuário da qual você não tem acesso. Para controlar esses valores, adicione espaços reservados (chaves `{}`) no texto e execute os valores por meio do método`format()`:

```python
#A sintaxe padrão
preço = float(input("Digite o valor: R$"))
msg ="O preço é {} reais"
print(msg.format(preço))

#A sintaxe aninhada
preço = float(input("Digite o valor: R$"))
print("O preço é {} reais".format(preço))

#Você pode adicionar parâmetros dentro das chaves para especificar datalhes do valor:
preço = float(input("Digite o valor: R$"))
print("O preço é {:.2f} reais".format(preço)) #flutuante com duas casas decimais
```

## **Valores Múltiplos**

Se você quiser usar mais valores, basta adicionar mais valores.

```python
preço = float(input("Digite o valor: R$"))
modelo= str(input("Digite o modelo: "))
print("O preço é {} reais e o modelo é {}".format(preço))
```

## **Números de Índice**

Você pode usar números de índice para garantir que os valores sejam colocados nos marcadores de posição corretos.

```python
unidade = 3
item = 567
preço = 49
meupedido = "E quero {0} unidades do item número {1} que custa {2:.2f} reais.".format(unidade, item, preço))
```

É possível utilizar os valores através dos índices.

```python
idade = 22
nome = "João"
print("Meu nome é {1}. {1} tenho {0} anos.".format(idade, nome))
```

## **Índices Nomeados**

Você também pode usar índices nomeados inserindo um nome entre chaves `{nome}`, mas deve usar nomes ao passar os valores dos parâmetros `.format(nome = ")`.

```python
print("Eu tenho um {nome} modelo {modelo}.".format(nome = "Monza", modelo = "1998"))
```

### Números

Existem três tipos numéricos em Python:

- `int`
- `float`
- `complex`

Variáveis de tipos numéricos são criadas quando você atribui um valor a elas:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#Para verificar o tipo de qualquer objeto em Python, use a type()função:
print(type(x))
print(type(y))
print(type(z))
```

# Int

Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado. 

```python
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
```

# Float

Float, ou "número de ponto flutuante", é um número, positivo ou negativo, que contém uma ou mais casas decimais.

```python
x = 1.10
y = 1.0
z = -35.59
w = 35e3
h = 12E4
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(h))
#Float também pode ser números científicos com um "e" para indicar a potência de 10.
```

## Complex

Os números complexos são escritos com um "j" como parte imaginária:

```python
x = 3+5j
y = 5j
z = -5j
rint(type(x))
print(type(y))
print(type(z))
```

## Conversão de Tipo

Você pode converter de um tipo para outro com o `int()`, `float()`e `complex()`métodos:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#converte de int para float:
a = float(x)
#converte de float para int:
b = int(y)
#convert de int para complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
```

<aside>
💡 **Nota:** Você não pode converter números complexos em outro tipo de número.

</aside>

### Valores Booleanos

Os booleanos representam um de dois valores: `True` ou `False`.

Na programação, você geralmente precisa saber se uma expressão é `True`ou `False`.

Você pode avaliar qualquer expressão em Python e obter uma de duas respostas, `True`ou `False`.

Quando você compara dois valores, a expressão é avaliada e o Python retorna a resposta booleana:

```python
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Resultado:
True
False
False
```

Quando você executa uma condição em uma instrução if, o Python retorna `True`ou `False`.

```python
a = 200
b = 33
if b > a:
 print("b é maior que a")
else:
 print("b não é maior que a")

#Resultado:
b não é maior que a

```

A função `bool()` permite que você avalie qualquer valor e dê a você `True` ou `False` em troca.

```python
print(bool("Olá"))
print(bool(15))

#Resultado:
True
True
```

De fato, não existem muitos valores que avaliam o booleano `False`, exceto valores vazios, tais como `()`, `[]`, `{}`, `""`, o número `0` e o valor `None`. E, claro, o valor `False` avalia para `False`.

```python
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
```

Você pode criar funções que retornam um valor booleano.

```python
def funcao() :
return True
print(funcao())

#Resultado:
True
```