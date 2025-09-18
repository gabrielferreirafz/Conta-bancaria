import os

def menu(): # apenas o menu inicial para o loop_menu funcionar
    print(' 1- exibir saldo atual \n 2- sacar \n 3- depositar \n 4- Sair do programa')
    opcao = int(input('o que você deseja fazer? '))
    return opcao

def loop_menu(): # funcionamento do menu com as opções com stop de flag
    flag = False
    while flag == False: 
        escolha_usuario = menu()
        if escolha_usuario == 1:
            os.system('clear')
            usuario.exibir()
            input('pressione enter para voltar ao menu: ')
            os.system('clear')
        elif escolha_usuario == 2:
            os.system('clear')
            usuario.sacar()
            input('pressione enter para voltar ao menu: ')
            os.system('clear')
        elif escolha_usuario == 3:
            os.system('clear')
            usuario.depositar()
            input('pressione enter para voltar ao menu: ')
            os.system('clear')
        elif escolha_usuario == 4:
            os.system('clear')
            flag = True
        else:
            print('Opção inválida. escolha uma das opções!')

class Contabancaria: # classe com atributos e metodos da contabancaria
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self):
        qtd_deposito = float(input('qual valor você deseja depositar?'))
        self.saldo += qtd_deposito
        print(f'deposito realizado com sucesso! seu saldo agora é de R${self.saldo:.2f}')

    def exibir(self):
        print(f'seu saldo atual é de R${self.saldo:.2f}')

    def sacar(self):
        qtd_sacar = float(input('qual valor você deseja sacar?'))
        if qtd_sacar > self.saldo:
            print('saldo insuficiente para saque')
        elif qtd_sacar <= self.saldo:
            self.saldo -= qtd_sacar
            print(f'saque realizado com sucesso! seu saldo atual é de R${self.saldo:.2f}')
        

saldo_inicial = 1000 
'''
   apenas um saldo inicial por enquanto para teste do código,
   depois vou fazer a integração com um banco de dados para puxar o saldo de um respectivo usuário
 '''
usuario = Contabancaria(saldo_inicial)
loop_menu()
