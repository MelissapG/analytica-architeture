import time

class Tamagoshi:
    nome = ''
    especie = ''
    fome = 0

    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    #retorna o estado do animal
    def __str__(self):
        return '{} está com {} de fome.'.format(self.nome, self.fome)

    #valor da fome do animal aumenta em 1
    def andar(self):
        self.fome += 1
    
    #fome do animal diminui conforme quantidade, caso fome < quantidade:
    #retorna ao usuário que animal comeu até ficar saciado e deixou o resto da comida no prato
    def comer(self, quantidade):
        if(self.fome<quantidade):
            self.fome = 0
            print( '{} comeu até ficar saciado e deixou o resto da comida no prato.'.format(self.nome))
        else:
            self.fome -= quantidade
            print('{} foi alimentado.'.format(self.nome))


nome = input("Digite o nome do seu tamagoshi: ")
especie = input("Digite a espécie do seu tamagoshi: ")

meuBichinho = Tamagoshi(nome, especie)
time.sleep(1)

while(True):
    print('\n--- Menu ---\n')
    print('Opção 1: Alimentar o tamagoshi.\n')
    print('Opção 2: Andar com o tamagoshi.\n')
    print('Opção 3: Mostrar o estado atual do tamagoshi.\n')
    print('Opção 4: Finalizar execução.\n')
    
    escolha = input()
    if(escolha == '1'):
        quantidade = input('Digite a quantidade de comida: ')
        meuBichinho.comer(int(quantidade))
    elif(escolha == '2'):
        meuBichinho.andar()
    elif(escolha == '3'):
        print(meuBichinho.__str__())
        time.sleep(1)
        continue
    elif(escolha == '4'):
        break
    else:
        print('Esta opção não existe.')

    time.sleep(1)
    print(meuBichinho.__str__())
    time.sleep(2)