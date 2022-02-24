# Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.
# 10 + 20 × 30
# 42 ÷ 30
# (94 + 2) × 6 - 1
# 9^2 (9 elevado a dois)

expressao1 = 10 + 20 * 30

expressao2 = 42 / 30

expressao3 = (94 + 2) * 6 - 1

expressao4 = 9 ** 2

# Complete a tabela a seguir, respondendo True ou False.
# Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

# Expressão Resultado        Expressão Resultado
# a == c    ○ True ○ False   b > a     ○ True ○ False
# a < b     ○ True ○ False   c >= f    ○ True ○ False 
# d > b     ○ True ○ False   f >= c    ○ True ○ False
# c != f    ○ True ○ False   c <= c    ○ True ○ False
# a == b    ○ True ○ False   c <= f    ○ True ○ False
# c < d     ○ True ○ False

# False (a==c)
# True  (a<b)
# False (d>b)
# False (c!=f)
# False (a==b)
# False (c<d)
# True (b>a)
# True (c>=f)
# True (f>=c)
# True (c<=c)
# True (c<=f)


# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

# materia1 >= 7 and materia2 >= 7 and materia3 >= 7. Abaixo uma das formas de se fazer

def aprovado(materia1, materia2, materia3):
  if (materia1 >= 7 and materia2 >= 7 and materia3 >= 7):
    print('Este aluno foi aprovado')
  else:
    print('Aluno reprovado')
    
print(aprovado(4, 7, 8))

# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite o percentual de desconto: '))

valorDesconto = (preco * desconto) / 100
aPagar = preco - valorDesconto

print('O produto custa R$ %15.9f mas tem um desconto de %9.5f' % (desconto, preco))
print('Valor do desconto em cima R$ %15.9f' % valorDesconto)
print('O valor do pagamento de R$ %15.9f é R$ ' % aPagar)

# Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

#      9 × C
#  F = ----- + 32
#        5

C = float(input('Digite a temperatura em Celsius: '))

F = ((9 * C) / 5) + 32

print('%5.2fCelsius é igual a %5.2fFareinheit' % (C, F))

# Faça um programa para exibir os números de 1 a 100.

numeroInicial = 1

while numeroInicial <= 100:
  print(numeroInicial)
  numeroInicial = numeroInicial + 1

# Faça um programa para escrever a contagem regressiva do lançamento de um foguete

contagemRegressiva = 10

while contagemRegressiva >= 0:
  print(contagemRegressiva)
  contagemRegressiva = contagemRegressiva - 1
print('FOGO!')

# Faça um programa para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

valorDigitado = int(input('Digite um número: '))
numeroInicial = 1

while numeroInicial <= valorDigitado:
  print(numeroInicial)
  numeroInicial = numeroInicial + 2

# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

numero = int(input('Digite um número qualquer para verificarmos se é primo ou não: '))

if (numero < 0):
  print('Número é inválido. Digite apenas valores positivos')
if (numero == 0 or numero == 1):
  print('Os números 0 e 1 não são primos')
else:
  if (numero == 2):
    print('2 é primo')
  elif (numero % 2 == 0):
    print(f'{numero} não é primo, porque 2 é o único número par primo')
  else:
    x = 3
    while (x < numero):
      if numero % x == 0:
        break
      x = x + 2
    if (x == numero):
      print(f'{numero} É PRIMO')
    else:
      print(f'{numero} não é primo, porque é divisível por {x}')

# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

array1 = []
array2 = []

while True:
  numeroDigitado = int(input('Digite um valor para o primeiro array: '))
  
  if numeroDigitado == 0:
    break
  
  array1.append(numeroDigitado)
  
while True:
  numeroDigitado = int(input('Digite um valor para o segundo array: '))
  
  if numeroDigitado == 0:
    break
  
  array2.append(numeroDigitado)
  
array3 = array1[:]
array3.extend(array2)

x = 0
while x < len(array3):
  print(f'{x}: {array3[x]}')
  x = x + 1

# Testando meu arquivo indo para o github atualizado...