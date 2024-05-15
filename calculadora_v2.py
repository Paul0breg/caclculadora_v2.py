saída=''
def adição(num1,num2):
    return num1 + num2
def subtração(num1, num2):
    return num1 - num2
def multiplicação(num1, num2):
    return num1 * num2 
def divisão(num1, num2):
    if num2 == 0:
      return ("não foi possível realizar a divisão por 0")
    else:
        return num1 / num2
def calculadora(num1, num2, operação):
    if operação == '+' or operação == adição:
        return adição(num1, num2)
    elif operação == '-' or operação == subtração:
        return subtração(num1, num2)
    elif operação == '*' or operação == multiplicação:
        return multiplicação(num1, num2)
    elif operação == '/' or operação == divisão:
        return divisão(num1 , num2)
    else: 
        return 'operação iválida'
while saída.lower()!= 'n':
    num1= float(input('digite o primeiro número: '))
    num2=float(input('digite o segundo número: '))
    operação=input('digite a operação matemática(+,-,*,/): ')
    resultado=calculadora(num1,num2,operação)
    print('resultado da operação: ', resultado)
    saída=input('deseja continuar (S/N)? ')