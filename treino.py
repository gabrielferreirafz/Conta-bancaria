import os

def limpar_tela(): # função para limpar a tela
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(): # apenas o menu inicial para o loop_menu funcionar
    print(' 1- exibir saldo atual \n 2- sacar \n 3- depositar \n 4- Sair do programa')
    try:
        opcao = int(input('o que você deseja fazer? '))
        return opcao
    except ValueError:
        return 0
def loop_menu(): # funcionamento do menu com as opções com stop de flag
    flag = False
    while flag == False: 
        escolha_usuario = menu()
        if escolha_usuario == 1:
            limpar_tela()
            usuario.exibir()
            input('pressione enter para voltar ao menu: ')
            limpar_tela()
        elif escolha_usuario == 2:
            limpar_tela()
            usuario.sacar()
            input('pressione enter para voltar ao menu: ')
            limpar_tela()
        elif escolha_usuario == 3:
            limpar_tela()
            usuario.depositar()
            input('pressione enter para voltar ao menu: ')
            limpar_tela()
        elif escolha_usuario == 4:
            limpar_tela()
            flag = True
        else:
            limpar_tela()
            print('Opção inválida. escolha uma das opções!')

class Contabancaria: # classe com atributos e metodos da contabancaria
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self):
        try:
            qtd_deposito = float(input('qual valor você deseja depositar?'))
            if qtd_deposito <= 0:
                print('valor inválido para depósito')
            else:
                self.saldo += qtd_deposito
                print(f'deposito realizado com sucesso! seu saldo agora é de R${self.saldo:.2f}')
        except ValueError:
            print('valor inválido para depósito')

    def exibir(self):
        print(f'seu saldo atual é de R${self.saldo:.2f}')

    def sacar(self):
        try:
            qtd_sacar = float(input('qual valor você deseja sacar?'))
            if qtd_sacar > self.saldo:
                print('saldo insuficiente para saque')
            elif qtd_sacar <= 0:
                print('valor inválido para saque')
            elif qtd_sacar <= self.saldo:
                self.saldo -= qtd_sacar
                print(f'saque realizado com sucesso! seu saldo atual é de R${self.saldo:.2f}')
        except ValueError:
            print('valor inválido para saque')
        

saldo_inicial = 1000 
'''
   apenas um saldo inicial por enquanto para teste do código,
   depois vou fazer a integração com um banco de dados para puxar o saldo de um respectivo usuário
 '''
usuario = Contabancaria(saldo_inicial)
loop_menu()
limpar_tela()