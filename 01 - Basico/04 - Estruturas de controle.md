# ESTRUTURAS DE CONTROLE

# If & Else

Uma "declaração if" é escrita usando a palavra-chave  `if` .

```python
a = 33
b = 200
if b > a:
 print("b é maior que a")

#Resultado
b é maior que a
```

Python depende de indentação (espaço em branco no início de uma linha) para definir o escopo no código. Outras linguagens de programação costumam usar chaves para esse propósito.

### Elif

A palavra-chave `elif` é a forma de dizer "se as condições anteriores não eram verdadeiras, tente esta condição".

```python
a = 33
b = 33
if b > a:
 print("b é maior que a")
elif a == b:  
 print("a e b são iguais")

#Resultado
a e b são iguais
```

### Else

A palavra-chave `else` captura qualquer coisa que não seja capturada pelas condições anteriores.

```python
a = 200
b = 33
if b > a:  
 print("b é maior que a")
elif a == b:  
 print("a e b são iguais")
else:  
 print("a é maior que b")

#Resultado:
a é maior que b
```

<aside>
💡 **Nota:** Você também pode ter um `else` sem `elif`

</aside>

### Short Hand If

Se você tiver apenas uma instrução para executar, pode colocá-la na mesma linha da instrução if.

```python
a = 200
b = 33
if a > b: print("a é maior que b")
```

### Short Hand If ... Else

Se você tem apenas uma instrução para executar, uma para if e outra para else, você pode colocar tudo na mesma linha:

```python
a = 2
b = 330
print("A") if a > b else print("B")
```

<aside>
💡 **Nota:** Essa técnica é conhecida como **Operadores Ternários** ou **Expressões Condicionais** .

</aside>

Você também pode ter várias instruções else na mesma linha:

```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

### And

A palavra-chave `and` é um operador lógico, e é usado para combinar declarações condicionais.

```python
a = 200
b = 33
c = 500
if a > b and c > a:  print("Ambas condições são Verdadeiras")

#Resultado:
Ambas condições são Verdadeiras
```

### Or

A palavra-chave `or` é um operador lógico e também é usada para combinar declarações condicionais.

```python
a = 200
b = 33
c = 500
if a > b or a > c: print("Pelo menos uma das condições é Verdadeira") #a > b

#Resultado:
Pelo menos uma das condições é Verdadeira
```

### Aninhando If

Você pode ter instruções `if` dentro de instruções`if`, isso é chamado de instruções aninhadas `if` (nested if).

```python
x = 41
if x >  10:
 print("Acima de 10 ")
if x > 20:
 print("e também de 20,")
if x > 50:
 print("e também de 50.")
else:
 print("mas não acima de 50")

#Resultado:
Acima de 10 
e também de 20,
mas não acima de 50
```

### A declaração pass

Declarações `if` não podem estar vazias, mas se por algum motivo você tiver uma declaração `if` sem conteúdo, adicione a declaração `pass` para evitar um erro.

```python
a = 33
b = 200
if b > a:
 pass
print("O erro no if vazio foi contornado")

#Resultado:
O erro no if vazio foi contornado
```

# Loop while

Com o loop `while` podemos executar um conjunto de instruções enquanto uma condição for verdadeira.

```python
i = 1
while i < 6:
 print(i)
 i += 1

#Resultado:
1
2
3
4
5
```

<aside>
💡 **Nota:** lembre-se de incrementar i, ou então o loop continuará para sempre, pois o valor de i permanece inalterado, a medida que realizamos o incremente a condição é avaliada novamente.

</aside>

### A declaração break

Com a instrução `break`, podemos parar o loop mesmo se a condição while for verdadeira:

```python
i = 1
while i < 6:
 print(i)
 if i == 3:
  break  
 i += 1

#Resultado:
1
2
3
```

### A declaração continue

Com a instrução `continue`, podemos parar a iteração atual e continuar com a próxima:

```python
i = 0
while i < 6:
 i += 1  
 if i == 3:
  continue
 print(i)

#Resultado:
1
2
4
5
6
```

### A declaração else

Com a instrução `else` , podemos executar um bloco de código uma vez, quando a condição não for mais verdadeira.

```python
i = 1
while i < 6:
 print(i)  
 i += 1
else:  
 print("i não é menor que 6")

#Resultado:
1
2
3
4
5
i não é menor que 6
```

# Loop FOR

Um laço `for` é utilizado para a iteração através de uma sequência (isto é, quer uma lista, uma tupla, um dicionário, um conjunto ou uma cadeia).

Isso é menos parecido com a palavra-chave for em outras linguagens de programação e funciona mais como um método iterador, como encontrado em outras linguagens de programação orientadas a objetos.

Com o loop for , podemos executar um conjunto de instruções, uma vez para cada item em uma lista, tupla, conjunto etc.

Imprima cada fruta em uma lista de frutas:

```python
frutas = ["maçã", "banana", "cereja"]
for x in frutas:  
 print(x)

#Resultado:
maçã
banana
cereja
```

O loop for não requer uma variável de indexação para definir de antemão.

### Looping através de uma string

Até mesmo strings são objetos iteráveis, eles contêm uma sequência de caracteres.

```python
for x in "banana":
 print(x)

#Resultado:
b
a
n
a
n
a
```

### **A declaração break**

Com a instrução `break` , podemos interromper o loop antes que ele percorra todos os itens.

```python
frutas = ["maçã","banana","cereja"]
for x in frutas:
 print(x)
 if x == "banana":
  break

#Resultado:
maçã
banana
```

Válido mostrar um detalhe interessante, quando a impressão é realizado pós-avaliação do if, o resultado é diferente.

```python
frutas = ["maçã", "banana", "cereja"]
for x in frutas:
 if x == "banana":
  break
 print(x)

#Resultado:
maçã
```

### **A declaração continue**

Com a instrução `continue` , podemos interromper a iteração atual do loop e continuar com a próxima.

```python
frutas = ["maçã", "banana", "cereja"]
for x in frutas:  
 if x == "banana":
  continue
 print(x)

#Resultado:
maçã
cereja
```

Para percorrer um conjunto de código um determinado número de vezes, podemos usar a função `range()`.

A função range() retorna uma sequência de números, começando em 0 por padrão, e incrementos em 1 (por padrão), e termina em um número especificado.

```python
for x in range(6):
 print(x)

#Resultado:
0
1
2
3
4
5
```

O padrão da função range() tem como valor inicial 0, no entanto, é possível especificar o valor inicial adicionando um parâmetro: range (2,6), que significa valores de 2 a 6 (mas não incluindo 6).

```python
for x in range(2, 6):
 print(x)

#Resultado:
2
3
4
5
```

O padrão da função range() é incrementar a sequência em 1, no entanto, é possível especificar o valor do incremento adicionando um terceiro parâmetro: range (2, 6, 2), significa valores de 2 a 6(mas não incluindo 6), incrementando 2.

```python
for x in range(2, 6, 2):
 print(x)

#Resultado:
2
4
```

### Loop For com else

A palavra-chave `else` em um loop `for` especifica um bloco de código a ser executado quando o loop for concluído.

```python
for x in range(6):
 print(x)
else:
 print("O laço terminou!")

#Resultado:
1
2
3
4
5
O laço terminou!
```

**Nota:** O `else` NÃO será executado se o loop for interrompido por uma instrução `break`.

```python
for x in range(6):
 if x == 3: break
 print(x)
else:
 print("O laço terminou!")

#Resultado:
0
1
2
```

### **Loops aninhados**

Um loop aninhado é um loop dentro de um loop. O "loop interno" será executado uma vez para cada iteração do "loop externo".

```python
adjetivos = ["vermelha", "grande", "gostosa"]
frutas = ["maçã", "banana", "cereja"]
for x in frutas:
 for y in adjetivos:
  print(x, y)

#Resultado:
maçã vermelha
maçã grande
maçã gostosa
banana vermelha
banana grande
banana gostosa
cereja vermelha
cereja grande
cereja gostosa

```

### **A declaração pass**

Assim como nas outras estruturas, os laços `for` não podem estar vazios, mas se, por algum motivo, você tiver um `for`loop sem conteúdo, insira a `pass`instrução para evitar um erro.

```python
for x in [0, 1, 2]:
 pass
```