def mensagem():
    print('Criando no python')

def tabuada():
    n = int(input('Digite um número que deseja ver a tabuada: '))
    for x in range (1,11):
        print('{}  X {:2} = {:2}'.format(n, x, n*x))

mensagem()
tabuada()
  